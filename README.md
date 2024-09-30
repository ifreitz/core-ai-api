# core-ai-api

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/core-ai-api.git
   cd core-ai-api
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory and add the necessary environment variables, for example:
   ```
   GEMINI_API_KEY=your_api_key_here
   DEBUG=True
   ```

## Running Locally

1. **Start the server:**
   ```bash
   uvicorn app.main:app --reload
   ```

2. **Access the API:**
   Open your browser and navigate to `http://localhost:8000` to access the API. You can also visit `http://localhost:8000/docs` for the interactive API documentation.