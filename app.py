from flask import Flask,request,render_template
from model import create_model,preprocess_data
from tensorflow.keras.preprocessing.text import Tokenizer
from joblib import load

app = Flask(__name__)
new_model = create_model()
tokenizer = load('tokenizer.pkl')

@app.route('/')
def home():
    return render_template("index.html",positive =0 , negative =0)

@app.route('/predict',methods=['POST'])
def second():
    text = [x for x in request.form.values()]
    processed_data = preprocess_data(text,tokenizer)

    results = new_model.predict(processed_data)
    print(results)
    if results > .75:
        positive = results
        negative = 1 - positive
    else:
        positive = results
        negative = 1 - positive
    return render_template('index.html',positive = positive, negative = negative)

if __name__ == '__main__':
    app.run(debug=True)


