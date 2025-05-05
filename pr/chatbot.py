def chatbot():
    print("Welcome to ShopEase Customer Support!")
    print("How can I assist you today?")
    print("Type 'bye' to end the chat.\n")

    while True:
        user_input = input("You: ").lower()

        if "order" in user_input:
            print("Bot: You can track your order in the 'My Orders' section of your account.")
        elif "refund" in user_input or "return" in user_input:
            print("Bot: To request a refund, go to 'My Orders' and click on 'Return or Replace'.")
        elif "product" in user_input or "item" in user_input:
            print("Bot: Could you please specify the product name?")
        elif "hello" in user_input or "hi" in user_input:
            print("Bot: Hello! How can I help you today?")
        elif "thanks" in user_input or "thank you" in user_input:
            print("Bot: You're welcome! 😊")
        elif "bye" in user_input:
            print("Bot: Thank you for contacting ShopEase. Have a great day!")
            break
        else:
            print("Bot: I'm sorry, I didn't understand that. Could you please rephrase?")

if __name__ == "__main__":
    chatbot()
