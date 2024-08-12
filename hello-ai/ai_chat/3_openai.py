from openai import OpenAI

client = OpenAI(
    base_url='https://free.gpt.ge/v1/'
)



def generate_text(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": 'You are a helpful assistant.'},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        max_tokens=256,
        stop=["\n\n"],
    )
    return response.choices[0].message.content.strip()



if __name__ == '__main__':
    prompt = "请告诉我Python中的列表和元组有什么区别？"
    generated_text = generate_text(prompt)
    print(generated_text)


