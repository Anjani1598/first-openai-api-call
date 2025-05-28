from openai import OpenAI

import os
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
  api_key = api_key,
)


user_input  = input("Enter your input: ")
completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": user_input},
    {"role": "system", "content": "You are a helpful assistant."}
  ]
)


print("AI Message :",completion.choices[0].message.content)
print("token usage: ", completion.usage.total_tokens)

