# Docusaurus Feedback Backend
This is a backend application for saving and receiving user feedbacks, powered by fastapi and sqlite to use with docusaurus sites. Follow the link to read the tutorial for the frontend.

https://gokhang1327.medium.com/how-to-add-feedbacks-to-docusaurus-df18559ce59f

# Testing
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
pytest
```

# Running
```
uvicorn app.main:app --reload
```

# Endpoints

## Get feedbacks
***Note: url is docusaurus path for the document***
```http
POST /api/notes
Host: localhost:8000
Content-Type: application/json

{
    "url": "/test"
}
```
### Response:
```json
{
    "status": "success",
    "positive_feedback": 0,
    "negative_feedback": 0
}
```

## Post feedback
***Note: Positive feedback is 1 and negative feedback is -1***
```http
POST /api/notes/new
Host: localhost:8000
Content-Type: application/json

{
    "url": "/test",
    "feedback": 1
}
```
### Response:
***Note: "positive_feedback" is number of positive feedbacks and***
***"negative_feedback" is number of negative feedbacks***
```json
{
    "status": "success",
    "note": {
        "url": "/test",
        "id": "00dbd17c-6504-49ed-82c8-6e87f93b6da3",
        "feedback": 1,
        "createdAt": "2023-02-11T23:26:27",
        "ip": "127.0.0.1"
    },
    "positive_feedback": 1,
    "negative_feedback": 0
}
```
