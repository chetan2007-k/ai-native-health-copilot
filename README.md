# AI-Native Consumer Health Co-Pilot

This project explores what a consumer health experience looks like when
AI itself is the interface, not a feature.

Instead of listing ingredients or health scores, the system reasons on
the user’s behalf and explains trade-offs and uncertainty at the moment
a food decision is made.

---

## Why AI-Native?

- No filters or forms
- No ingredient dumping
- AI infers user intent and explains relevance
- Acts as a co-pilot, not a lookup tool
- Reduces cognitive load at decision time

---

## Tech Stack

- FastAPI (backend API)
- Local LLM via Ollama (model-agnostic)
- Minimal HTML/CSS/JS UI for clarity

---

## Demo Flow

User uncertainty → AI reasoning → Clear guidance

---

## How to Run (Local Demo)

1. Install Ollama: https://ollama.com  
2. Pull model:
ollama pull mistral

3. Run backend:
cd backend
pip install fastapi uvicorn requests
uvicorn main:app --reload

4. Open frontend:
frontend/index.html

---

## Note

This prototype focuses on experience design and reasoning quality rather
than dataset scale or deployment, in line with the hackathon scope.
