from ollama import chat


def ask_once(prompt: str):
    """Send a single prompt to the Ollama chat API and return the content string.

    Keeps the call minimal; raises any exception to the caller for handling.
    """
    response = chat(
        model="gemma3:1b",
        messages=[{"role": "user", "content": prompt}],
    )
    # The ollama client returns an object with .message.content in the example.
    return response.message.content


def conversation():
    print("Bucle de pregunta/respuesta. Escribe 'quit' o 'exit' para salir.")
    try:
        while True:
            prompt = input("Pregunta: ").strip()
            if not prompt:
                # ignore empty input and continue
                continue
            if prompt.lower() in ("quit", "exit"):
                print("Saliendo...")
                break
            try:
                answer = ask_once(prompt)
            except Exception as e:
                # Surface the error but continue the loop so the user can try again
                print(f"Error al llamar a la API: {e}")
                continue
            print("Respuesta:\n", answer)
    except KeyboardInterrupt:
        print("\nInterrumpido por el usuario. Saliendo...")


if __name__ == "__main__":
    conversation()
