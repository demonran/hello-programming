from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader
import time

output_parser = StrOutputParser()


llm = Ollama(temperature=0.9, model='qwen2')


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

while True:
    try:
        user_input = input("请输入问题：")
        if user_input.lower() == "exit":
            break
        start = time.time()
        print(chain.invoke({
            "input": user_input,
            "context": docs
            }))
        print("耗时:", time.time() - start)
    except Exception as e:
        print(e)
        break



