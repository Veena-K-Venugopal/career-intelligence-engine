from fastapi import FastAPI, HTTPException
from agent import CareerInsight, analyze_career_fit  
from pydantic import BaseModel

app = FastAPI(title="Career Intelligence Engine API")

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