import os
import sys

from mistralai.client import Mistral

MODEL = "mistral-small-latest"


def main() -> None:
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        sys.exit(
            "MISTRAL_API_KEY is not set. Export it first: export MISTRAL_API_KEY='your-api-key'"
        )

    client = Mistral(api_key=api_key)

    chat_response = client.chat.complete(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": "Who is the best French painter? Answer in one short sentence.",
            },
        ],
    )

    if chat_response.choices:
        print(chat_response.choices[0].message.content)


if __name__ == "__main__":
    main()
