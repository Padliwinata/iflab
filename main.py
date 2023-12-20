from fastapi import FastAPI
from utils import *


app = FastAPI()


@app.get('/aslab')
def get_data_aslab():
    return get_aslab()
