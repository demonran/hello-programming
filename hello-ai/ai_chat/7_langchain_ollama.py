from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.documents import Document
import time

output_parser = StrOutputParser()


llm = OllamaLLM(temperature=0.9, model='qwen2')

# prompt = ChatPromptTemplate.from_messages([
#     ("system", "You are a helpful assistant."),
#     ("user", "{input}")
# ])

prompt = ChatPromptTemplate.from_template("""Answer the following question based only on the provided context:

<context>
{context} 
</context>

Question: {input}""")

chain = prompt | llm | output_parser

docs = [
    Document(page_content="xxxsss刘燃的电话是13111111111")
]

start = time.time()
print(chain.invoke({
    "input": "刘燃的电话是多少？",
    "context": docs
    }))
print("耗时:", time.time() - start)

