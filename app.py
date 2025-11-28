from flask import Flask, render_template, request, jsonify
import markovify
import random
from gtts import gTTS
import os
import subprocess

app = Flask(__name__)

with open("oracle.txt", encoding="utf-8") as f:
    text = f.read()

model = markovify.Text(text, state_size=2)

def make_delirious_voice(input_path, output_path):
    """Transforme la voix en quelque chose de délirant avec sox"""
    
    # Effets sox pour une voix délirante et mystique
    effects = [
        'sox', input_path, output_path,
        
        # Ralentir légèrement et baisser le pitch (voix plus grave)
        'tempo', '0.85',
        'pitch', '-200',
        
        # Ajouter reverb (écho de temple)
        'reverb', '50', '50', '100',
        
        # Ajouter un léger chorus (effet de voix multiples)
        'chorus', '0.7', '0.9', '55', '0.4', '0.25', '2', '-t',
        
        # Tremolo (variation de volume, effet de transe)
        'tremolo', '0.5', '80',
        
        # Égalisation pour rendre plus caverneux
        'equalizer', '1000', '1q', '-6',
        'equalizer', '3000', '1q', '-8',
        
        # Normaliser 
        'norm', '-3'
    ]
    
    try:
        subprocess.run(effects, check=True, capture_output=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Erreur sox: {e}")
    
        if os.path.exists(input_path):
            os.replace(input_path, output_path)
        return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prophecy', methods=['POST'])
def prophecy():
    question = request.json.get('question', '')
    
    # Générer la prophétie
    prop = model.make_sentence(tries=200)
    
    if prop:
        temp_path = "static/prophecy_temp.mp3"
        final_path = "static/prophecy.mp3"
        

        tts = gTTS(text=prop, lang='fr', slow=True)
        tts.save(temp_path)
        

        success = make_delirious_voice(temp_path, final_path)
        

        if os.path.exists(temp_path):
            try:
                os.remove(temp_path)
            except:
                pass
        
        return jsonify({'prophecy': prop})
    
    return jsonify({'prophecy': 'L\'Oracle reste silencieux...'})

if __name__ == '__main__':
    app.run(debug=True)