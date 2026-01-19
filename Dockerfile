# 1. Base image: lightweight Python
FROM python:3.10-slim

# 2. Set working directory
WORKDIR /app

# 3. Copy requirements
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy all project files
COPY . .

# 6. Expose Streamlit default port
EXPOSE 8501

# 7. Command to run the app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
