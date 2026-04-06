![Build Status](https://github.com/[your-username]/Wingman-2.0/actions/workflows/main.yml/badge.svg)
![Docker Hub](https://img.shields.io/docker/pulls/walkedal006/rexburg-wingman)

# Rexburg Wingman 2.0 🚀
**A Data-Driven Date Planning Application**

## 🛠️ Tech Stack
- **Backend:** FastAPI (Python)
- **Database:** SQLite with SQLAlchemy ORM
- **DevOps:** Docker, GitHub Actions (CI/CD), Terraform (IaC)

## 📊 Statistical Success Model
This app features a custom Logistic Regression model to predict the likelihood of a "Yes" for a date invite.
- **Interests ($b_1$):** 0.322
- **Prep Hours ($b_2$):** 0.111
- **Notice Days ($b_3$):** 0.344
- **Group Size ($b_4$):** -0.389 (Negative coefficient reflects lower 1-on-1 intimacy in large groups)

## 🐳 How to Run (Docker)
1. Build: `docker build -t rexburg-wingman .`
2. Run: `docker run -p 8000:8000 rexburg-wingman`
3. Access at: `http://localhost:8000/static/index.html`
