import datetime
import re

def calcular_idade(data_nascimento, data_referencia):
    """Calcula a idade com base na data de nascimento e uma data de referência."""
    idade = data_referencia.year - data_nascimento.year

    if (data_referencia.month, data_referencia.day) < (data_nascimento.month, data_nascimento.day):
        idade -= 1
    return idade

def corrigir_idade_no_readme(idade_calculada, caminho_readme="README.md"):

    try:
        with open(caminho_readme, "r", encoding="utf-8") as f:
            conteudo = f.read()

        padrao_idade = re.compile(r"(tenho )(\d+)( anos)", re.IGNORECASE)
        
        match = padrao_idade.search(conteudo)

        if match:
            idade_no_arquivo_str = match.group(2) 
            idade_no_arquivo = int(idade_no_arquivo_str)
            
            if idade_no_arquivo == idade_calculada:
                return 

            conteudo_novo = padrao_idade.sub(rf"\g<1>{idade_calculada}\g<3>", conteudo)
            
            with open(caminho_readme, "w", encoding="utf-8") as f:
                f.write(conteudo_novo)
            
    except Exception:
        pass 


data_nascimento = datetime.date(2004, 10, 14)
data_hoje = datetime.date.today()

idade_calculada = calcular_idade(data_nascimento, data_hoje)

corrigir_idade_no_readme(idade_calculada)
