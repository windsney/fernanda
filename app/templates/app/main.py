import pandas as pd
import unicodedata

# Função para limpar nomes (Remove acentos, D', espaços extras, etc)
def limpar_nome(txt):
    if not isinstance(txt, str): return ""
    # Remove acentos (Cáceres -> CACERES)
    txt = unicodedata.normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')
    txt = txt.upper().strip()
    # Padroniza o "D'" ou "DO" para garantir o cruzamento
    txt = txt.replace(" D'", " D ").replace("'", "").replace(" DO ", " D ")
    return " ".join(txt.split())

# 1. Carregar os arquivos reais
votos = pd.read_excel('Votos_Coronel.xlsx')
eleitores = pd.read_excel('Eleitores_foram.xlsx')

# 2. Criar chaves de busca padronizadas
votos['Chave'] = votos['Município'].apply(limpar_nome)
eleitores['Chave'] = eleitores['Município'].apply(limpar_nome)

# 3. Cruzar as tabelas (Merge)
df_final = pd.merge(votos, eleitores, on='Chave')

# 4. Calcular a Penetração usando o nome CORRETO da coluna: 'Comparecimento'
df_final['% Penetração'] = (df_final['Total de Votos'] / df_final['Comparecimento']) * 100

# 5. Ordenar do maior para o menor impacto
df_final = df_final.sort_values(by='% Penetração', ascending=False)

# 6. Selecionar apenas as colunas importantes e salvar
ranking = df_final[['Município_x', 'Comparecimento', 'Total de Votos', '% Penetração']]
ranking.columns = ['Município', 'Comparecimento', 'Votos Coronel', '% Penetração']

ranking.to_excel('Ranking_Penetracao_Final.xlsx', index=False)

print("✅ Sucesso! Planilha 'Ranking_Penetracao_Final.xlsx' gerada.")
print(f"Cidades processadas: {len(ranking)}")