from crypto_data import crypto_db

def crypto_chatbot():
    print("CryptoBuddy 🤖💰: Hello! Ask me about the best crypto for long-term, security, low risk, or sustainability.")

    while True:
        user_query = input("You: ").lower()

        if "exit" in user_query or "quit" in user_query:
            print("CryptoBuddy: 👋 Bye for now! Stay crypto smart.")
            break

        elif "long-term" in user_query or "investment" in user_query:
            recommend = max(crypto_db, key=lambda x: crypto_db[x]["long_term_score"])
            print(f"CryptoBuddy: 📈 {recommend} is great for long-term holding!")

        elif "secure" in user_query or "security" in user_query:
            recommend = max(crypto_db, key=lambda x: crypto_db[x]["security_score"])
            print(f"CryptoBuddy: 🔐 {recommend} is one of the most secure choices.")

        elif "low risk" in user_query or "safe" in user_query:
            recommend = max(crypto_db, key=lambda x: crypto_db[x]["risk_score"])
            print(f"CryptoBuddy: 🛡️ {recommend} has the lowest risk in our database.")

        elif "sustainable" in user_query or "eco" in user_query:
            recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
            print(f"CryptoBuddy: 🌱 {recommend} is the most sustainable! It’s eco-friendly and future-focused!")

        else:
            print("CryptoBuddy: 🤔 I'm not sure about that. Try asking about long-term, secure, low risk, or sustainable cryptos.")

if __name__ == "__main__":
    crypto_chatbot()