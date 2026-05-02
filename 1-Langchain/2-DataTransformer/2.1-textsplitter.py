from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# loader = PyPDFLoader("attention.pdf")
# docs = loader.load()

# text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=10)
# final_docs = text_splitter.split_documents(docs)
# final_docs
# print(final_docs[0])


speech= ""
with open("speech.txt",'r') as f:
    speech =f.read()

text_splitter = RecursiveCharacterTextSplitter(chunk_size =50, chunk_overlap =10) 

text = text_splitter.create_documents([speech])
print(text[0])
print(text[1])
print(text)