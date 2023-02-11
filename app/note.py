from . import schemas, models
from sqlalchemy.orm import Session
from sqlalchemy import and_
from fastapi import Depends, status, APIRouter, Request
from .database import get_db

router = APIRouter()


@router.post('/')
def get_notes(payload: schemas.Url, db: Session = Depends(get_db)):
    positive_feedback = db.query(models.Note).filter(and_(models.Note.ip != "testclient", models.Note.url == payload.url, models.Note.feedback == 1)).count()
    negative_feedback = db.query(models.Note).filter(and_(models.Note.ip != "testclient", models.Note.url == payload.url, models.Note.feedback == -1)).count()
    return {'status': 'success', 'positive_feedback': positive_feedback, 'negative_feedback': negative_feedback}


@router.post('/new', status_code=status.HTTP_201_CREATED)
def create_note(request: Request, payload: schemas.NoteBaseSchema, db: Session = Depends(get_db)):
    """note_query = db.query(models.Note).filter(models.Note.ip == request.client.host)
    db_note = note_query.first()
    if db_note:
        raise HTTPException(status_code=400,
                            detail=f'same client')"""
    new_note = models.Note(**payload.dict())
    new_note.ip = request.client.host
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    positive_feedback = db.query(models.Note).filter(and_(models.Note.url == new_note.url, models.Note.feedback == 1)).count()
    negative_feedback = db.query(models.Note).filter(and_(models.Note.url == new_note.url, models.Note.feedback == -1)).count()
    return {"status": "success", "note": new_note, 'positive_feedback': positive_feedback, 'negative_feedback': negative_feedback}
