from fastapi import FastAPI, Request, HTTPException

app = FastAPI(title="Honeypot API Tester")

API_KEY = "guvi123"   # demo key

@app.get("/")
def root():
    return {"message": "Unauthorized"}   # GUVI expected output

@app.post("/honeypot")
async def honeypot(request: Request):
    api_key = request.headers.get("x-api-key")

    if not api_key:
        return {"error": "API key missing"}

    if api_key != API_KEY:
        return {"error": "Invalid API key"}

    data = await request.json()
    return {
        "message": "Honeypot triggered",
        "data": data
    }
