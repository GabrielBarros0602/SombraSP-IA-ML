"""Baixa os dados horários da estação INMET A701 (São Paulo - Mirante de Santana).

O INMET publica um ZIP por ano com todas as estações automáticas do Brasil
(~100 MB cada). Este script baixa cada ZIP, extrai só o CSV da A701 e apaga o ZIP.

Uso (de dentro da pasta ml/):  python dados/baixar_dados_inmet.py
"""
import sys
import tempfile
import urllib.request
import zipfile
from pathlib import Path

ANOS = range(2015, 2027)  # 2026 é parcial (o INMET atualiza o ZIP do ano corrente)
URL = "https://portal.inmet.gov.br/uploads/dadoshistoricos/{ano}.zip"
ESTACAO = "A701"
DESTINO = Path(__file__).resolve().parent / "brutos"
# o portal derruba conexões sem user-agent de navegador
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}


def baixar(ano: int) -> None:
    saida = DESTINO / f"INMET_A701_{ano}.csv"
    if saida.exists():
        print(f"{ano}: já existe, pulando")
        return
    with tempfile.TemporaryDirectory() as tmp:
        zip_path = Path(tmp) / f"{ano}.zip"
        print(f"{ano}: baixando {URL.format(ano=ano)} ...", flush=True)
        req = urllib.request.Request(URL.format(ano=ano), headers=HEADERS)
        with urllib.request.urlopen(req, timeout=600) as resp, open(zip_path, "wb") as f:
            while bloco := resp.read(1 << 20):
                f.write(bloco)
        with zipfile.ZipFile(zip_path) as z:
            nomes = [n for n in z.namelist() if f"_{ESTACAO}_" in n.upper() and n.upper().endswith(".CSV")]
            if len(nomes) != 1:
                sys.exit(f"{ano}: esperava 1 arquivo da {ESTACAO}, achei {nomes}")
            # grava com nome fixo; não usa o caminho de dentro do ZIP
            saida.write_bytes(z.read(nomes[0]))
            print(f"{ano}: salvo {saida.name}  (original: {nomes[0]})")


if __name__ == "__main__":
    DESTINO.mkdir(parents=True, exist_ok=True)
    for ano in ANOS:
        baixar(ano)
