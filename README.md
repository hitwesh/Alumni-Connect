# Alumni Connect Platform

A modern web platform connecting students with alumni mentors using AI-powered recommendations.

![Alumni Connect](frontend/static/img/hero-illustration.svg)

## 🌟 Features

- **Smart Mentor Matching**: AI-powered recommendation system matches students with alumni mentors based on skills and interests
- **Alumni Directory**: Searchable directory of alumni profiles with skills and experience
- **User Management**: Secure registration and login system for students and alumni
- **Dashboard**: Personalized dashboard showing mentor recommendations and profile stats
- **Responsive Design**: Modern, mobile-friendly interface built with Bootstrap 5

## 🚀 Tech Stack

- **Backend**: Python/Flask
- **Frontend**: HTML5, Bootstrap 5, JavaScript
- **Database**: CSV-based data storage
- **AI/ML**: scikit-learn for mentor recommendations
- **UI Libraries**: 
  - Font Awesome for icons
  - Animate.css for animations
  - Bootstrap Icons
  - Google Fonts (Poppins)

## 📋 Prerequisites

- Python 3.x
- pip (Python package manager)

## ⚙️ Installation

1. Clone the repository:
```bash
git clone https://github.com/hitwesh/Alumni-Connect.git
cd InnovationProject
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Unix/MacOS:
source venv/bin/activate
```

3. Install required packages:
```bash
pip install flask pandas scikit-learn
```

4. Run the application:
```bash
cd backend
python -m flask --app app run
```

5. Open your browser and navigate to:
```
http://127.0.0.1:5000
```

## 📁 Project Structure

```
InnovationProject/
├── backend/           # Application server code
│   ├── app.py        # Main Flask application
│   └── model.py      # AI recommendation model
├── frontend/
│   ├── static/       # Static assets
│   │   ├── css/     # Stylesheets
│   │   └── img/     # Images
│   └── templates/    # HTML templates
├── database/         # Data storage
│   ├── users.csv    # User accounts
│   └── alumni_dataset.csv  # Alumni profiles
└── backups/         # Backup storage
```

## 🚦 Usage

1. **Register an Account**:
   - Choose between Student or Alumni role
   - Fill in your details
   - For alumni, add your skills and experience

2. **Find Mentors**:
   - Log in to your account
   - Navigate to "Find Mentor"
   - Enter your interests/skills
   - Get AI-powered mentor recommendations

3. **Browse Alumni**:
   - View the alumni directory
   - Filter by department or batch
   - See detailed skill sets

## 🔒 Security Features

- Secure password handling
- Session-based authentication
- Form validation and sanitization
- CSRF protection via Flask-WTF
- Defensive CSV data handling

## 💡 AI Recommendation System

The platform uses:
- CountVectorizer for text processing
- Cosine similarity for mentor matching
- Skills-based recommendation algorithm
- Batch processing for efficient matching

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -m 'Add YourFeature'`
4. Push to the branch: `git push origin feature/YourFeature`
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

Props to Hitesh Kumar Roy, Samik Sarkar, Riya Ghosh for managing, directing, and Implementing this project.
Special thanks to Hitesh Kumar Roy for deployment of this project on Render
Special thanks to Samik Sarkar and Hitesh Kumar Roy for testing and bug fixing.

---

