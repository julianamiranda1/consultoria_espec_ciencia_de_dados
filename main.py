from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI(
    title="Santo Garfo API",
    description="API do restaurante Santo Garfo",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {
        "restaurante": "Santo Garfo",
        "mensagem": "Bem-vindo à nossa API",
        "chef": "Juliana Miranda",
        "cidade": "São Paulo",
        "especialidade": "Comida brasileira"
    }

pratos = [{"id": 1, "nome": "Baião de Dois", "categoria": "Prato Principal", "preco": 44.90, "disponivel": True},
          {"id": 2, "nome": "Acarajé", "categoria": "Prato Principal", "preco": 31.00, "disponivel": False},
          {"id": 3, "nome": "Feijoada", "categoria": "Prato Principal", "preco": 50.00, "disponivel": True},
          {"id": 4, "nome": "Moqueca", "categoria": "Prato quente", "preco": 45.00, "disponivel": True},
          {"id": 5, "nome": "Virado à Paulista", "categoria": "Prato Principal", "preco": 30.00, "disponivel": False}]

@app.get("/pratos/{prato_id}/detalhes")
async def buscar_prato(prato_id: int, formato: str = "completo"):
    for prato in pratos:
        if prato["id"] == prato_id:
            if formato == "resumido":
                return {"nome": prato["nome"], "preco": prato["preco"]}
            return prato
    return {"mensagem": "Prato não encontrado"}

@app.get("/pratos")
async def listar_pratos(categoria: Optional[str] = None,
                        preco_max: Optional[float] = None,
                        apenas_disponiveis: bool = False):

    resultado = pratos

    if categoria:
        resultado = [p for p in resultado if p["categoria"] == categoria]
    if preco_max:
        resultado = [p for p in resultado if p["preco"] <= preco_max]
    if apenas_disponiveis:
        resultado = [p for p in resultado if p["disponivel"]]
    return resultado