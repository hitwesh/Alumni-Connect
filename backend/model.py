import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_alumni_data(csv_path):  
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        print(f"[Error] File not found: {csv_path}")
        return pd.DataFrame(columns=['name', 'email', 'batch', 'department', 'skills'])

    df.fillna("", inplace=True)
    return df

def recommend_mentors(user_skills, alumni_data, top_n=5): 
    if alumni_data.empty:
        return []  
    
    # Corpus should only contain the documents to learn the vocabulary from
    corpus = alumni_data['skills'].astype(str).tolist()
    vectorizer = TfidfVectorizer(
        analyzer='char_wb', # Analyze characters within word boundaries for typo tolerance
        ngram_range=(2, 5), # Use n-grams of length 2 to 5
        min_df=1 # Include words that appear in at least one document
    )

    # Fit on the alumni skills, then transform both alumni and user skills
    alumni_tfidf_matrix = vectorizer.fit_transform(corpus)
    user_tfidf_vector = vectorizer.transform([user_skills])

    cosine_sim = cosine_similarity(user_tfidf_vector, alumni_tfidf_matrix).flatten()
    top_indices = cosine_sim.argsort()[::-1][:top_n]
    recommendations = []
    for idx in top_indices:
        score = cosine_sim[idx]
        mentor = alumni_data.iloc[idx]
        recommendations.append({
            'name': mentor['name'],
            'email': mentor['email'],
            'batch': mentor['batch'],
            'department': mentor['department'],
            'skills': mentor['skills'],
            'score': score
        })

    return recommendations

if __name__ == "__main__":
    data = load_alumni_data("../database/alumni_dataset.csv")
    if not data.empty:
        mentors = recommend_mentors("Python, Machine Learning, AI", alumni_data=data, top_n=3)
        for m in mentors:
            print(f"{m['name']} ({m['email']}) - Skills: {m['skills']}")
    else:
        print("No alumni data found.")
