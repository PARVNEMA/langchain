from langchain_community.tools import tool


# ? remember tools decorator is important to make it work with llm and also add type hints properly so llm know the type to call the function properly

@tool
def multiply(a:int,b:int) ->int :
  """multiply 2 numbers""" # ? doc strings
  return a *b

# ? it becomes runnable
result = multiply.invoke({"a":4,"b":5})

print(result)

# * Every tools has name,description and args whether it is built in or custom
print(multiply.name)
print(multiply.description)
print(multiply.args)

# ? how llm sees it
print(multiply.args_schema.model_json_schema())
