from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
from dotenv import load_dotenv

load_dotenv()

## chat model
llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    temperature=0.5,
    max_input_tokens=10

)

chat_history=[
  SystemMessage(content="You are a helpful assistant"),
]
while(True):
    user_input =input("User: ")
    chat_history.append(HumanMessage(content=user_input))
    if(user_input == "exit"):
      break
    result = llm.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content[0]['text']))
    print("AI :", result.content[0]['text'])

