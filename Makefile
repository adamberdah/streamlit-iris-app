.PHONY: install run test docker-build docker-run lock

install:
\tpython -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

run:
\texport PYTHONPATH=. && streamlit run app/main.py

test:
\texport PYTHONPATH=. && pytest -q

lock:
\tpip freeze > requirements.lock.txt

docker-build:
\tdocker build -t streamlit-iris-app:latest .

docker-run:
\tdocker run --rm -p 8501:8501 streamlit-iris-app:latest
