elif "sustainable" in user_query:
    recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
    print(f"CryptoBuddy: 🌱 {recommend} is the most sustainable! It’s eco-friendly and future-focused!")