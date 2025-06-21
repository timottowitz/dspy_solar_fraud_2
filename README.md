# DSPy Solar Fraud Toolkit

This project demonstrates a simple DSPy pipeline for generating a Statement of Claims along with a small React front‑end and API server.

## Requirements
- Python 3.12+
- Node 18+

## Setup
1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Install Node dependencies for the front‑end and server:
   ```bash
   cd frontend
   npm install
   cd ..
   ```
3. Create a `.env` file with your `OPENAI_API_KEY`.

## Running
### Backend API
Start the API server:
```bash
cd frontend
npm run server
```
The server exposes a `POST /generate` endpoint that accepts JSON client data and returns the generated document.

### Front‑end
From the `frontend` directory run:
```bash
npm run dev
```
This starts Vite in development mode. Open the printed URL in your browser.

## Generating Locally
You can also run the pipeline directly:
```bash
python main.py
```
The resulting Statement of Claims will be written to a text file.
