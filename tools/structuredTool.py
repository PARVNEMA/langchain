from langchain_community.tools import StructuredTool
from pydantic import BaseModel,Field
## ? strcutured tools are stricter than normal @tools decoratos as it uses pydantic

class Multiply(BaseModel):
  a:int=Field(required=True,description="first number")
  b:int=Field(required=True,description="second number")

def multiply_tool(a:int,b:int) ->int :

  return a *b

multiply_tool =StructuredTool.from_function(
func=multiply_tool,
description="multiply 2 numbers",
args_schema=Multiply,
name="multiply"
)

result = multiply_tool.invoke({"a":4,"b":5})
print(result)
print(multiply_tool.name)