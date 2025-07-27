from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="CryptoBuddy AI",
    description="Your first AI-powered crypto sidekick 🪙🤖",
    version="1.0.0"
)

# Allow frontend (if hosted elsewhere) to access this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict to your frontend URL later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Basic test route
@app.get("/")
def home():
    return {"message": "CryptoBuddy API is live and working! 🔥"}

# Sample endpoint for crypto advice
@app.get("/advise/{crypto_name}")
def advise(crypto_name: str):
    # Simple placeholder logic for demo
    advice = {
        "bitcoin": "Consider holding long-term. High volatility.",
        "ethereum": "Great for smart contracts. Keep an eye on gas fees.",
        "dogecoin": "High risk, high meme. Be cautious.",
    }
    return {
        "crypto": crypto_name,
        "advice": advice.get(crypto_name.lower(), "No specific advice yet. Research well!")
    }
