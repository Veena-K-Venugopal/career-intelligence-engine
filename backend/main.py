from fastapi import FastAPI, HTTPException
from .agent import CareerInsight, analyze_career_fit  
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Career Intelligence Engine API")

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://0.0.0.0:3000",
]

# origins = ["*"]  # Allow all origins for development; restrict in production!

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

class AnalysisRequest(BaseModel):
    job_description: str
    resume_text: str

@app.post("/analyze", response_model=CareerInsight)
async def run_analysis(request: AnalysisRequest):
    try:
        result = analyze_career_fit(request.job_description, request.resume_text)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))