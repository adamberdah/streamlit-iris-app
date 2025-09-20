# 📊 Streamlit IRIS App
A minimal Streamlit app for exploring the classic **Iris dataset**.  
This project demonstrates:
- Data loading, filtering, and simple visualizations
- A toy machine learning classifier
- A clean Streamlit interface
- Proper containerization with Docker
- Testing and CI integration with GitHub Actions
---

## 🚀 Features
- **Dataset**: Use the built-in Iris dataset or upload your own CSV.
- **Preview**: Display the first rows and dataset summary.
- **Filtering**: Select columns and apply simple row filters.
- **Visualization**: Quick scatter plots with matplotlib.
- **ML Demo**: Train a logistic regression classifier on Iris.
---

## 🛠️ Tech Stack
- [Streamlit](https://streamlit.io/) for the UI
- [Pandas](https://pandas.pydata.org/) for data handling
- [Matplotlib](https://matplotlib.org/) for plots
- [Scikit-learn](https://scikit-learn.org/) for ML
- [Pytest](https://docs.pytest.org/) for testing
- [Docker](https://www.docker.com/) for containerization
- GitHub Actions for CI
---

## 📂 Repository structure
streamlit-iris-app/
├─ app/ # Application code
├─ sample_data/ # Example Iris dataset
├─ tests/ # Unit tests
├─ .github/workflows/ # CI configuration
├─ requirements.txt # Minimal top-level dependencies
├─ requirements.lock.txt# Frozen exact versions for reproducibility
├─ Dockerfile # Container definition
├─ README.md # Project documentation
└─ .gitignore
---

## ⚙️ Setup and Installation
### 1. Clone the repo
```bash
git clone https://github.com/<your-username>/streamlit-iris-app.git
cd streamlit-iris-app