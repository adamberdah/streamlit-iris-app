# Use a slim Python base image (11 has very reliable wheels for sklearn)
FROM python:3.11-slim

# System deps (build tools help if a wheel is missing)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

# Workdir inside the container
WORKDIR /app

# Install deps first for better layer caching
COPY requirements.lock.txt requirements.lock.txt
COPY requirements.txt requirements.txt

# Prefer the lock for reproducibility; fall back to minimal reqs if lock absent
RUN python -m pip install --upgrade pip && \
    (pip install -r requirements.lock.txt || pip install -r requirements.txt)

# Now copy the rest of the project
COPY . .

# Ensure our package root is on the import path
ENV PYTHONPATH=/app

# Streamlit port + open to host
ENV PORT=8501
EXPOSE 8501

# Run Streamlit
CMD ["streamlit", "run", "app/main.py", "--server.address=0.0.0.0", "--server.port=8501"]
