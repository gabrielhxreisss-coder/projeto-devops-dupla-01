from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def inicio():
    return jsonify({
        "mensagem": "Olá da dupla 01!",
        "projeto": "DevOps na Nuvem"
    })

@app.route("/saude")
def saude():
    return jsonify({
        "status": "ok"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)