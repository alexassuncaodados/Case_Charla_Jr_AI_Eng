# Extrator de Nota Fiscal com IA

Sistema de extração automática de dados de Notas Fiscais de Serviço (NFSe) usando inteligência artificial Google Gemini com **processamento em lote**.

## Funcionalidades

- ✅ **Processamento em lote** de múltiplos PDFs
- ✅ Extração automática de dados de PDF(texto ou imagens)
- ✅ Processamento via Google Gemini 2.5 Flash
- ✅ Validação de dados com Pydantic
- ✅ Saída em JSON


## Dados Extraídos

- **Descrição do Serviço**: Detalhamento dos serviços prestados
- **Valor do Serviço**: Valor monetário do serviço
- **Número da NF**: Número da nota fiscal
- **Data de Emissão**: Data de emissão da nota
- **Valor Total**: Valor total bruto da nota
- **CNPJ**: CNPJ da empresa emitente

## Instalação

1. **Clone o repositório**
   ```bash
   git clone <url-do-repositorio>
   cd "Engenheiro de IA JR - Charla"
   ```

2. **Crie o ambiente virtual (Python >=3.13)**
   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate
   
   # Linux/Mac
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as credenciais do VertexAI**
   - Baixe o arquivo de credenciais JSON do VertexAI
   - Copie o arquivo `.env.example` para `.env`
   - Edite o arquivo `.env` e configure o caminho para suas credenciais:
     ```
     GOOGLE_APPLICATION_CREDENTIALS=./seu-arquivo-credenciais.json
     ```

## Uso

### Via Script Python

1. Coloque todos os arquivos PDF de notas fiscais dentro da pasta `nota_fiscal/`
2. Execute o script para processar todos os PDFs:
   ```bash
   python app.py
   ```
   
**O sistema processará automaticamente todos os arquivos PDF encontrados na pasta e exibirá:**
- Progresso do processamento (arquivo X de Y)
- Dados extraídos de cada nota fiscal
- Relatório de erros (se houver)

## Estrutura do Projeto

```
├── app.py                    # Script principal
├── requirements.txt          # Dependências
├── .env.example              # Template de configuração
├── .env                      # Variáveis de ambiente (não versionado)
├── .gitignore                # Arquivos ignorados pelo Git
├── nota_fiscal/              # Pasta com arquivos PDF
│   ├── nota_001.pdf         # Notas fiscais para processar
│   ├── nota_002.pdf         # (adicione quantas precisar)
│   └── ...
└── utils/
    ├── AgenteCharla.py       # Criação do agente IA
    └── BaseModel.py          # Modelo de dados Pydantic
```

## Exemplo de Saída

### Processamento em Lote
```
Encontrados 3 arquivos PDF para processar...

--- Processando arquivo 1/3: nota_fiscal_001.pdf ---
Resultado extraído:
{
  "descricao_servico": "MENSALIDADE EAD - EDUCAÇÃO SUPERIOR", 
  "valor_servico": 138.33,
  "numero_nf": 4365344,
  "data_emissao": "2025-10-02",
  "valor_total": 138.33,
  "cnpj": "04986320003139"
}

--- Processando arquivo 2/3: nota_fiscal_002.pdf ---
Resultado extraído:
{
  "descricao_servico": "CONSULTORIA EM TI",
  "valor_servico": 1500.00,
  "numero_nf": 7891234,
  "data_emissao": "2025-10-01", 
  "valor_total": 1500.00,
  "cnpj": "12345678000195"
}
```

## Tecnologias Utilizadas

- **Python >=3.13**
- **PydanticAI**: Framework para agentes de IA
- **Google Gemini**: Modelo de linguagem para extração
- **Pydantic**: Validação de dados


## Requisitos

- **Python >=3.13** (recomendado)
- Pasta `nota_fiscal/` com arquivos PDF das notas fiscais



## Licença

Este projeto foi desenvolvido como parte de um case técnico.