from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import requests
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
@tool
def multiply(a: int, b: int) -> int:
  """Given 2 numbers a and b this tool returns their product"""
  return a * b

llm=ChatGoogleGenerativeAI(model="gemini-3-flash-preview",temperature=0.5)

llm_tools=llm.bind_tools([multiply])

query = HumanMessage('can you multiply 3 with 1000')
messages = [query]

result = llm_tools.invoke(messages)
# ? AI message
messages.append(result)

tool_result = multiply.invoke(result.tool_calls[0])

# ? tool message

messages.append(tool_result)

print(llm_tools.invoke(messages).content)