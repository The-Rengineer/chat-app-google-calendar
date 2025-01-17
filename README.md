# LangChain-Powered Google Calendar Chatbot
This app leverages **LangChain** to enable conversations with a bot about your personal **Google Calendar**.

---

## Prerequisites

- Python 3.10.16 was used for testing the app.
- Docker must be pre-installed to test the app with Docker.

---

## Common Setup Instructions

### **[LLM Setup]**
1. Rename `.env.sample` to `.env`.
2. Obtain an API key from your OpenAI account.
3. Add the API key to the `.env` file.

### **[Google Calendar Setup]**
1. Log in with your Google account and ensure access to your calendar is enabled.
2. Create Credentials and obtain a JSON file.
3. Place the JSON file in the root directory and rename `xxx.json` to `credentials.json`.

---

## How to Verify the App Works

```bash
# Method 1: Using Uvicorn

# Step 1: Create and activate a virtual environment
python -m venv venv

# If you are using macOS, use the following command:
source venv/bin/activate

# If you are using Windows, use the following command:
venv/Scripts/activate

# Step 2: Install the required dependencies
pip install -r requirements.txt

# Step 3: Open Terminal 1 and run:
uvicorn main:app --host 127.0.0.1 --port 8000 --reload

# Step 4: Open Terminal 2 and run:
curl -X POST "http://127.0.0.1:8000/chat" -H "Content-Type: application/json" -d '{"input": "Could you tell me my next schedule?"}'

# If you receive a response, the app is working correctly.

---

# Method 2: Using Docker

# Step 1: Build the Docker image from the root directory:
docker build -t fastapi-app .

# Step 2: Run the container in the background:
docker run --rm -d --name fastapi-container -p 8000:8000 fastapi-app

# Step 3: Verify the container is running:
docker container ls

# Step 4: Test the app with the following curl command:
curl -X POST "http://localhost:8000/chat" -H "Content-Type: application/json" -d '{"input": "Could you tell me my next schedule?"}'

# If you receive a response, the app is working correctly.