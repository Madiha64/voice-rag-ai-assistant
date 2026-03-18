from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import CharacterTextSplitter

# load document
with open("data/rag_docs.txt", "r", encoding="utf-8") as f:
    text = f.read()

# split text into chunks
text_splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=20
)

docs = text_splitter.split_text(text)

# load embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# create vector database
db = FAISS.from_texts(docs, embeddings)

# save database locally
db.save_local("vector_db")

print("✅ Vector database created successfully!")