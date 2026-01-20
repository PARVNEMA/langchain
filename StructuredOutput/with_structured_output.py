from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional

load_dotenv()

model = ChatGoogleGenerativeAI(
  model="gemini-3-flash-preview",
  temperature=0,
  max_tokens=100,
)

class Review(TypedDict):
  movie_name:Annotated[Optional[str],"name of the movie"]
  rating: Annotated[Optional[int],"rating of the movie"]
  review:  Annotated[Optional[str],"review of the movie"]

structured_model = model.with_structured_output(Review,method="json_mode")

result = structured_model.invoke(
  "Give a movie review with movie_name, rating (1–5), and review for the movie Dhurander. "
)

print(result)
print(result["movie_name"])
print(result["rating"])
print(result["review"])
