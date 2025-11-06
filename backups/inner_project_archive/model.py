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
    corpus = alumni_data['skills'].astype(str).tolist() + [user_skills]
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(corpus)
    cosine_sim = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1]).flatten()
    top_indices = cosine_sim.argsort()[::-1][:top_n]
    recommendations = []
    for idx in top_indices:
        mentor = alumni_data.iloc[idx]
        recommendations.append({
            'name': mentor['name'],
            'email': mentor['email'],
            'batch': mentor['batch'],
            'department': mentor['department'],
            'skills': mentor['skills']
        })

    return recommendations

if __name__ == "__main__":
    data = load_alumni_data("alumni_dataset.csv")
    if not data.empty:
        mentors = recommend_mentors("Python, Machine Learning, AI", data="alumni_dataset.csv", top_n=3)
        for m in mentors:
            print(f"{m['name']} ({m['email']}) - Skills: {m['skills']}")
    else:
        print("No alumni data found.")