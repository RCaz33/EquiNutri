from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def accueil():
    return render_template("accueil.html", message_home="Bienvenue sur la page d'accueil !")

@app.route("/next", methods=['POST','GET'])
def profil():
    name = request.form['username']
    poids = request.form['poids']
    taille = request.form['taille']
    age = request.form['age']
    #processed_text = name.upper()
    return render_template("profil.html", name=name, poids=poids, taille=taille, age=age)

if __name__ == "__main__":
    app.run(debug=True)
