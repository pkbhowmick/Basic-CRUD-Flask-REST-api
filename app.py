from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/hello')
def index():
    return jsonify({"response":"Hello!"})


if __name__=="__main__":
    app.run(debug=True)

