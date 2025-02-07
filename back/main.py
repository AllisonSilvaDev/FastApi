import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel


class inputs(BaseModel):
    inp: int
    inp2: str

app = FastAPI()

vendas = {
    1: {"Item": "lata", "preco_uni": 4, "quantidade": 5},
    2: {"Item": "Garrafa 2l", "preco_uni": 15, "quantidade": 5},
    3: {"Item": "garrafa 750ml", "preco_uni": 10, "quantidade": 5},
    4: {"Item": "lata mini", "preco_uni": 2, "quantidade": 5},
}

@app.get("/")
def home():
    return {"Vendas":(vendas)}

@app.get("/vendas/{id_venda}")
def pegar_venda(id_venda: int):
    if id_venda in vendas:
        return vendas[id_venda]
    else:
        return {"Erro: product not found !"}
    
@app.post("/exemplo")
def example(inputs: inputs):
    return inputs.inp2, inputs.inp