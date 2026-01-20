from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough
load_dotenv()


model2= ChatGoogleGenerativeAI(
  model='gemini-3-flash-preview',
  temperature=1,
)

template1=PromptTemplate(template= 'generate very short joke for {text}',input_variables=['text'])
template2=PromptTemplate(template= 'generate explanation of joke for {text}',input_variables=['text'])


parser=StrOutputParser()

initial_chain= RunnableSequence(template1,model2,parser)

chain = RunnableParallel({
  "joke":RunnablePassthrough(),
  "explanation":RunnableSequence(template2 , model2 , parser),
})

merge_chain =RunnableSequence(initial_chain,chain)
result = merge_chain.invoke({'text':'ai'})
print(result)