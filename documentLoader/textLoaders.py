from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model= ChatGoogleGenerativeAI(
  model='gemini-2.5-flash',
  temperature=0.7,
)

parser=StrOutputParser()

prompt=PromptTemplate(template="generate english translation for it {text}",
                      input_variables=['text'])

loader =TextLoader(file_path='documentLoader/demo.txt',encoding='utf-8')

docs =loader.load()

print(docs)
print(type (docs))

chain = prompt | model | parser

print(chain.invoke({'text':docs[0].page_content}))