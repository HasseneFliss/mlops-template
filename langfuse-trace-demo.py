from langfuse import Langfuse
from langfuse.decorators import observe
from langfuse.openai import openai  # OpenAI integration
import os

import os

os.environ["LANGFUSE_PUBLIC_KEY"] = "pk-lf-5134505d-7094-41ad-882d-9dd82a448f4f"
os.environ["LANGFUSE_SECRET_KEY"] = "sk-lf-cfa66944-1a8a-4893-812b-8b023b0b7e45"
os.environ["LANGFUSE_HOST"] = "https://langfuse.dev-avaxialabs.com"


os.environ['OPENAI_API_KEY'] = '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'

@observe()
def story():
    return openai.chat.completions.create(
        model="gpt-3.5-turbo",
        max_tokens=100,
        messages=[
            {"role": "system", "content": "You are a great storyteller."},
            {"role": "user", "content": "Once upon a time in a galaxy far, far away..."}
        ],
    ).choices[0].message.content

@observe()
def main():
    return story()

if __name__ == "__main__":
    main()
