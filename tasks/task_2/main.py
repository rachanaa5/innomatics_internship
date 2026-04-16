from chains.evaluator import get_eval_chain

# 1. Inputs [cite: 191-197]
job_desc = "Data Scientist: Requires Python, SQL, and 3+ years Machine Learning experience."

resumes = {
    "Strong": "Expert Data Scientist with 5 years experience in Python, SQL, and Deep Learning.",
    "Average": "Software Engineer with Python skills and 1 year of basic data analysis.",
    "Weak": "Graphic Designer with experience in Photoshop and creative branding."
}

# 2. Execution
chain = get_eval_chain()

for candidate, resume in resumes.items():
    print(f"--- Evaluating {candidate} Candidate ---")
    # Using .invoke() as required 
    response = chain.invoke({
        "job_description": job_desc, 
        "resume_text": resume
    })
    print(response.content)