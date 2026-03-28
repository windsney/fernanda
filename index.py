import pandas as pd

# Carregar o arquivo enviado
file_path = 'votacao_candidato_munzona_2022_MT.csv'
df = pd.read_csv(file_path, sep=';', encoding='latin-1')

# Filtrar pela Coronel Fernanda (Nome de Urna ou Número 2222)
# Nota: Ajustei para o nome que costuma aparecer no TSE
filtro = df[df['NM_URNA_CANDIDATO'] == 'CORONEL FERNANDA']

# Agrupar por município e somar os votos
resultado = filtro.groupby('NM_MUNICIPIO')['QT_VOTOS_NOMINAIS'].sum().reset_index()

# Renomear colunas para ficar organizado
resultado.columns = ['Município', 'Total de Votos']

# Salvar em Excel
resultado.to_excel('Votos_Coronel_Fernanda_2022.xlsx', index=False)

print("Arquivo 'Votos_Coronel_Fernanda_2022.xlsx' gerado com sucesso!")