# 📊 Streamlit IRIS App

[![CI](https://github.com/adamberdah/streamlit-iris-app/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/adamberdah/streamlit-iris-app/actions/workflows/ci.yml)

A minimal, well-engineered **Streamlit** application to explore the classic **Iris** dataset.  
Focus is on **clean tooling**: package layout, tests, CI, and **Docker** containerization.

---

## ✨ Features

- **Data sources**
  - Built-in sample: `sample_data/iris.csv`
  - Upload your own CSV via sidebar
- **Explore**
  - Preview head, pick columns, sanity filters
- **Visualize**
  - Quick scatter plot (matplotlib)
- **Codebase**
  - Small, testable modules: `data.py`, `filters.py`, `viz.py`
- **Tooling**
  - `pytest` unit tests for data loading & filtering
  - GitHub Actions CI
  - Reproducible Docker image (optional publish to Docker Hub)

---

## 🧠 Why this repo looks like this (grading-oriented)

- **Separation of concerns** → simple modules are easy to test.
- **Package layout** (`app/` with `__init__.py`) → reliable imports locally, in CI, and in Docker.
- **Reproducibility** → `requirements.lock.txt` (frozen versions) + Docker image.
- **Automation** → CI runs tests on every push; optional Docker build/push job.

---

## 🗂️ Repository structure

streamlit-iris-app/
├─ app/ # App package (importable as 'app')
│ ├─ init.py
│ ├─ main.py # Streamlit entrypoint
│ ├─ data.py # load_data()
│ ├─ filters.py # apply_filters()
│ └─ viz.py # quick_plot()
├─ sample_data/
│ └─ iris.csv # local copy of Iris dataset
├─ tests/
│ ├─ test_data.py
│ ├─ test_filters.py
│ └─ test_viz.py
├─ .github/workflows/
│ └─ ci.yml # GitHub Actions: pytest (+ optional Docker build)
├─ requirements.txt # top-level deps (flexible)
├─ requirements.lock.txt # frozen exact versions (reproducible)
├─ Dockerfile # container definition
├─ .dockerignore # reduce image context size
├─ pyproject.toml # pytest config (adds project root to PYTHONPATH)
├─ .gitignore
└─ README.md


---

## 🚀 Quickstart (local)
> **Why:** local run is fastest for development.

### 1) Create & activate a virtualenv
```bash
python3 -m venv .venv
source .venv/bin/activate

2) Install dependencies
Flexible (dev):
pip install -r requirements.txt

Reproducible (exact):
pip install -r requirements.lock.txt

3) Run Streamlit
# Ensure the project root is on the import path:
export PYTHONPATH=.
streamlit run app/main.py
# then open http://localhost:8501

If you use Conda and see both (base) and (.venv) in your prompt, ensure you install/launch with the venv (or set PYTHONPATH=. as above).

🧪 Tests
Why: demonstrates correctness of data I/O and filtering logic.
# optional but recommended
export PYTHONPATH=.
pytest -q

test_data.py → sample dataset loads, non-empty, has target column
test_filters.py → column selection and min-rows rule behave as expected
test_viz.py → plotting helper returns a matplotlib figure

🐳 Docker (build & run)
Why: run your app without any local Python setup.

Build
docker build -t streamlit-iris-app:latest .

Run
docker run --rm -p 8501:8501 streamlit-iris-app:latest
# open http://localhost:8501

Notes
Dockerfile sets PYTHONPATH=/app so imports like from app.data ... work in-container.
The image installs from requirements.lock.txt if present (reproducible builds).

⬇️ Pull prebuilt image (optional)

If you publish to Docker Hub:
docker pull adamberdah/streamlit-iris-app:latest
docker run --rm -p 8501:8501 adamberdah/streamlit-iris-app:latest

Docker Hub page (replace with your namespace):
https://hub.docker.com/r/adamberdah/streamlit-iris-app

🔄 Continuous Integration (GitHub Actions)
Why: shows process maturity; tests run on every push/PR.
This repo includes .github/workflows/ci.yml which:
- checks out code
- sets up Python
- installs dependencies (requirements.lock.txt if present)
- runs pytest -q
Optional: Add a Docker job to build & push the image on main.

Set up Docker publishing (optional)
In your GitHub repo: Settings → Secrets and variables → Actions
DOCKERHUB_USERNAME → your Docker Hub username
DOCKERHUB_TOKEN → a Docker Hub access token (Docker Hub → Account Settings → Security)
Append this job to ci.yml:
  docker:
    name: Build & Push Docker image
    needs: test
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: docker/setup-qemu-action@v3
      - uses: docker/setup-buildx-action@v3
      - name: Login to Docker Hub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}
      - name: Build & push
        uses: docker/build-push-action@v6
        with:
          context: .
          push: true
          tags: ${{ secrets.DOCKERHUB_USERNAME }}/streamlit-iris-app:latest

Badge

📦 Dependencies & Reproducibility
requirements.txt → concise, top-level deps (developer-friendly)
requirements.lock.txt → pinned versions (reproducible for Docker/CI)

To refresh the lock file after upgrading:
pip install -r requirements.txt
pip freeze > requirements.lock.txt

🧰 Troubleshooting
ModuleNotFoundError: No module named 'app' (local)
Ensure you run from the repo root and export PYTHONPATH=.

Confirm app/__init__.py exists.
In Docker this is handled via ENV PYTHONPATH=/app.

Conda vs venv confusion
If (base) appears, install/run using .venv explicitly or disable conda auto-activation:
conda config --set auto_activate_base false
Streamlit “Watchdog” hint

Optional performance improvement:
pip install watchdog
Port already in use

Run on a different host port:
docker run --rm -p 8502:8501 streamlit-iris-app:latest

## 📝 Final Submission Checklist

### ✅ Required (for grading)
- Public GitHub repo link in submission (example:  
  `https://github.com/adamberdah/streamlit-iris-app`)
- `README.md` with:
  - Local run instructions (venv + `streamlit run`)
  - Tests instructions (`pytest`)
  - Docker build/run instructions
  - (If using) Docker Hub pull/run instructions
- Unit tests implemented (`pytest`) and **passing in CI**
- GitHub Actions CI workflow (`.github/workflows/ci.yml`) runs tests automatically
- `Dockerfile` builds and runs locally
- (If requested in assignment) Docker image pushed to a public registry (Docker Hub)  
  Example pull:  
  ```bash
  docker pull adamberdah/streamlit-iris-app:latest
