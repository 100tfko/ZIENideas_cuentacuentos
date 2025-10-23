import json
import urllib.request

# 🔑 Replace with your free Hugging Face access token from https://huggingface.co/settings/tokens
HF_TOKEN = "YourkeyHERE"

def main():
    prompt = input("Enter your story prompt (in Spanish): ")

    # 🧠 Instruction for the model
    system_prompt = (
        "Eres un narrador que crea cuentos infantiles en español. "
        "Sigue la estructura clásica: presentación, nudo y desenlace. "
        "Crea una historia de unas 500 palabras, apta para menores de edad."
    )

    full_prompt = f"{system_prompt}\n\nTema: {prompt}\n\nHistoria:"

    # 🌐 Hugging Face Inference API endpoint for the Mistral 7B model
    url = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"

    headers = {
        "Authorization": f"Bearer {HF_TOKEN}",
        "Content-Type": "application/json"
    }

    # 📦 Prepare the payload
    body = {
        "inputs": full_prompt,
        "parameters": {
            "max_new_tokens": 600,
            "temperature": 0.8
        }
    }

    # 📤 Prepare the request
    req = urllib.request.Request(url, data=json.dumps(body).encode('utf-8'), headers=headers, method='POST')

    print("\n✅ Sending request... please wait (it might take a few seconds).")

    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode())

            # Hugging Face responses return a list with generated_text
            if isinstance(result, list) and "generated_text" in result[0]:
                story = result[0]["generated_text"]
                print("\n📝 Generated Story:\n")
                print(story)

                with open("story_output.txt", "w", encoding="utf-8") as f:
                    f.write(story)
                print("\n✅ Story saved to 'story_output.txt'.")
            else:
                print("\n⚠️ Unexpected response format:")
                print(json.dumps(result, indent=2, ensure_ascii=False))

    except urllib.error.HTTPError as e:
        print(f"\n⚠️ HTTP Error {e.code}: {e.reason}")
        if e.code == 503:
            print("💤 The model might be loading — try again in 30 seconds.")
    except Exception as e:
        print(f"\n⚠️ General error: {e}")

if __name__ == "__main__":
    main()
