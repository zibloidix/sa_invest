from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return ""

@app.get("/projects")
def read_projects(project_id: int, q: Union[str, None] = None):
    return []

@app.get("/projects/{project_id}")
def read_project(project_id: int, q: Union[str, None] = None):
    return [{}]