# from langchain_openai import OpenAIEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

# embeddings = OpenAIEmbeddings(
#     model = "text-embedding-3-large",
#     dimensions = 64
# )

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    dimensions=64
)

vector = embeddings.embed_query("What are the planets in our solar system?")

print(vector)