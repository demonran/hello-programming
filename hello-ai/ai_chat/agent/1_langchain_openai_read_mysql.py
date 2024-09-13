from langchain_community.utilities import SQLDatabase
import pymysql

pymysql.install_as_MySQLdb()

user = ''
password = ''
host = ''
db = ''

db = SQLDatabase.from_uri(f"mysql+mysqldb://{user}:{password}@{host}/{db}")

def get_schema(_):
    return db.get_table_info()


def run(query):
    return db.run(query)

# print(get_schema())

from langchain_openai import OpenAI

llm = OpenAI(temperature=0, base_url="https://free.gpt.ge/v1/")

from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from langchain_core.prompts import ChatPromptTemplate

template = """
根据下表结构，编写一个SQL查询语句，查询出满足条件的数据。
{schema}

问题：{question}
SQL查询：
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", "给你一个问题，转换成SQL查询，直接返回查询语句."),
    ("human",template),
])

sql_chain = (
    RunnablePassthrough.assign(schema=get_schema)
    | prompt
    | llm.bind(stop="\n SQL查询：")
    | StrOutputParser()
)
# sql = sql_chain.invoke({"question":"有多个用户？"})
# print(sql)
# print(run(sql))

template = """
根据下表结构、问题、SQL查询和SQL响应，编写问题答案。。
{schema}

问题：{question}
SQL查询：{query}
SQL响应：{response}
答案：
"""

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "根据下表结构、问题、SQL查询和SQL响应，编写问题答案，同时把sql打印出来"),
    ("human",template),
])

full_chain =(RunnablePassthrough.assign(query=sql_chain) 
             | RunnablePassthrough.assign(
                 schema=get_schema, 
                 response=lambda x: run(x["query"])
                 )
            | prompt_template
            | llm
            ) 

print(full_chain.invoke({"question" : "Tony有什么角色？"}))