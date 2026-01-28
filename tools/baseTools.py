from langchain_community.tools import BaseTool
from typing import Type
from pydantic import BaseModel,Field
class Multiply(BaseModel):
  a:int=Field(required=True,description="first number")
  b:int=Field(required=True,description="second number")

# * all the @tool ,structured tool are created using basetool
# * it is an abstract class for implementing tools
class MultiplyTool(BaseTool):
  name = "multiply",
  args_schema: Type[BaseModel] = Multiply
  description = "multiply 2 numbers"
  def _run(self,a:int,b:int) -> int:
    return a *b
