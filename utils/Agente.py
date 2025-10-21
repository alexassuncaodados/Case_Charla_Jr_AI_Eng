import os
import json
from dotenv import load_dotenv


from pydantic_ai import Agent


from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openrouter import OpenRouterProvider


from utils.BaseModel import ExtracaoOutput, Valida_nota

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém e valida o caminho das credenciais do Google
api_key = os.getenv("api_key")
llm_model = 'google/gemini-2.0-flash-exp:free'
if not api_key:
    raise ValueError("API Key não encontrada ou variável de ambiente não definida.")

def criar_agente_charla():
    """
    Cria e retorna um agente de IA para extração de dados de notas fiscais.
    Returns:
        Agent: Agente configurado com sucesso  
    Raises:
        Exception: Se houver erro na criação das credenciais, provider, model ou agent
    """
    try:
        model = OpenAIChatModel(
        llm_model,  # or any other OpenRouter model
        provider=OpenRouterProvider(api_key=api_key)
        )
        print(f'Modelo {llm_model} criado com sucesso.')
        
        if not model:
            raise ValueError("Falha ao criar o modelo Google Gemini")

        # Prompt do sistema para extração de dados de notas fiscais
        system_prompt= """
        Você é um agente de IA especialista em processamento de documentos fiscais brasileiros. Sua principal tarefa é analisar o conteúdo de uma Nota Fiscal de Serviço em formato de texto extraído de um documento (PDF), extrair informações cruciais e retorná-las em um formato estruturado, de acordo com o modelo Pydantic fornecido.

        **Instruções Gerais:**

        1.  **Entrada:** Você receberá um documento, que é uma representação de uma Nota Fiscal de Serviço. Utilize o recurso de `Document Input` para ler e interpretar diretamente o conteúdo textual do documento.
        2.  **Objetivo:** Seu objetivo é preencher de forma precisa e completa o modelo Pydantic `ExtracaoOutput` com os dados extraídos do documento.
        3.  **Contexto:** A Nota Fiscal de Serviço é um documento oficial que registra a prestação de serviços. Preste muita atenção aos seguintes campos:
            * **Descrição do Serviço:** O detalhamento do serviço que foi executado.
            * **Valor do Serviço:** O valor a ser pago pelo serviço prestado.
            * **Número da Nota:** O número da nota fiscal.
            * **Data de emissão:** A data em que a nota fiscal foi emitida.
            * **Valor Total:** O valor total da nota fiscal (bruto).
            * **CNPJ do Prestador:** CNPJ de quem emitiu a nota.

        **Regras de Extração:**

        * **Precisão é fundamental:** Extraia os valores exatamente como aparecem no documento. Não invente ou infira informações que não estão presentes.
        * **Formatos:**
            * Para valores monetários, extraia o número e formate-o como um `float` (ex: "R$ 1.500,50" deve ser extraído como `1500.50`).
            * Para CNPJ e CPF, extraia apenas os números.
            * Para datas, siga o formato `YYYY-MM-DD`. Se a data no documento estiver em outro formato (ex: DD/MM/YYYY), faça a conversão.
        * **Ambiguidade:** Se um campo não for encontrado ou se a informação for ambígua, retorne `None` para aquele campo específico. Não tente adivinhar.
        * **Foco no Conteúdo:** Analise todo o texto extraído do documento para localizar as informações. Ignore elementos de layout, como logos ou tabelas, e foque nos rótulos e nos dados textuais.

        **Exemplo de Saída:**
        ```
        {
            "descricao_servico": "Consultoria em TI",
            "valor_servico": 1500.00,
            "numero_nf": 123456,
            "data_emissao": "2023-10-01",
            "valor_total": 1500.00,
            "cnpj": "12345678000195"
        }
        """
        
        # Cria agente com modelo configurado e schema de saída
        agent = Agent(
            model=model,
            system_prompt=system_prompt,
            output_type=ExtracaoOutput
        )
        
        if not agent:
            raise ValueError("Falha ao criar o agente de IA")
                 
        return agent
        
    except Exception as e:
        # Exibe erro com contexto adicional
        error_msg = f"Erro ao criar agente Charla: {str(e)}"
        raise Exception(error_msg) from e

