from langchain_core.prompts import PromptTemplate

template= PromptTemplate(
  """
  You are a helpful assistant that translates {input_language} to {output_language}.
  {input}
  """,
  input_variables=["input_language", "output_language", "input"],
  validate_template=True
)

template.save('tranlate_prompt.json')
