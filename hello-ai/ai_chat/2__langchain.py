from langchain import OpenAI
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.embeddings import OpenAIEmbeddings

# with open('test.txt') as f:
#     text = f.read()
#     print(text)


# 初始化 OpenAI 模型
llm = OpenAI( model_name='gpt-3.5-turbo', temperature=0.9)

# 加载文件
loader = TextLoader('test.txt')

# 创建索引
embeddings = OpenAIEmbeddings(openai_api_key=open_ai_key, model='gpt-3.5-turbo')
index = VectorstoreIndexCreator(embedding=embeddings).from_loaders([loader])

# 输入问题
question = "什么是配置中心?"

# 生成回答
answer = index.query(question)
print(answer)