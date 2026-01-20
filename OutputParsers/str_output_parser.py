from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
repo_id="deepseek-ai/DeepSeek-R1", # Replace as needed
temperature=0.7,
max_new_tokens=100
)

chat_model =ChatHuggingFace(llm=llm)

template1=PromptTemplate(template='write a detailed prompt on the following {topic}',
                          input_variables=["topic"])
template2=PromptTemplate(template='write a short 5 lines summary on following {text}',
                          input_variables=["text"])

parser= StrOutputParser()

chain =template1 | chat_model | parser | template2 | chat_model |parser

result = chain.invoke({'topic':"White hole"})

print(result)



