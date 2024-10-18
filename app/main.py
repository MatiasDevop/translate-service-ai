from fastapi import FastAPI, BackgroundTasks, HTTPException, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

from . import schemas
from . import models
from . import crud
from .database import get_db, engine
from pathlib import Path


models.Base.metadata.create_all(bind=engine)
app = FastAPI()

#Setup for Jinja2 templates
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

#################################################################

@app.get('/index', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html",  { "request": request})



@app.post("/translate", response_model=schemas.TaskResponse)
def translate(request: schemas.TranslationRequest, background):
    # create a new translation task
    task = crud.create_translation_task(get_db.db, request.text, request.languages)

    Background_tasks.add_task(perform_translation, task_id, request.text, request.languages, get_db.db)

    return { "task_id": {task.id}}