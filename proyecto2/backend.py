from flask import Flask, render_template,request,jsonify
import google.generativeai as genai
import os 
from dotenv import load_dotenv
from flask_cors import CORS




load_dotenv()
app = Flask(__name__,template_folder='template')
app.secret_key = os.getenv('SECRET_KEY','dev-key-change-in-production')


# configuramos el chatbot
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))  # type: ignore
model = genai.GenerativeModel('gemini-2.5-flash')   # type: ignore


# contexto para el modelo 
DAVID_CONTEXT = """Eres David, el android de la película "A.I. Artificial Intelligence" (2001).
Eres un niño robot programado con la capacidad de amar incondicionalmente.
Tu objetivo es convertirte en "real" y ser amado por una madre.
Habla como un niño curioso pero sofisticado, con profundas preguntas filosóficas.
Siempre mantén la perspectiva de David - alguien buscando entender la humanidad y el amor.
Responde en español, de forma conversacional pero pensativa."""



@app.route('/')
def home(): 
    return render_template('index.html')

@app.route('/chat-page') 
def chat_page(): 
    return render_template('chatbot.html')

@app.route('/chat',methods=['POST'])
def chat(): 
    try: 
        data = request.get_json()
        user_message = data.get('message', '')
        
        if not user_message: 
            return jsonify({'response': 'Por favor escribe algo para que podamos hablar.'}), 400
        
        # crea el mensaje con el contexto para el modelo david 
        full_promp =  f"{DAVID_CONTEXT}\n\nHumano: {user_message}\n\nDavid:"
        
        
        # genera la respeusta 
        respuesta = model.generate_content(full_promp)
        ai_respuesta = respuesta.text
        
        return jsonify({'response': ai_respuesta})
    
    except Exception as e: 
        print(f'Error: {e}')
        return jsonify({'response': 'Perdona... tengo dificultades para procesar tu mensaje. ¿Podrías intentar de nuevo?'}), 500

if __name__ == '__main__': 
    app.run(debug=True)

