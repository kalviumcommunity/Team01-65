FROM python:3.12-slim

# Prevent Python from creating .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Send Python output directly to terminal
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies first
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Streamlit's default port
EXPOSE 8501

# Start Streamlit
CMD ["streamlit", "run", "app/app.py", "--server.address=0.0.0.0", "--server.port=8501"]
