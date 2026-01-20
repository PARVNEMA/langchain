from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableBranch
load_dotenv()


model2= ChatGoogleGenerativeAI(
  model='gemini-3-flash-preview',
  temperature=1,
)

template1=PromptTemplate(template= 'generate very report for {text}',input_variables=['text'])
template2=PromptTemplate(template= 'generate very short resport for {text}',input_variables=['text'])

parser=StrOutputParser()

initial_chain=RunnableSequence(template1,model2,parser)

chain = RunnableBranch({
  (lambda x:len(x.split())>500,RunnableSequence(template2,model2,parser)),
  (RunnablePassthrough()),
})

main_chain=RunnableSequence(initial_chain,chain)
result = main_chain.invoke({'text':'ai'})
print(result)