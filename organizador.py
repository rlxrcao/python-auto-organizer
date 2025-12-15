import os
import shutil

# Pega o local onde este script está salvo
caminho = os.getcwd() 

print(f"Organizando a pasta: {caminho}")

# Dicionário de extensões
extensoes = {
    ".pdf": "Documentos",
    ".docx": "Documentos",
    ".xlsx": "Planilhas",
    ".jpg": "Imagens",
    ".png": "Imagens",
    ".txt": "Textos"
}

# Varre todos os arquivos da pasta
for arquivo in os.listdir(caminho):
    nome, extensao = os.path.splitext(arquivo)
    
    # Ignora o próprio script para não se mover
    if arquivo == "organizador.py":
        continue

    # Se a extensão for conhecida...
    if extensao in extensoes:
        pasta_destino = extensoes[extensao]
        caminho_final = os.path.join(caminho, pasta_destino)
        
        # Cria a pasta se não existir
        if not os.path.exists(caminho_final):
            os.makedirs(caminho_final)
            print(f"Criando pasta: {pasta_destino}")
            
        # Move o arquivo
        shutil.move(os.path.join(caminho, arquivo), os.path.join(caminho_final, arquivo))
        print(f"Movido: {arquivo} -> {pasta_destino}")

print("✅ Tudo organizado com sucesso!")

