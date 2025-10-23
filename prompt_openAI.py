import json
import urllib.request

API_KEY = "sk-your_api_key_here"

def main():
    prompt = input("Enter your story prompt: ")

    data = {
        "task": "story_generation",
        "language": "es",
        "prompt": prompt,
        "constraints": {
            "length": "≈500 palabras",
            "structure": ["presentación", "nudo", "desenlace"],
            "characters_min": 3,
            "contenido": "Prompt y resultado final deben tener contenido apto para menores de edad, contenido infantil únicamente"
        }
    }

    print("\n✅ Prompt prepared.")

    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "system",
                "content": (
                    "Eres un narrador que crea cuentos infantiles en español, "
                    "siguiendo las instrucciones dadas en el prompt."
                )
            },
            {
                "role": "user",
                "content": data["prompt"]
            }
        ],
        "temperature": 0.8,
        "max_tokens": 800
    }
