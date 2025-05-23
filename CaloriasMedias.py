import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv
import os

#Carregar as variáveis 
load_dotenv()
api_key = os.getenv("API_KEY")

#Configurar a chave api 
genai.configure(api_key=api_key)

#Selecionar as pastas com as imagens
image_folder = "imagens"

#Selecionar todos os arquivos da pasta com .jpg, .jpeg e .png
image_files = [
    os.path.join(image_folder, file)
    for file in os.listdir(image_folder)
    if file.lower().endswith((".jpg", ".jpeg", ".png"))
]

#Abre as imagens uma por uma
image = [Image.open(file) for file in image_files]

#Criar o modelo Gemini 
model = genai.GenerativeModel("gemini-2.5-flash-preview-05-20")

#Prompt para obter as calorias médias dos alimentos 
prompt = (
    "Observe a imagem e liste os alimentos identificáveis."
    "Para da alimento que foi identificado forneça uma estimativa aproximada de calorias médias."
    "Exemplo: \n\n"
    "- Arroz branco: 200 kcal por xícara \n\n"
    "Responda de forma clara e objetiva com um somatório das calorias totais ao final de foto por foto."
)

#Enviar imagens e o prompt
response = model.generate_content([
    prompt,
    *image 
])

#Exibir a resposta
print(response.text)
