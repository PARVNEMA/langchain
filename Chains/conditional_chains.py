from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.runnables import RunnableBranch,RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from typing import Literal
load_dotenv()

llm = HuggingFaceEndpoint(
repo_id="deepseek-ai/DeepSeek-R1", # Replace as needed
temperature=0.7,
max_new_tokens=100
)

class feedback(BaseModel):
  sentiment:Literal['positive','negative']=Field(description='Sentiment of the user can be')

parser2= PydanticOutputParser(pydantic_object=feedback)

model1 =ChatHuggingFace(llm=llm)

model2= ChatGoogleGenerativeAI(
  model='gemini-2.5-flash',
  temperature=1,
)

template1=PromptTemplate(template= 'classify the sentiment of the user as positive or negative  {text} \n {format_instructions}',input_variables=['text'],partial_variables={'format_instructions':parser2.get_format_instructions()})

template2=PromptTemplate(template= 'give simple response on positive feedback of user {text}',input_variables=['text'])

template3=PromptTemplate(template= 'give simple response on negative feedback of user {text} ',input_variables=['text'])

parser=StrOutputParser()

classifier_chain=template1 | model2 | parser2

conditional_chain = RunnableBranch(
  (lambda x:x.sentiment =='positive',template2 | model1 | parser),
  (lambda x:x.sentiment =='negative',template3 | model2 | parser),
  RunnableLambda(lambda x:'sentiment cannot be identified')
)

chain = classifier_chain | conditional_chain

result = chain.invoke({'text':'worst product purchase'})
print(result)

print(chain.get_graph().draw_ascii())