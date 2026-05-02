from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import ArxivLoader
import bs4

loader = TextLoader("speech.txt")
loader
text_docs = loader.load()
print(text_docs)

loader = PyPDFLoader("finalNLP.pdf")
docs = loader.load()
print(docs)
print(type(docs[0]))

loader = WebBaseLoader(
    web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
    bs_kwargs=dict(
        parse_only=bs4.SoupStrainer(
            class_=("post-content", "post-title", "post-header")
        ),
    ),
)


docs1 = loader.load()
print(docs1)


docs3 = ArxivLoader(query="1706.03762", load_max_docs=2).load()
print(len(docs3))
