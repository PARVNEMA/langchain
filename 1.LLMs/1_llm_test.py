from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = GoogleGenerativeAI(
    model="gemini-3-flash-preview",
)

print(llm.invoke("what is the capital of india?"))

