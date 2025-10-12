# A.I. Artificial Intelligence - Film Analysis & Interactive Chatbot

Presentación interactiva sobre la película "A.I. Artificial Intelligence" (2001) con chatbot impulsado por IA.

## Requisitos previos

- Python 3.8 o superior
- Una API Key de Google Generative AI (gratis en [Google AI Studio](https://aistudio.google.com/apikey))

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/PROYECTO2.git
cd PROYECTO2
```

### 2. Crear archivo `.env`

```bash
cp .env.example .env
```

Edita `.env` y agrega tu API Key:

```
GOOGLE_API_KEY=tu_clave_api_aqui
SECRET_KEY=tu_clave_secreta_aqui
FLASK_ENV=development
FLASK_DEBUG=True
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación

```bash
python backend.py
```

Abre `http://localhost:5000` en tu navegador.

## Uso

1. Scrollea por la presentación
2. Al llegar al final, se redirige automáticamente al chatbot
3. Chatea con David

## Estructura

```
PROYECTO2/
├── backend.py
├── requirements.txt
├── .env.example
├── template/
│   ├── index.html
│   └── chatbot.html
└── static/img_2/
```

## Obtener API Key

1. Ve a [Google AI Studio](https://aistudio.google.com/apikey)
2. Clic en "Get API key"
3. Copia la clave en tu `.env`