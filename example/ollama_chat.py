import ollama

response = ollama.chat(
    model = "gemma3:1b",
    messages =[
        {
            "role": "system",
            "content": "당신은 친절한 한국어 비서입니다."
        },
        {
            "role": "user",
            "content": "뭐하니?"
        },
    ],
)

print(response["message"]["content"])