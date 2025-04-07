import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPEN_API_KEY"])

# Read PR diff from file
with open('pr_diff.txt', 'r') as f:
    diff = f.read()[:8000]

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful code assistant."},
        {"role": "user", "content": f"Summarize this PR diff:\n{diff}"}
    ]
)

summary = response.choices[0].message.content
print(summary)

with open('summary.txt', 'w') as f:
    f.write(summary)
