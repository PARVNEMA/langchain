from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel
load_dotenv()


model2= ChatGoogleGenerativeAI(
  model='gemini-3-flash-preview',
  temperature=1,
)

template1=PromptTemplate(template= 'generate very short tweet for {text}',input_variables=['text'])
template2=PromptTemplate(template= 'generate very short linkdeln post for {text}',input_variables=['text'])

parser=StrOutputParser()


chain = RunnableParallel({
  "tweet":RunnableSequence(template1 , model2 , parser),
  "linkdeln":RunnableSequence(template2 , model2 , parser),
})
result = chain.invoke({'text':'ai'})
print(result)