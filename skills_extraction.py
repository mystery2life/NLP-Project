import spacy
from spacy.pipeline import EntityRuler
import jsonlines
import os
import requests

#spacy.cli.download("en_core_web_lg")
nlp = spacy.load("en_core_web_lg")


# Add entity ruler to the pipeline if not already added
if "entity_ruler" not in nlp.pipe_names:
    ruler = nlp.add_pipe("entity_ruler")
else:
    ruler = nlp.get_pipe("entity_ruler")

# URL to the JSONL file on GitHub
url = "https://raw.githubusercontent.com/mystery2life/NLP-Project/main/jz_skill_patterns.jsonl"

# Download the file content from GitHub
response = requests.get(url)
response.raise_for_status()  # Raises an HTTPError for bad responses

# Save the downloaded content to a temporary file
with open('temp_patterns.jsonl', 'wb') as f:
    f.write(response.content)

# Load patterns from the temporary file
ruler.from_disk('temp_patterns.jsonl')

# Print the updated pipeline component names
print("Pipeline components:", nlp.pipe_names)

def get_skills(text):
    doc = nlp(text)
    myset = []
    subset = []
    for ent in doc.ents:
        if ent.label_ == "SKILL":
            subset.append(ent.text)
    myset.append(subset)
    return subset


def unique_skills(x):
    return list(set(x))










