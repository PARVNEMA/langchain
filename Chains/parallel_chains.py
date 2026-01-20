from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.runnables import RunnableParallel
load_dotenv()

llm = HuggingFaceEndpoint(
repo_id="deepseek-ai/DeepSeek-R1", # Replace as needed
temperature=0.7,
max_new_tokens=100
)

model1 =ChatHuggingFace(llm=llm)

model2= ChatGoogleGenerativeAI(
  model='gemini-3-flash-preview',
  temperature=1,
)

template1=PromptTemplate(template= 'generate very short notes for {text}',input_variables=['text'])
template2=PromptTemplate(template= 'generate very short quiz for {text}',input_variables=['text'])
template3=PromptTemplate(template= 'merge both the output into single {text1} {text2}',input_variables=['text1','text2'])

parser=StrOutputParser()

parallel_chain = RunnableParallel({
  'notes':template1 | model1 |parser,
  'quiz':template2 | model2 |parser
})

merge_chain = template3 | model1 |parser

chain = parallel_chain | merge_chain

text='''hello python programming '''

result = chain.invoke({'text':text})
print(result)