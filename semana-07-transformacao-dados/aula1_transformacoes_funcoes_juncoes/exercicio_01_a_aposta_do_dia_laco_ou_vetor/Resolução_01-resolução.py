from pathlib import Path

import numpy as np
import pandas as pd

BASE = Path(__file__).parent if "__file__" in globals() else Path.cwd()
PASTA_EXTRA = BASE.parent / "exercicio_07_juntando_tabelas"


def ler_csv(nome: str) -> pd.DataFrame:
    for pasta in (BASE, PASTA_EXTRA):
        arquivo = pasta / nome
        if arquivo.exists():
            return pd.read_csv(arquivo)
    raise FileNotFoundError(f"Não encontrei {nome} em {BASE} nem em {PASTA_EXTRA}")


pedidos = ler_csv("pedidos.csv")
produtos = ler_csv("produtos.csv")
clientes = ler_csv("clientes.csv")
print(pedidos.shape, produtos.shape, clientes.shape)
print(pedidos[["id_pedido", "data", "qtd", "canal"]].head(3))
