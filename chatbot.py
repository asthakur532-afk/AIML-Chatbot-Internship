import re

RESPONSES = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi! Ask me anything about AI/ML.",
    "ai": "Artificial Intelligence is the simulation of human intelligence in machines.",
    "machine learning": "Machine Learning allows computers to learn patterns from data.",
    "python": "Python is a high-level language widely used in AI and ML.",
    "bye": "Goodbye! Have a nice day."
}

def normalize(text):
    text = text.lower().strip()
    return re.sub(r"[^a-z0-9\s]", "", text)

def get_response(user_text):
    text = normalize(user_text)

    if text in ("quit", "exit", "bye"):
        return RESPONSES["bye"], True

    for key, response in sorted(RESPONSES.items(), key=lambda x: len(x[0]), reverse=True):
        if key in text:
            return response, False

    return "Sorry, I am still learning. Please try another question.", False


def main():
    print("AIML Chatbot started successfully.")
    print("Type 'bye' to exit.")

    while True:
        user = input("You: ")
        response, stop = get_response(user)

        print("Bot:", response)

        if stop:
            break


if __name__ == "__main__":
    main()