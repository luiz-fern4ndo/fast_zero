from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def ready_root():
    return {'message': 'Olá Mundod!'}
