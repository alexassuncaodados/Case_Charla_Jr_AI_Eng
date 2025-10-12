# Importações necessárias
import asyncio
from utils.AgenteCharla import criar_agente_charla
from utils.BaseModel import ExtracaoOutput

from pydantic_ai import BinaryContent
from pathlib import Path

def main_sync():
    # Inicialização do agente de IA
    try:
        agent = criar_agente_charla()
        print("Agente criado com sucesso!")
    except Exception as e:
        print(f"Erro ao criar agente: {e}")
        return  
    
    # Verificação da existência do arquivo PDF
    nota_fiscal = Path('2000013345952102_251012134611.pdf')
    if not nota_fiscal.exists():
        print(f"Arquivo '{nota_fiscal}' não encontrado.")
        return
    
    # Função assíncrona para processar o documento
    async def process_document():
        # Faz a extração de dados do PDF e executa o agente
        resultado = await agent.run(
            [BinaryContent(nota_fiscal.read_bytes(), media_type='application/pdf')]
        )
        # Exibe o resultado no console
        print(resultado.output.model_dump())
        return resultado
    
    # Executa a função assíncrona
    return asyncio.run(process_document())


if __name__ == "__main__":
    main_sync()