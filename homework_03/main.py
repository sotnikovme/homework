from typing import Union

from fastapi import FastAPI, Query, Path

app = FastAPI()


@app.get("/ping/")
def read_root():
    return {"message": "pong"}



    