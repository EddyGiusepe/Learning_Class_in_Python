# Imagem base do Python 3.10
FROM python:3.10

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia apenas o arquivo de requirements primeiro para aproveitar o cache do Docker
# Se os requirements não mudarem, essa camada será reutilizada
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copia todo o resto do código fonte para o container
# Esta etapa é feita depois dos requirements para melhor utilização do cache
COPY . .

# Informa que o container irá escutar na porta 80
EXPOSE 80

# Comando para executar a aplicação
# Usando python diretamente para executar main.py
CMD ["python", "main.py"]