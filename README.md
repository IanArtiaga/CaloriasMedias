# CaloriasMedias 🍽️📷

Neste projeto foi utilizo o modelo **Gemini 2.5 Flash** da Google, para analisar imagens contendo alimentos e estimar a quantidade média de calorias por alimento presente em cada foto.

## 🔧 Tecnologias Utilizadas

- Python 3
- Gemini API (via `google-generativeai`)
- Pillow (`PIL`)
- dotenv (para a API)

## 📂 Organização do Projeto

```
├── CaloriasMedias.py   # Script principal que envia imagens e recebe calorias
├── .env                # Arquivo com a chave da API 
├── README.md           # Este arquivo
├── requirements.txt    # Dependências do projeto
└── imagens/            # Pasta com as imagens dos alimentos
```

## 🚀 Como Rodar

1. **Clone o repositório:**

```bash
git clone https://github.com/IanArtiaga/CaloriasMedias.git
cd CaloriasMedias
```

2. **Crie e edite o arquivo .env:**

```ini
API_KEY=sua-chave-aqui
```

3. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

4. **Adicione suas imagens na pasta (opicional)**

```
Já possuem imagens anexadas, porém podem ser adicionadas mais imagens
```

5. **Rode o script:**

```bash
python main.py
```

## 🖼️ Como Funciona

O script carrega várias imagens, envia para o Gemini com um prompt específico e recebe uma resposta com:

* Lista de alimentos identificados

* Estimativa de calorias por porção

* Somatório final por imagem

## 👍 Decisões tomadas

* Foi utilizada a biblioteca `dotenv` como forma de segurança para proteger a API

* Está presente a pasta `imagens` com todas as fotos presentes

* É escolhido o modelo `gemini-2.5-flash-preview-05-20`, por ser mais rápido e adequado para entrada de imagens

* Um prompt para enviar ao LLM de forma descritiva para guiar e realizar as tarefas de identificar e estimar as calorias

* Envia o script com o prompt e as imagens de uma só vez para o modelo

* Ao final é gerado uma resposta contendo:
  
  - Lista de alimentos identificados por imagem
    
  - Estimativa de calorias por alimento
    
  - Somatório de calorias por imagem
