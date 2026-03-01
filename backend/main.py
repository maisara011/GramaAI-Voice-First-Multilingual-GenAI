from fastapi import FastAPI

app = FastAPI(title="GramaAI Backend API")

@app.get("/")
def root():
    return {"message": "Welcome to GramaAI - Voice First Multilingual Generative AI Platform"}

@app.get("/health")
def health_check():
    return {"status": "API is running successfully"}
