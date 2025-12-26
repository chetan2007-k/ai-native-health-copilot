from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

# -------------------------------------------------
# FastAPI App
# -------------------------------------------------
app = FastAPI(
    title="AI-Native Consumer Health Co-Pilot",
    version="1.0.0"
)

# -------------------------------------------------
# CORS (required for frontend index.html)
# -------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins for local demo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------------------------
# Ollama Configuration
# -------------------------------------------------
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "mistral"

# -------------------------------------------------
# Request Schema
# -------------------------------------------------
class IngredientInput(BaseModel):
    ingredients: str

# -------------------------------------------------
# Analyze Endpoint
# -------------------------------------------------
@app.post("/analyze")
def analyze_ingredients(data: IngredientInput):
    try:
        prompt = f"""
You are an AI-native consumer health co-pilot helping a person
make a food decision at the moment it matters.

Your job is NOT to explain ingredients academically.
Your job is to THINK on behalf of the user.

First, silently infer what the user is most likely optimizing for:
- health vs convenience
- adult vs child consumption
- occasional vs regular use
- sensitivity to additives
- clean-label preference

Rules:
- Do NOT list ingredients
- Do NOT give medical advice
- Avoid absolute claims
- Be honest about uncertainty
- Reduce cognitive load

Respond in this structure:
1. What likely matters to the user
2. Why this product may or may not align
3. Trade-offs and uncertainty
4. Bottom-line guidance (clear, memorable, non-judgmental)

Ingredient list:
{data.ingredients}

Remember: this is a decision-time explanation, not a research summary.
"""

        payload = {
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(OLLAMA_URL, json=payload, timeout=120)

        if response.status_code != 200:
            raise RuntimeError(response.text)

        result = response.json()

        return {
            "analysis": result.get("response", "").strip()
        }

    except Exception as e:
        print("OLLAMA ERROR:", e)
        raise HTTPException(status_code=500, detail=str(e))
