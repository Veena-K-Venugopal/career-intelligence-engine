import os
from pydantic import BaseModel, Field 
from typing import List, cast
from google import genai
from dotenv import load_dotenv

load_dotenv()  # Pulls GEMINI_API_KEY from .env file

# The "Child" - describes one single skill
class SkillInference(BaseModel):
    skill_name: str = Field(description="The name of the inferred skill.")
    explanation: str = Field(description="Why the AI believes the candidate has this skill based on the resume.")
    growth_field: str = Field(description="A specific way to showcase or explain this skill during an interview.")
    confidence: float = Field(ge=0, le=1, description="How certain the AI is about this inference (0.0 to 1.0).")

# The "Parent" - describes the whole analysis
class CareerInsight(BaseModel):
    # Attribute 1: The Business Pain
    business_pain: str = Field(
        description="The underlying reason this company is hiring (e.g., technical debt, scaling issues).")

    # Attribute 2: Implicit Skills 
    implicit_skills: List[SkillInference] = Field(
        description="A list of 3 skills inferred from the candidate's achievements.")

    # Attribute 3: The Match Score
    match_score: int = Field(
        ge=0, le=100,    # This 'ge' means Greater than or Equal to
        description="Overall fit score.")

def analyze_career_fit(job_description: str, resume_text: str)-> CareerInsight:
        # client = genai.Client(api_key=os.getenv("GENAI_API_KEY"))

        # # The System Prompt defines the "AI's Persona"
        # system_instruction = (
        #     "You are an expert Executive Recruiter. Your task is to look past the surface of a resume."
        #     "Find the 'Hidden Signals'-skills that candidate clearly has based on their achievements, "
        #     "even if they didn't list them. Also, identify the 'Business Pain' the company is trying to"
        #     "solve by hiring for this role."
        # )

        # response = client.models.generate_content(
        #     model="gemini-2.0-flash",
        #     contents=[
        #         f"Job Description: {job_description}",
        #         f"Candidate Resume: {resume_text}",
        #     ],
        #     config={
        #         "system_instruction": system_instruction,
        #         "response_mime_type": "application/json",
        #         "response_schema": CareerInsight, 
        #         }
        # )

    # return cast(CareerInsight, response.parsed)

    # RETURNING THIS INSTEAD TO KEEP DEVELOPING
    return CareerInsight(
        business_pain="Scaling technical infrastructure to handle AI workloads.",
        implicit_skills=[
            SkillInference(
                skill_name="Architectural Patterns",
                explanation="Inferred from FastAPI usage and LLM integration.",
                growth_field="System Design Interviews",
                confidence=0.95
            )
        ],
        match_score=88
    )

# if __name__ == "__main__":
#     # 1. Create a fake Job and Resume
#     test_job = "Hiring a Software Engineer to fix legacy code and scale our user base."
#     test_resume = "Experienced dev who migrated a 10-year-old monolith to microservices."

#     # 2. Call your function
#     print("Sending to Gemini...")
#     try:
#         result = analyze_career_fit(test_job, test_resume)
        
#         # 3. Print the result using .model_dump_json(indent=2)
#         # This is a Pydantic method that makes the output beautiful!
#         print(result.model_dump_json(indent=2))
#     except Exception as e:
#         print(f"Something went wrong: {e}")