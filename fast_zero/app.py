# Importando da biblioteca fastapi do objeto FastAPI
from fastapi import FastAPI

# Iniciando uma aplicação FastAPI
app = FastAPI()


# Definindo um endpoint com o endereço / acessível pelo método HTTP GET
@app.get('/')
def read_root():
    # Função que será executada quando o endereço / for acessado por um cliente

    # Os dados que serão retornados pelo endereço quando for chamado
    return {'message': 'olá Mundo!'}
