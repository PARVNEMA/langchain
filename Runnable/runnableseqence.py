from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
load_dotenv()


model2= ChatGoogleGenerativeAI(
  model='gemini-3-flash-preview',
  temperature=1,
)

template1=PromptTemplate(template= 'generate very short notes for {text}',input_variables=['text'])

parser=StrOutputParser()


chain = RunnableSequence(template1 , model2 , parser)
result = chain.invoke({'text':'what is ai write a joke about it'})
print(result)