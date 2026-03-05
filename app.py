from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
todos = []
templates = Jinja2Templates(directory="templets")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "todos": todos})

@app.post("/add")
def add_todo(request: Request, todo: str = Form(...)):
    todos.append(todo)
    return RedirectResponse("/", status_code=303)

@app.post("/remove")
def remove_todo(request: Request, index: int = Form(...)):
    if 0 <= index < len(todos):
        todos.pop(index)
    return RedirectResponse("/", status_code=303)