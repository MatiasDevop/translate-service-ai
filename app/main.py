from fastapi import FastAPI, BackgroundTasks, HTTPException, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from fastapi.templating import Jinja2Templates
from pathlib import Path
import schemas

app = FastAPI()

#Setup for Jinja2 templates
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

@app.get('/index', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html",  { "request": request})


# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.post("/translate", response_model=schemas.TaskResponse)
def translate(request: schemas.TranslationRequest):
    # create a new translation task
    task = crud.create_translation_task(x, y, ,p)

    Background_tasks.add_task(perform_translation, task_id, request.text, request.languages, db)