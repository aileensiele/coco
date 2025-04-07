import os
import openai

openai.api_key = os.environ['OPEN_API_KEY']
# Read PR diff from file instead of env variable
with open('pr_diff.txt', 'r') as f:
    diff = f.read()[:8000]  # Trim to avoid token limit


response = openai.ChatCompletion.create(
    model='gpt-4o',
    messages=[
        {'role': 'system', 'content': 'You are a helpful code assistant.'},
        {'role': 'user', 'content': f'Summarize this PR diff:\n{diff}'}
    ]
)

summary = response['choices'][0]['message']['content']
print(summary)

with open('summary.txt', 'w') as f:
    f.write(summary)
