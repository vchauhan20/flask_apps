from flask import Flask,request,render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict',methods=['POST'])
def second():
    return render_template('chart.html',toxic=100,hate=50,threat=20,Neutral=0)

if __name__ == '__main__':
    app.run(debug=True)


