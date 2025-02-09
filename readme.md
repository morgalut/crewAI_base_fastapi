# 🚀 CrewAI + FastAPI Project

## 📌 Overview
This project integrates **CrewAI** with **FastAPI** to manage IoT event ingestion, processing, and alerting using a microservices architecture. The system dynamically creates agents and assigns them tasks, leveraging PostgreSQL for data persistence and OpenAI for intelligent task execution.

## 🛠️ Tech Stack
- **FastAPI** - Backend API framework
- **SQLAlchemy** - ORM for PostgreSQL database
- **PostgreSQL** - Database for storing agents and tasks
- **CrewAI** - AI-based task execution
- **Docker** - Containerization (optional)
- **RabbitMQ / Redis** - (Future integration for messaging)

## 📂 Project Structure
```
crewAI_base_fastapi/
│── crew_ai_project/
│   ├── agents.py        # Defines AI agents
│   ├── base.py          # SQLAlchemy base model
│   ├── crud.py          # Database operations
│   ├── database.py      # Database connection setup
│   ├── main.py          # FastAPI endpoints
│   ├── models.py        # SQLAlchemy models
│   ├── services.py      # Task execution logic
│   ├── tasks.py         # Task definitions
│── .gitignore           # Git ignored files
│── README.md            # Project documentation
```

## 🚀 Installation & Setup
### 1️⃣ Clone Repository
```sh
git clone https://github.com/morgalut/crewAI_base_fastapi.git
cd crewAI_base_fastapi
```

### 2️⃣ Create Virtual Environment
```sh
python -m venv env
source env/bin/activate  # For macOS/Linux
env\Scripts\activate    # For Windows
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
Create a `.env` file in the project root with:
```
DATABASE_URL=postgresql://admin:admin@localhost:5432/crewai
OPENAI_API_KEY=your_openai_api_key_here
```

### 5️⃣ Run Database Migrations
```sh
python -m database
```

### 6️⃣ Start FastAPI Server
```sh
uvicorn main:app --reload
```

## 📡 API Endpoints
| Method | Endpoint | Description |
|--------|---------|-------------|
| **POST** | `/agents/` | Create an agent with tasks |
| **GET** | `/agents/` | Fetch all agents |
| **POST** | `/run-tasks/` | Execute assigned tasks |

## 🎯 Example API Usage
### Create an Agent with Tasks
```sh
curl -X POST "http://127.0.0.1:8000/agents/" \
-H "Content-Type: application/json" \
-d '{
    "name": "John Doe",
    "role": "IoT Security Analyst",
    "goal": "Detect anomalies in IoT data",
    "backstory": "Cybersecurity expert specialized in IoT threats.",
    "tasks": [
        {"description": "Analyze security logs"},
        {"description": "Detect unauthorized access"}
    ]
}'
```

### Run Tasks
```sh
curl -X POST "http://127.0.0.1:8000/run-tasks/"
```

## 🛠️ Future Improvements
- 🔹 Add Redis/RabbitMQ for event processing
- 🔹 Implement real-time alerting
- 🔹 Expand AI models for advanced automation

## 🤝 Contribution
Feel free to submit issues or pull requests to improve the project!

## 📜 License
MIT License © 2025 morgalut
