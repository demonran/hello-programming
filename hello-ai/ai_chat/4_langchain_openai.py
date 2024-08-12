from langchain_openai import OpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.documents import Document

output_parser = StrOutputParser()


llm = OpenAI(temperature=0.9, base_url="https://free.gpt.ge/v1/")

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
    Document(page_content="刘燃的电话是13111111111")
]

print(chain.invoke({
    "input": "刘燃的电话是多少？",
    "context": docs
    }))

