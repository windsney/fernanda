import pandas as pd
import os

# 📂 Caminho do arquivo
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
caminho_excel = os.path.join(BASE_DIR, 'Votos_Coronel.xlsx')

try:
    # 📖 Lendo o arquivo Excel (xlsx)
    # Nota: pode ser necessário instalar a biblioteca openpyxl: pip install openpyxl
    df = pd.read_excel(caminho_excel)
    
    # 📋 Padronizando os nomes para MAIÚSCULAS
    df['Município'] = df['Município'].str.upper()
    
    # 🔢 Criando o dicionário de votos
    votos_map = dict(zip(df['Município'], df['Total de Votos']))
    
    print("✅ Dados carregados com sucesso!")
    print(f"Exemplo: CUIABÁ tem {votos_map.get('CUIABÁ', 0)} votos.")

except Exception as e:
    print(f"❌ Erro ao ler o Excel: {e}")