from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

## chat model
llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    temperature=0.5
)

print(llm.invoke("what is the capital of india ?"))
