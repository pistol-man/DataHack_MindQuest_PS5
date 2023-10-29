import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download NLTK data (if not already downloaded)
nltk.download('punkt')
nltk.download('stopwords')

# Load your dataset from "dataset.csv" (replace with your file path)
df = pd.read_csv('dataset.csv')

# Preprocess the text data
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    if isinstance(text, str):
        # Tokenize the text
        words = word_tokenize(text)
        # Remove stop words and non-alphabetic characters
        clean_words = [word.lower() for word in words if word.isalpha() and word.lower() not in stop_words]
        return ' '.join(clean_words)
    else:
        return ''  # Return an empty string if the input is not a valid string

# Apply text preprocessing to the 'Projects/Experience' and 'Skills' columns
df['Projects/Experience'] = df['Projects/Experience'].apply(preprocess_text)
df['Skills'] = df['Skills'].apply(preprocess_text)

# Create a TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Vectorize the text data
tfidf_matrix = vectorizer.fit_transform(df['Projects/Experience'] + ' ' + df['Skills'])

# Example client's resume (replace with the extracted content from the client's PDF resume)
client_resume = "Results-driven marketing manager with over 8 years of experience in developing and executing marketing strategies to drive brand awareness and revenue growth, skilled in leading cross-functional teams and leveraging data analytics for data-driven decision-making, with proven success in digital marketing, content strategy, and brand management, and a Master of Business Administration in Marketing."

# Preprocess the client's resume
client_resume = preprocess_text(client_resume)

# Vectorize the client's resume
client_resume_vector = vectorizer.transform([client_resume])

# Calculate cosine similarities between the client's resume and projects
cosine_similarities = cosine_similarity(client_resume_vector, tfidf_matrix)

# Recommend top N projects (e.g., top 3)
top_n_projects_indices = cosine_similarities.argsort()[0][::-1][:3]
recommended_projects = df.loc[top_n_projects_indices, ['Projects/Experience', 'Domain', 'Skills']]

# Print the recommended projects
for index, row in recommended_projects.iterrows():
    print(f"Project {index + 1}:")
    print(f"Projects/Experience: {row['Projects/Experience']}")
    print(f"Domain: {row['Domain']}")
    print(f"Skills: {row['Skills']}")
    print("\n")
print(recommended_projects)