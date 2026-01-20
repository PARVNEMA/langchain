from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage,AIMessage
load_dotenv()

llm = HuggingFaceEndpoint(
repo_id="deepseek-ai/DeepSeek-R1", # Replace as needed
temperature=0.7,
max_new_tokens=100
)

chat_model =ChatHuggingFace(llm=llm)

messages =[HumanMessage(content="Hello, how are you?")]
response = chat_model.invoke("Write a short poem about Bangalore sunsets.")
messages.append(AIMessage(content=response.content))
print(response.content)