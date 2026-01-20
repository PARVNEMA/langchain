from langchain_core.output_parsers import PydanticOutputParser
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel,Field
load_dotenv()

llm = HuggingFaceEndpoint(
repo_id="deepseek-ai/DeepSeek-R1", # Replace as needed
temperature=0.7,
max_new_tokens=100
)

chat_model =ChatHuggingFace(llm=llm)

class Person(BaseModel):
  name:str=Field(description="name of the person")
  age:int=Field(gt=18,description="age of the person")
  city:str=Field(description="place of the person")

parser= PydanticOutputParser(pydantic_object=Person)

template1=PromptTemplate(template='create a demo person object of person in {place}  {format_instructions}',
          input_variables=['place'],
          partial_variables={'format_instructions':parser.get_format_instructions()})


chain = template1 | chat_model | parser

final_result = chain.invoke('jabalpur')
print(final_result)
print(type( final_result))



