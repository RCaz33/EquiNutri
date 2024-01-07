from flask import Flask, render_template, request
from utils import OMS_interpret

app = Flask(__name__)

@app.route("/", methods=['GET'])
def accueil():
    return render_template("accueil.html", message_home="Bienvenue sur la page d'accueil !")

@app.route("/profile", methods=['POST','GET'])
def profil():
    name = request.form['name']
    poids = int(request.form['poids'])
    taille = float(request.form['taille'])
    age = request.form['age']
    processed_text = name.capitalize()
    IMC = round(poids / (taille**2),1)
    status_ = OMS_interpret(IMC)
    return render_template("profil.html", name=processed_text, poids=poids, taille=taille, age=age, \
                           IMC=IMC, OMS_interpret = status_)

if __name__ == "__main__":
    app.run(debug=True)
