# 🤖 Chatbot - Flask-Based Conversational AI

A ChatGPT-like chatbot built with **Flask**, supporting room-specific conversations, persistent chat history, sentiment analysis, and FAQ analytics.  
Easily deployable with **Docker** and backed by **MongoDB** for robust data persistence.

---

## ✨ Features

- 🗣️ Room-specific conversations
- 🧠 Persistent chat history with MongoDB
- 😃 Sentiment analysis using TextBlob
- 📊 Analytics dashboard for frequent questions
- 🐳 Dockerized deployment
- 🌐 REST API endpoints for chatbot interaction

---

## 📂 Project Structure

```
chatbot/
├── app/
│   ├── __init__.py
│   ├── models/
│   ├── routes/
│   ├── templates/
│   ├── static/
│   └── utils.py
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env.example
├── .gitattributes
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Docker (optional, for container deployment)
- MongoDB (local or cloud via MongoDB Atlas)

### Installation (Local)

```
git clone https://github.com/JPdev6/chatbot.git
cd chatbot
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
flask run
```

Open your browser at:

```
http://localhost:5000/
```

---

## 🐳 Run with Docker

To build and run using Docker:

```
docker-compose up --build
```

This starts:
- Flask backend
- MongoDB database

---

## 📄 Environment Variables

Create a `.env` file (or copy from `.env.example`) with:

```
FLASK_APP=app
FLASK_ENV=development
MONGO_URI=mongodb://localhost:27017/chatbot
SECRET_KEY=your-secret-key-here
```

---

## 📊 Analytics

- View frequently asked questions
- Analyze sentiment trends
- Monitor chat activity per room

Accessible via a secure admin dashboard.

---

## 📊 Technologies Used

- Flask
- MongoDB
- Docker
- Jinja2
- TextBlob
- Bootstrap

---

## 🤝 Contributing

Contributions are welcome!  
Fork the repository, improve it, and submit a pull request.

---

## 📄 License

This project is licensed under the **MIT License**.
