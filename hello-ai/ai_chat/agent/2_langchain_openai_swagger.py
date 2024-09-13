from langchain_openai import OpenAI
from langchain.chains.api.base import APIChain
from langchain.prompts import PromptTemplate
from langchain.tools import BaseTool
from langchain.agents import initialize_agent, AgentType
import requests
from urllib.parse import urlparse
import json


llm = OpenAI(temperature=0, base_url="https://free.gpt.ge/v1/")


api_docs = requests.get("https://clubapi.sit.yumimiao.cn/v2/api-docs").text
api_docs = api_docs.replace('clubapi.sit.yumimiao.cn', 'https://clubapi.sit.yumimiao.cn')

api_token = ""
api_docs = api_docs + f"\nAll requests to this API should include an 'Token' header with the value 'Bearer {api_token}'."

allowed_domains = ["https://clubapi.sit.yumimiao.cn", 'http://clubapi.sit.yumimiao.cn']

# 创建自定义的请求函数，用于添加 token
def custom_request(a, api_endpoint: str):
    print(type(a))
    print(api_endpoint)
    # headers = {"Authorization": f"Bearer {api_token}"}
    # full_url = f"{api_url}{api_endpoint}"
    # response = requests.get(full_url, headers=headers)
    # return response.text

template = """You are given the below API Documentation:
{api_docs}
Using this documentation, generate the full API url to call for answering the user question.
You should build the API url in order to get a response that is as short as possible, while still getting the necessary information to answer the question. Pay attention to deliberately exclude any unnecessary pieces of data in the API call.
All requests to this API should include an 'Authorization' header with the value '{api_token}'.

Question:{question}
API url:"""

url_prompt = PromptTemplate(
    input_variables=[
        "api_docs",
        "api_token",
        "question"
        
    ],
    template=template,
)

chain = APIChain.from_llm_and_api_docs(llm, api_docs, 
                                       limit_to_domains=allowed_domains, 
                                       headers= {"Authorization": api_token},
                                    # api_url_prompt = url_prompt,
                                       verbose=True)


user_question = "请查询会员卡列表"
answer = chain.invoke({"question": user_question, "api_token": api_token})
print(answer)
