# Registro do uso de IA — entrega de IA&ML

Ferramenta: **Claude Code** (modelo Claude Opus 5.5, Anthropic), usado como assistente de programação no computador do grupo, em 17/11/2026.

## O que pedimos

Prompt principal (resumido):

> Desenvolva a entrega de Inteligência Artificial & Machine Learning da SombraSP nesta pasta. Leia o briefing (slides 31–33) e a ficha da CitizenTech. Transforme o problema em uma pergunta de ML (ex.: prever se o próximo dia terá risco de calor alto na estação INMET Mirante de Santana A701) e responda com dados reais e públicos do INMET, documentando fonte, link e período. Use um modelo entre XGBoost, Random Forest, MLP, LSTM ou KMeans+PCA, justificando. Faça limpeza, divisão treino/teste, teste pelo menos 10 combinações de 3 hiperparâmetros com validação cruzada só no treino, mostre métricas de treino e teste lado a lado com gráficos, discuta overfitting e conclua o que significa para o cidadão. Gere o notebook executado, `dados/README.md`, `requirements.txt`, `RELATORIO_ML.md`, `README.md`, `prompts.md` e o roteiro do vídeo.

## O que a IA fez

| Etapa | O que a IA fez | O que o grupo decidiu / revisou |
|---|---|---|
| Dados | Escreveu `ml/dados/baixar_dados_inmet.py`, baixou os ZIPs anuais do portal do INMET (2015–2026) e extraiu só a estação A701. Descobriu que o portal exige *user-agent* de navegador e que o formato de data/hora muda em 2019. | Conferir no portal que os arquivos são os mesmos. |
| Pergunta de ML | Comparou dois alvos nos dados: índice de calor ≥ 32 °C (só ~4 % dos dias, raro demais) e máxima ≥ 31 °C (~17 %, percentil 84 do treino). Ficou com o segundo. | Validar se 31 °C faz sentido para a SombraSP. |
| Modelo | Escolheu Random Forest e justificou contra XGBoost, MLP/LSTM e KMeans+PCA. | — |
| Experimentos | Rodou um teste exploratório (fora do notebook) com variáveis das 21h e vento em componentes norte/leste: não melhorou (F1 0,673 contra 0,675), então ficaram de fora. Adicionou a comparação com a regra de persistência ("amanhã igual a hoje") ao perceber que ela é uma referência forte, e a escolha do limiar de alerta pela validação do treino. | — |
| Notebook | Escreveu e executou o notebook de ponta a ponta (24 combinações × 5 dobras de `TimeSeriesSplit`). | Ler o notebook inteiro e saber explicar cada célula. |
| Textos | Redigiu `README.md`, `RELATORIO_ML.md`, `ml/dados/README.md` a partir dos números gerados pelo notebook. | Revisar o texto. |

## Cuidados

- Todos os números do relatório vêm das saídas do notebook executado; nada foi inventado ou simulado.
- Nenhum dado pessoal foi usado: só dados meteorológicos públicos do INMET.
- A pedido do grupo, a IA criou o repositório no GitHub e enviou os arquivos (18/11/2026). O envio no Teams fica com o grupo (o vídeo deixou de ser exigido, conforme orientação do professor).
