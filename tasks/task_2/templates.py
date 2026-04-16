from langchain.prompts import PromptTemplate

# Extraction and Evaluation Prompt
eval_template = """
You are an expert recruiter. Compare the Resume provided against the Job Description.
1. Extract Skills, Tools, and Experience.
2. Compare the Resume to the Job Description requirements.
3. Assign a Fit Score (0-100).
4. Provide a detailed explanation for the score.

Constraint: Do NOT assume skills not present in the resume[cite: 239].

Job Description: {job_description}
Resume: {resume_text}

Output format:
Score: [score]
Skills Extracted: [list]
Explanation: [reasoning]
"""

eval_prompt = PromptTemplate(
    input_variables=["job_description", "resume_text"],
    template=eval_template
)