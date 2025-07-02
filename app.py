from flask import Flask, jsonify, render_template
from game import JarreGame

app = Flask(__name__)
jeu = JarreGame()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/start", methods=["GET"])
def start_game():
    jeu.reset_game()
    return jsonify({"message": "Nouvelle partie lancée", "etat": jeu.get_state()})

@app.route("/click/<int:index>", methods=["POST"])
def click(index):
    result = jeu.click_jarre(index)
    return jsonify(result)

@app.route("/state", methods=["GET"])
def state():
    return jsonify(jeu.get_state())

if __name__ == "__main__":
    app.run(debug=True)
