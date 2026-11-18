# Dados — INMET, estação A701 (São Paulo – Mirante de Santana)

Dados **reais e públicos**, sem nenhuma simulação.

| Item | Valor |
|---|---|
| Fonte | INMET — Instituto Nacional de Meteorologia, *Banco de Dados Meteorológicos — Dados Históricos* |
| Link | https://portal.inmet.gov.br/dadoshistoricos (ZIP anual: `https://portal.inmet.gov.br/uploads/dadoshistoricos/<ANO>.zip`) |
| Estação | A701 — SAO PAULO - MIRANTE (código WMO A701), lat −23,50, lon −46,62, alt. ~786 m, zona norte, ~5 km da Sé |
| Período | 01/01/2015 a 31/10/2026 (2026 até o último mês publicado pelo INMET na data do download) |
| Frequência | horária, em UTC (o notebook converte para o horário de Brasília, UTC−3) |
| Licença / uso | dados públicos do governo federal, livres para uso citando a fonte |
| Data do download | 17/11/2026 |

## Arquivos

- `brutos/INMET_A701_<ANO>.csv` (2015 a 2026, ~800 KB cada): o CSV original da A701 extraído do ZIP anual do INMET, sem nenhuma alteração. O script só troca o nome do arquivo (o original está no log do download, ex. `INMET_SE_SP_A701_SAO PAULO - MIRANTE_01-01-2024_A_31-12-2024.CSV`).
- `baixar_dados_inmet.py`: baixa os ZIPs anuais (~100 MB cada, com todas as estações do Brasil), extrai só a A701 e apaga o ZIP. Para refazer o download, apague `brutos/` e rode, de dentro de `ml/`:

  ```
  python dados/baixar_dados_inmet.py
  ```

  O portal do INMET recusa conexões sem *user-agent* de navegador; o script já envia um.

## Formato dos CSVs

- 8 linhas de cabeçalho com metadados da estação, depois a tabela.
- Separador `;`, decimal `,`, codificação `latin1`.
- Falhas de sensor aparecem como `-9999` ou vazio.
- O formato muda entre anos: até 2018 a data é `2015-01-01` e a hora `00:00`; a partir de 2019 a data é `2023/01/01` e a hora `0000 UTC`. O notebook lê as colunas **pela posição** e padroniza.

## Colunas (19, na ordem) → nome usado no notebook

| # | Coluna original (INMET) | Nome no notebook | Unidade |
|---|---|---|---|
| 1 | DATA (YYYY-MM-DD) / Data | `data` | — |
| 2 | HORA (UTC) / Hora UTC | `hora` | UTC |
| 3 | PRECIPITAÇÃO TOTAL, HORÁRIO | `chuva_mm` | mm |
| 4 | PRESSAO ATMOSFERICA AO NIVEL DA ESTACAO, HORARIA | `pressao_hpa` | hPa (mB) |
| 5 | PRESSÃO ATMOSFERICA MAX. NA HORA ANT. | `pressao_max` | hPa |
| 6 | PRESSÃO ATMOSFERICA MIN. NA HORA ANT. | `pressao_min` | hPa |
| 7 | RADIACAO GLOBAL | `radiacao_kj` | kJ/m² (vazio à noite) |
| 8 | TEMPERATURA DO AR - BULBO SECO, HORARIA | `temp_c` | °C |
| 9 | TEMPERATURA DO PONTO DE ORVALHO | `orvalho_c` | °C |
| 10 | TEMPERATURA MÁXIMA NA HORA ANT. | `temp_max_c` | °C |
| 11 | TEMPERATURA MÍNIMA NA HORA ANT. | `temp_min_c` | °C |
| 12 | TEMPERATURA ORVALHO MAX. NA HORA ANT. | `orvalho_max` | °C |
| 13 | TEMPERATURA ORVALHO MIN. NA HORA ANT. | `orvalho_min` | °C |
| 14 | UMIDADE REL. MAX. NA HORA ANT. | `ur_max` | % |
| 15 | UMIDADE REL. MIN. NA HORA ANT. | `ur_min` | % |
| 16 | UMIDADE RELATIVA DO AR, HORARIA | `ur_pct` | % |
| 17 | VENTO, DIREÇÃO HORARIA | `vento_dir` | graus |
| 18 | VENTO, RAJADA MAXIMA | `rajada_ms` | m/s |
| 19 | VENTO, VELOCIDADE HORARIA | `vento_ms` | m/s |

## Qualidade observada

- 103.728 registros horários; ~0,5 % de falhas nas variáveis principais (a radiação tem ~47 % de vazios porque fica vazia à noite).
- Nenhuma leitura fora dos limites físicos usados na limpeza.
- 30 dias com menos de 20 horas válidas foram descartados (há falhas maiores em set–dez/2023).
- Base final do modelo: 4.237 dias com dados válidos de hoje e de amanhã.
