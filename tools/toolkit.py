from langchain_community.tools import tool


# ? toolkit wraps up similar kind of tools
@tool
def multiply(a:int,b:int) ->int :
  """multiply 2 numbers""" # ? doc strings
  return a *b
@tool
def add(a:int,b:int) ->int :
  """add 2 numbers""" # ? doc strings
  return a +b

class calctoolkit:
  def get_tools(self):
    return [multiply,add]

toolkit = calctoolkit()
tools = toolkit.get_tools()