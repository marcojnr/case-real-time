# case-real-time

### Visão geral
Este repositório contém um Estudo de Caso que simula eventos de vendas a partir de um CSV e demonstra uma pipeline de streaming (produtor -> Event Hub -> processamento). O objetivo é servir como base para aprendizado e experimentos com arquiteturas real-time.

### Estrutura do repositório
- [data/Sales Transaction v.4a.csv]— dataset de exemplo (vendas).
- [src/producer.py](src/producer.py) — script que injeta eventos (simulação de produtor).
- [src/databricks_stream.py](src/databricks_stream.py) — exemplo de pipeline de processamento (Databricks / Structured Streaming).
- [docs/diagrama-case.drawio](docs/diagrama-case.drawio) — diagrama arquitetural.
- [requirements.txt](requirements.txt) — dependências Python.
- [.gitignore](.gitignore)

### Pré-requisitos
- Python 3.8+
- Criar e ativar um ambiente virtual (recomendado)
- Instalar dependências:
```sh
python -m venv .venv
source .venv/bin/activate  # macOS / Linux
.venv\Scripts\activate     # Windows
pip install -r [requirements.txt](http://_vscodecontentref_/7)
```

### Execução (exemplo)
1. Simular produção de eventos (envia linhas do CSV como eventos):
```sh
python src/producer.py
```
2. Pipeline de processamento:
- Adaptar e executar `src/databricks_stream.py` em um ambiente Spark/Databricks compatível.

### Observação
Este projeto é apenas um exemplo/prova de conceito e foi criado para demonstração. Há muitas melhorias e adaptações possíveis para torná-lo adequado a um ambiente de produção (segurança, escalabilidade, testes, etc.).


### Alguns próximos passos 
- Tornar o produtor configurável (taxa, paralelismo).
- Suportar múltiplos formatos de entrada (JSON).
- Automatizar escrita para Delta Lake (bronze/silver/gold) com jobs de curadoria.
- Adicionar observabilidade: métricas, logs estruturados e dashboards.
- Criar CI/CD  para provisionamento.
- Adicionar testes unitários e integração.
