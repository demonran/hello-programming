import re
from random import random

import gensim
import numpy as np

# 定义回答集合
responses = {
    "你好": ["你好！", "嗨！", "你好，有什么我可以帮助你的吗？"],
    "天气": ["今天天气晴朗，温度适宜。", "天气状况良好，气温适中。"],
    "再见": ["再见！", "下次见！", "祝你有美好的一天！"],
    # "默认回答": ["抱歉，我无法理解你的问题。", "我还不够智能，无法回答你的问题。"]
}

def preprocess_text(text):
    # 去除标点符号和多余的空格
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    # 转换为小写
    text = text.lower()
    return text


def get_response(message, model):
    similarities = []
    for response in responses:
        response_words = preprocess_text(response).split()
        print(response_words)
        similarity = model.wv.similarity(message, response)
        similarities.append(similarity)
    print(similarities)
    index = np.argmax(similarities)
    max_similarity = similarities[index]
    if max_similarity > 0:
        return responses[list(responses.keys())[index]]

    return responses["默认回答"]


if __name__ == '__main__':
    model = gensim.models.Word2Vec.load('./text.txt')
    while True:
        user_input = input("用户: ")
        response = get_response(user_input, model)
        print("机器：" + response[0])
