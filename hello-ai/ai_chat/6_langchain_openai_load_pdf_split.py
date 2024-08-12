from langchain_openai import OpenAI, OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA

output_parser = StrOutputParser()


llm = OpenAI(temperature=0.9, base_url="https://free.gpt.ge/v1/",max_tokens=1024)


prompt = ChatPromptTemplate.from_template("""Answer the following question based only on the provided context:

<context>
{context}
</context>

Question: {input}""")

chain = prompt | llm | output_parser
docs=[]
loader1 = PyPDFLoader("~/Desktop/关于质控部招募研发工程师的公告.pdf")
docs.extend(loader1.load())
loader2 = PyPDFLoader("~/Desktop/关键技术-长期计划导入.pdf")
docs.extend(loader2.load())

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
split_docs = text_splitter.split_documents(docs)

embeddings = OpenAIEmbeddings(base_url="https://free.gpt.ge/v1/")
vectorstore = Chroma.from_documents(split_docs, embeddings, collection_name="my_docs")

qa_chain = RetrievalQA.from_chain_type(llm, chain_type="stuff", retriever=vectorstore.as_retriever())



while True:
    try:
        user_input = input("请输入问题：")
        if user_input.lower() == "exit":
            break
        print(qa_chain.run(user_input))
    except Exception as e:
        print(e)
        break



