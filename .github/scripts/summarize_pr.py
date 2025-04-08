import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPEN_API_KEY"])

# Read PR diff from file
with open('pr_diff.txt', 'r') as f:
    diff = f.read()[:8000]  # Truncate for token limit safety

# Enhanced prompt
prompt = f"""
You're a senior software engineer reviewing a pull request. The following is a git diff from a PR.

Please provide:
1. A concise summary of the key changes made in the PR.
2. Any observations on potential bugs, anti-patterns, or bad practices you notice.
3. Suggestions for improvement or refactoring, if applicable.

Here is the PR diff:
{diff}
"""

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful, detail-oriented code reviewer."},
        {"role": "user", "content": prompt}
    ]
)

summary = response.choices[0].message.content
print(summary)

with open("summary.txt", "w") as f:
    f.write(summary)
