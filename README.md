# Task Manager Backend API

FastAPI backend for task management with JWT authentication and MongoDB.

API url: <https://j5s3m0dla9.execute-api.us-east-1.amazonaws.com/dev/>

## Features

- ✅ User registration & login
- 🔐 JWT authentication
- 📝 Task CRUD operations
- 🗄️ MongoDB storage
- 🔒 Password hashing
- 🌐 CORS enabled
- � Docker ready
- ☁️ Serverless compatible

## Tech Stack

| Component       | Technology          |
|-----------------|---------------------|
| Framework       | FastAPI             |
| Database        | MongoDB             |
| Auth            | JWT                 |
| Validation      | Pydantic            |
| Password Hashing| Passlib (bcrypt)    |
| Async DB Driver | Motor               |

## API Endpoints

### Auth Routes

| Method | Endpoint  | Description           |
|--------|-----------|-----------------------|
| POST   | /register | Register new user     |
| POST   | /login    | Login and get JWT     |

### Task Routes (Auth required)

| Method | Endpoint         | Description       |
|--------|------------------|-------------------|
| POST   | /tasks           | Create task       |
| GET    | /tasks           | List all tasks    |
| PUT    | /tasks/{task_id} | Update task       |
| DELETE | /tasks/{task_id} | Delete task       |

## Setup

### Prerequisites

- Python 3.9+
- MongoDB
- Docker (optional)

### Installation

1. Clone repo:
```bash
git clone https://github.com/your-repo/task-manager-backend.git
cd task-manager-backend
```

2. Create virtual env:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create .env file:
```bash
DB_STRING=mongodb+srv://root:bIpODxpDbkDaz2Ge@taskmanager-dev-us-east.tcdf4l5.mongodb.net/?retryWrites=true&w=majority&appName=taskmanager-dev-us-east1-cluster
DB_NAME=task_manager
DB_TEST_NAME=test_task_manager
SECRET_KEY=your-strong-secret-key
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

### Running the App
#### Development
```bash
uvicorn src.main:app --reload
```

#### Production
```bash
uvicorn src.main:app --host 0.0.0.0 --port 8000
```

#### With Docker
```bash
docker-compose up --build
```

#### Testing
```bash
TESTING=True pytest
```

### Environment Variables

|Variable                    | Required | Default                   |
|----------------------------|----------|---------------------------|
|DB_STRING                   | Yes      | mongodb://localhost:27017 |
|DB_NAME                     | Yes      | task_manager              |
|DB_TEST_NAME                | No       | test_task_manager         |
|SECRET_KEY                  | Yes      | -                         |
|ACCESS_TOKEN_EXPIRE_MINUTES | No       | 60                        |

### Documentation (Swagger UI)
- Online: <https://j5s3m0dla9.execute-api.us-east-1.amazonaws.com/dev/docs>
- Locally (after running proyect): <http://localhost:8000/docs>

### Deployment
#### Serverless (AWS Lambda)
```bash
serverless deploy
```

#### Docker
```bash
docker build -t task-manager-backend .
docker run -p 8000:8000 task-manager-backend
```

### Project Structure
```
task-manager-backend/
├── src/
│   ├── api/          # Route handlers
│   ├── auth/         # Auth logic
│   ├── models/       # Data models
│   ├── services/     # Business logic
│   ├── config.py     # DB config
│   └── main.py       # App entrypoint
├── tests/            # Tests
├── venv/             # Virtual env
└── config files      # Docker, serverless etc.
```
