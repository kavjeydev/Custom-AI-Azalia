from openai import OpenAI

client = OpenAI(api_key="sk-VMbVWoS5aF48-kDBDGc4yekmznV4YQgZ-wIj3sXZAOT3BlbkFJYVrwmEFTdfLnUufSctff_T6fp3G8lkdHh4iuT1zgYA")
completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": "write a haiku about ai"}
    ]
)

for chunk in completion:
    print(chunk)
