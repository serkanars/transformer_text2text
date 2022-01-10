import requests
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from flask import Flask, request
import pandas as pd

tokenizer_tr_en = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-tr-en")
model_tr_en = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-tr-en")

tokenizer_en_tr = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-tatoeba-en-tr")
model_en_tr = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-tatoeba-en-tr")

app = Flask(__name__)


@app.route("/", methods = ['GET','POST'])
def predict():

    if request.method == "POST":
        data = request.get_json()

        print(data)

        if data['source'] == "en-tr":

            text = data['text']
            tokenized_text = tokenizer_en_tr.prepare_seq2seq_batch([text], return_tensors="pt")

            translation = model_en_tr.generate(**tokenized_text)
            translated_text = tokenizer_en_tr.batch_decode(translation[0], skip_special_tokens=True)
            del translated_text[-1], translated_text[0]

            return {'çeviri' : " ".join(translated_text)}
        
        elif data['source'] == "tr-en":

            text = data['text']
            tokenized_text = tokenizer_tr_en.prepare_seq2seq_batch([text], return_tensors="pt")

            translation = model_tr_en.generate(**tokenized_text)
            translated_text = tokenizer_tr_en.batch_decode(translation[0], skip_special_tokens=True)
            del translated_text[-1], translated_text[0]

            return {'çeviri' : " ".join(translated_text)}
        else:
            return {"Error":"error"}



if __name__  == "__main__":
    app.run(debug = True) 