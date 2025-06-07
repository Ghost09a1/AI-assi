import os
try:
    import openai
except ImportError:  # Allow running without the openai package
    openai = None
from transformers import pipeline

README_FILE = 'README.md'
_local_pipe = None

# Load README content to provide context
def load_readme():
    try:
        with open(README_FILE, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return ''


def chat_with_local_model(prompt):
    """Fallback to a local transformers model if no API key is provided."""
    global _local_pipe
    if _local_pipe is None:
        _local_pipe = pipeline("text-generation", model="gpt2")
    result = _local_pipe(prompt, max_length=100, num_return_sequences=1)
    return result[0]['generated_text']


def chat_with_model(prompt):
    """Send the prompt either to OpenAI or a local model."""
    openai_api_key = os.getenv('OPENAI_API_KEY')
    if openai and openai_api_key:
        openai.api_key = openai_api_key
    else:
        # Fallback to local model when OpenAI credentials are unavailable
        return chat_with_local_model(prompt)

    messages = [
        {
            'role': 'system',
            'content': 'You are a helpful assistant. Use the project README as context.'
        },
        {
            'role': 'system',
            'content': load_readme()
        },
        {
            'role': 'user',
            'content': prompt
        }
    ]

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages,
        temperature=0.7,
    )

    return response.choices[0].message['content']


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Simple CLI AI agent')
    parser.add_argument('prompt', nargs='*', help='Prompt to send to the agent')
    args = parser.parse_args()
    prompt = ' '.join(args.prompt) if args.prompt else input('Prompt: ')
    result = chat_with_model(prompt)
    print(result)


if __name__ == '__main__':
    main()
