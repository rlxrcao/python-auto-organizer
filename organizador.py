import os
import shutil

# 1. Defina a pasta que você quer organizar (Ex: sua pasta de Downloads)
# Troque pelo seu caminho real. No Windows geralmente é C:/Users/SeuNome/Downloads
caminho = "C:/Users/Rafael/Downloads_Teste" 

# 2. Defina os tipos de arquivos e suas pastas destino
extensoes = {
    ".pdf": "Documentos",
    ".docx": "Documentos",
    ".jpg": "Imagens",
    ".png": "Imagens",
    ".exe": "Instaladores",
    ".zip": "Compactados"
}

# 3. O código que faz a mágica
for arquivo in os.listdir(caminho):
    nome, extensao = os.path.splitext(arquivo)
    
    # Se a extensão estiver na nossa lista...
    if extensao in extensoes:
        pasta_destino = extensoes[extensao]
        
        # Cria a pasta se ela não existir
        caminho_final = os.path.join(caminho, pasta_destino)
        if not os.path.exists(caminho_final):
            os.makedirs(caminho_final)
            
        # Move o arquivo
        shutil.move(os.path.join(caminho, arquivo), os.path.join(caminho_final, arquivo))
        print(f"Movido: {arquivo} -> {pasta_destino}")

print("Organização concluída!")