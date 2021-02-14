from flask import Flask,request,render_template
from model import create_model

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict',methods=['POST'])
def second():
    text = [x for x in request.form.values()]
    print(text[0])
    return render_template('chart.html',toxic=100,hate=50,threat=20,Neutral=0)

if __name__ == '__main__':
    app.run(debug=True)


