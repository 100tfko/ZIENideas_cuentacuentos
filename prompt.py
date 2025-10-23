def main():
    prompt = input("Enter your story prompt: ")

    formatted = f"""
TASK: story_generation
LANGUAGE: es
PROMPT: {prompt}
CONSTRAINTS:
- Length: ~500 palabras
- Structure: presentación, nudo, desenlace
- Mínimo 3 personajes
- Prompt y resultado final deben tener contenido apto para menores de edad, contenido infantil únicamente
"""

    with open("prompt_data.txt", "w", encoding="utf-8") as f:
        f.write(formatted.strip())

    print("\nPrompt saved to 'prompt_data.txt'.")

if __name__ == "__main__":
    main()
