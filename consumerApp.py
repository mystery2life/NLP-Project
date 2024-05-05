import streamlit as st
import os

from skills_extraction import unique_skills
from skills_extraction import get_skills

from ResumeProcess import extract_text_from_pdf
from ResumeProcess import extract_Identity


# Initialize session_state to store job description
if "job_description" not in st.session_state:
    st.session_state.job_description = None

# Function to upload job description
def upload_job_description():
    st.subheader("Upload Job Description")
    job_description = st.text_area("Job Description")
    submit_button = st.button("Submit Job Description")
    if submit_button:
        st.session_state.job_description = job_description  # Store job description in session state
        st.success("Job Description submitted successfully.")
    return job_description



# Function to upload resumes
def upload_resumes():
    st.subheader("Upload Resumes")
    uploaded_files = st.file_uploader("Upload Resumes", accept_multiple_files=True)
    submit_button = st.button("Submit Resumes")
    if submit_button:
        st.success("Resumes submitted successfully.")
        return uploaded_files
    return None

jd_skills = None 

# Main function
def main():
    st.title("Resume Processing App")

    # Upload job description
    job_description = upload_job_description()

    if job_description:
            # Process job description and extract unique skills
            jd_skills = unique_skills(get_skills(job_description))
            
            # Display unique skills
            st.subheader("Unique Skills in Job Description")
            for skill in jd_skills:
                st.write(skill)

    
    
    # Upload resumes
    uploaded_files = upload_resumes()

    ranked_resumes = []
    if uploaded_files:
        for resume_path in uploaded_files:
            resume_text = extract_text_from_pdf(resume_path)
            emails, names = extract_Identity(resume_text)
            resume_skills = unique_skills(get_skills(resume_text.lower()))

            score = 0
            for x in jd_skills:
                if x in resume_skills:
                    score += 1
            req_skills_len = len(jd_skills)
            match = round(score / req_skills_len * 100, 1)
            # resume_vector = tfidf_vectorizer.transform([resume_text])
            # similarity = cosine_similarity(job_desc_vector, resume_vector)[0][0]
            ranked_resumes.append((names, emails, match))

        s = 0
        missing_skills = []
        for skill in jd_skills:
            if skill in resume_skills:
                s += 1
            else:
                missing_skills.append(skill)
    

        # Display ranked resumes
        st.subheader("Your Resumes match score")
        for i, (names, emails, match) in enumerate(ranked_resumes):
            st.write(f"Skill Match Score: {match}%")
            st.write("--------------")  
        
        # Display the missing skills
        st.subheader("Missing Skills")
        if missing_skills:
            for skill in missing_skills:
                st.write(skill)
        else:
            st.write("No missing skills. Congratulations!")


if __name__ == "__main__":
    main()


    
