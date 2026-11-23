# Mistral Chat Completion Example

A minimal Python example that calls the Mistral chat completion API with the
official `mistralai` SDK, using `mistral-small-latest`.

Based on [Chat completions](https://docs.mistral.ai/studio/conversations/chat-completion).

## Requirements

- Python 3.9+

## 1. Generate a Mistral API key

1. Sign in to [Studio](https://console.mistral.ai/).
2. Open [API keys](https://console.mistral.ai/api-keys).
3. Click **Create new key** and copy the generated key.

## 2. Set the environment variable

```bash
export MISTRAL_API_KEY="your-api-key"
```

Add the line to your `~/.bashrc` or `~/.zshrc` to make it persistent.

## 3. Install the SDK

```bash
pip install -r requirements.txt
```

This installs the official [Mistral Python SDK](https://pypi.org/project/mistralai/).

## 4. Run the example

```bash
python main.py
```

Expected output:

```
The best French painter is often considered to be Claude Monet.
```
