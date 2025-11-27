from flask import Flask, render_template, request, jsonify
import markovify
import random
from gtts import gTTS
import os

app = Flask(__name__)


with open("oracle.txt", encoding="utf-8") as f:
    text = f.read()
model = markovify.Text(text, state_size=2)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/prophecy', methods=['POST'])
def prophecy():
    question = request.json.get('question', '')
    
    prop = model.make_sentence(tries=200)
    
    if prop:
        tts = gTTS(text=prop, lang='fr', slow=True)
        tts.save("static/prophecy.mp3")
    
    return jsonify({'prophecy': prop})

if __name__ == '__main__':
    app.run(debug=True)