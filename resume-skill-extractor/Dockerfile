# Use official Python image
FROM python:3.10-slim

# Set environment variables
ENV VIRTUAL_ENV=/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Create working directory
WORKDIR /app

# Install virtualenv
RUN python -m venv $VIRTUAL_ENV && \
    apt-get update && apt-get install -y gcc && \
    pip install --upgrade pip

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
