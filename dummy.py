# List of resume PDF file paths
resume_paths = ["resume1.pdf", "resume2.pdf", "resume3.pdf"]  

# # Extract text from PDFs
# def extract_text_from_pdf(pdf_path):
#     with open(pdf_path, "rb") as pdf_file:
#         pdf_reader = PyPDF2.PdfReader(pdf_file)
#         text = ""
#         for page in pdf_reader.pages:
#             text += page.extract_text()
#         return text



# req_skills = ["python", "machine learning"]

# # Rank resumes based on similarity
# ranked_resumes = []
# for resume_path in resume_paths:
#     resume_text = extract_text_from_pdf(resume_path)
#     emails, names = extract_Identity(resume_text)
#     resume_skills = unique_skills(get_skills(resume_text.lower()))

#     score = 0
#     for x in req_skills:
#         if x in resume_skills:
#             score += 1
#     req_skills_len = len(req_skills)
#     match = round(score / req_skills_len * 100, 1)
#     # resume_vector = tfidf_vectorizer.transform([resume_text])
#     # similarity = cosine_similarity(job_desc_vector, resume_vector)[0][0]
#     ranked_resumes.append((names, emails, match))

# print(ranked_resumes)