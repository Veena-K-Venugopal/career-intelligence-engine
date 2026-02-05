from pydantic import BaseModel, Field 
from typing import List

# The "Child" - describes one single skill
class SkillInference(BaseModel):
    skill_name: str = Field(description="The name of the inferred skill.")
    explanation: str = Field(description="Why the AI believes the candidate /" \
    "has this skill based on the resume.")
    growth_field: str = Field(description="A specific way to showcase or /" \
    "explain this skill during an interview.")
    confidence: float = Field(ge=0, le=1, description="How certain the AI is /" \
    "about this inference (0.0 to 1.0).")

# The "Parent" - describes the whole analysis
class CareerInsight(BaseModel):
    # Attribute 1: The Business Pain
    business_pain: str = Field(
        description="The underlying reason this company is hiring /" \
    "(e.g., technical debt, scaling issues).")

    # Attribute 2: Implicit Skills 
    implicit_skills: List[SkillInference] = Field(
        description="A list of 3 skills inferred from the candidate's /" \
        "achievements ")

    # Attribute 3: The Match Score
    match_score: int = Field(
        ge=0, le=100,    # This 'ge' means Greater than or Equal to
        description="Overall fit score.")

def analyze_career_fit(job_description: str, resume_text: str):
    pass