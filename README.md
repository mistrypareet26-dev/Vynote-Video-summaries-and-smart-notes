# 🎬 Vynote – YouTube Video Summarizer & Smart Notes

**Turn long YouTube videos into concise, organized notes with AI.**

Vynote is an AI-powered YouTube video summarization and note-taking application. It extracts video transcripts, generates concise summaries using a Large Language Model (LLM), and saves the generated summaries for future reference.

The application uses Streamlit for the frontend, FastAPI for backend services, and SQLite for storing notes.

## ✨ Features

- **YouTube Transcript Extraction:** Fetches available transcripts from YouTube videos.
- **AI-Powered Summarization:** Converts lengthy video transcripts into concise, meaningful bullet points.
- **Smart Notes:** Saves generated summaries for future reference.
- **Notes Management:** View previously generated summaries.
- **REST API:** Uses FastAPI to handle frontend and backend communication.
- **Interactive Interface:** Provides a simple and user-friendly Streamlit interface.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Frontend development |
| FastAPI | Backend API development |
| SQLite | Database |
| SQLModel | Database models and operations |
| Groq API | AI-powered text summarization |
| YouTube Transcript API | Extracting video transcripts |
| Requests | Frontend-backend communication |

## 📁 Project Structure

```text
Vynote/
│
├── backend/
│   ├── main.py
│   ├── transcript.py
│   ├── summarizer.py
│   ├── models.py
│   └── database.py
│
├── frontend/
│   └── [Streamlit frontend files]
│
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/mistrypareet26-dev/Vynote-Video-summaries-and-smart-notes.git
```

### 2. Navigate to the project directory

```bash
cd Vynote-Video-summaries-and-smart-notes
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file in the project root directory and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key
```

**Note:** Never upload your `.env` file or expose your API key publicly.

### 6. Run the backend

Open a terminal in the project directory:

```bash
uvicorn backend.main:app --reload
```

The FastAPI server will run at:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

### 7. Run the frontend

Open another terminal, activate the virtual environment, and run:

```bash
streamlit run frontend/YOUR_FRONTEND_FILE.py
```

Replace `YOUR_FRONTEND_FILE.py` with the actual name of your Streamlit Python file.

## 🔄 Application Workflow

1. User enters a YouTube video URL.
2. Streamlit sends the URL to the FastAPI backend.
3. The backend extracts the YouTube video ID.
4. The transcript is fetched using the YouTube Transcript API.
5. The transcript is divided into smaller chunks when necessary.
6. Groq API generates summaries from the transcript.
7. The generated summary is saved in the SQLite database.
8. The summary is returned to the frontend and displayed to the user.
9. Previously saved notes can be retrieved through the application.

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check API status |
| POST | `/summarize` | Generate and save a video summary |
| GET | `/notes` | Retrieve all saved notes |
| GET | `/notes/{note_id}` | Retrieve a specific note |
| DELETE | `/notes/{note_id}` | Delete a saved note |

## 🚀 Future Improvements

- Add support for more languages.
- Improve summary formatting and organization.
- Add search and filtering for saved notes.
- Allow users to download summaries.
- Add user authentication and personalized notes.
- Improve the dashboard and user experience.

## 🎯 Project Objective

The objective of Vynote is to make video-based learning more efficient by transforming lengthy video content into concise, accessible, and reusable notes.

---

**Developed with Python, Streamlit, FastAPI, and AI.**