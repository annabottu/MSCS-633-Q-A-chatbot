from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer


def create_and_train_bot(bot_name: str = "SchoolChatBot") -> ChatBot:
    bot = ChatBot(bot_name)

    # Train on built-in English corpus
    corpus_trainer = ChatterBotCorpusTrainer(bot)
    corpus_trainer.train("chatterbot.corpus.english")

    # Custom training
    custom_trainer = ListTrainer(bot)

    custom_trainer.train([
        "Hello",
        "Hi there! How can I help you today?"
    ])

    custom_trainer.train([
        "Hey",
        "Hello! What's up?"
    ])

    custom_trainer.train([
        "Good morning",
        "Good morning! How are you doing today?"
    ])

    custom_trainer.train([
        "How are you?",
        "I'm doing well, thank you! How are you?"
    ])

    custom_trainer.train([
        "I'm good",
        "That's great to hear!"
    ])

    custom_trainer.train([
        "What is your favorite color?",
        "blue!"
    ])

    custom_trainer.train([
        "My favorite color is blue",
        "Nice!"
    ])

    custom_trainer.train([
        "What are you doing?",
        "Just chatting with you! What about you?"
    ])

    custom_trainer.train([
        "Do you like animals?",
        "I love animals!"
    ])

    custom_trainer.train([
        "What is 2+2?",
        "2+2 is 4."
    ])

    custom_trainer.train([
        "What is 10 plus 5?",
        "10 plus 5 is 15."
    ])

    custom_trainer.train([
        "bye",
        "Goodbye! Talk to you later!"
    ])

    custom_trainer.train([
        "see you later",
        "See you later! Have a good day!"
    ])

    return bot

def chat_loop(bot: ChatBot) -> None:
    print("Chatbot is ready to talk!")
    print("Type 'quit', 'exit', or 'bye' to end the conversation.\n")

    while True:
        user_input = input("user: ").strip()

        if user_input.lower() in ("quit", "exit", "bye"):
            print("bot: Goodbye! Have a great day!")
            break

        if not user_input:
            print("bot: Please type something so I can respond.")
            continue

        bot_response = bot.get_response(user_input)

        print(f"bot: {bot_response}")


def main() -> None:
    
    # Create and train the chatbot
    chatbot = create_and_train_bot()

    # Start chatting with the user in the terminal
    chat_loop(chatbot)


if __name__ == "__main__":
    main()


