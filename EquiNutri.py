import streamlit as st


# fonction pour agréger les valeurs de toutes les courses
def f0(data, liste_de_courses):
    to_use = data.loc[data.id.isin(liste_de_courses),['protein_100g', 'glucides_100g', 'lipides_100g','serving_portion']]
    return to_use.protein * to_use.serving_portion, to_use.glucides * to_use.serving_portion, to_use.lipides * to_use.serving_portion

# Fonction pour effectuer calculer l'energie restante
def f1(protein, glucides, lipides, typologie):
    result = protein * 12 + glucides * 29 + lipides * 29 
    if 'Fat' in typologie:
        result -= 40
    elif 'Thin' in typologie:
        result += 20
    return result

# Fonction pour choisir les éléments de courses 
def f2(result, typologie):
    # calculate the amount of each cat to provide
    list_of_elements = trained_K_means(result, typologie)
    return list_of_elements

def f3(IMC):
    if IMC < 16.5:
        typologie = "Maigreur extrême – dénutrition"
    elif IMC < 18.5:
        typologie = "Maigreur"
    elif IMC < 25:
        typologie = "Corpulence normale"
    elif IMC < 30:
        typologie = "Surpoids ou pré-obésité"
    elif IMC < 35:
        typologie = "Obésité modérée (classe I)"
    elif IMC < 40:
        typologie = "Obésité sévère (classe II)"
    else:
        typologie = "Obésité morbide (classe III)"
    return typologie

# Fonction principale pour l'interface utilisateur
def main():
    st.title("Je termine mes courses")

    # Demander trois entrées entières pour definir typologie
    x = st.number_input("Entrez votre poids en kg", value=1, step=1)
    y = st.number_input("Entrez votre taille en metre", value=1, step=1)
    z = st.number_input("Entrez votre age", value=1, step=1)
    # Attribuer typologie
    IMC = y / (X**2)
    typologie = f3(IMC)


    # Proposer les élements de courses (propre à chaque magasin)
    options = ['id1', 'id2']
    selected_options = st.multiselect("Sélectionnez les articles de courses", options)
    # calculer apport NRJ
    protein, glucides, lipides = f0(data=,liste_de_courses=selected_options)


    # calculer l'energie restante
    result = f1(protein, glucides, lipides, typologie)

    # proposer suggestion de courses
    suggestions = f2(result,typologie)

    # Afficher les résultats
    st.header("Votre liste de courses:")
    st.write("suivant vos conditions", typologie)
    st.write("et le contenue de votre liste de course", protein.sum, glucides.sum, lipides.sum)
    st.write("Nous vous suggérons d'ajouter", suggestions)

# Appeler la fonction principale
if __name__ == "__main__":
    main()