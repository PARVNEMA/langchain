from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

template = PromptTemplate(template='give five facts about {topic}',
                          input_variables=['topic'])

model= ChatGoogleGenerativeAI(
  model='gemini-3-flash-preview',
  temperature=1,
)

parser= StrOutputParser()

chain = template | model | parser

result=chain.invoke({'topic':'virat kohli'})

print(result)
chain.get_graph().draw_png()

