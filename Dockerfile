FROM python:3.9-slim

# Create a non-root user for security
RUN useradd -m secureuser
WORKDIR /app

# Copy files
COPY . .

# Install dependencies (if you had any, mostly for Bandit)
# RUN pip install flask (Not needed for this simple script)

# Switch to secure user
USER secureuser

# Open Port 80
EXPOSE 8080

# Run the server
CMD ["python", "hello.py"]
