from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
repo_id="deepseek-ai/DeepSeek-R1", # Replace as needed
temperature=0.7,
max_new_tokens=100
)

chat_model =ChatHuggingFace(llm=llm)

parser= JsonOutputParser()


template1=PromptTemplate(template='write a short 5 lines summary jabalpur  {format_instructions}',
          input_variables=[],
          partial_variables={'format_instructions':parser.get_format_instructions()})


prompt=template1.format()

result =chat_model.invoke(prompt)

final_result =parser.parse(result.content)
print(final_result)
print(type( final_result))



