import ollama

response = ollama.chat(
    model = "gemma3:1b",
    options = {"temperature": 0, "top_p": 1},
    messages =[
        {
            "role": "system",
            "content": "당신은 친절한 한국어 비서입니다."
        },
        {
            "role": "user",
            "content": "파이썬에서 리스트를 정렬하는 법을 하나만 알려줘"
        },
    ],
)

print(response["message"]["content"])