import streamlit as st

# Fonction pour effectuer une opération mathématique (exemple : multiplication)
def f1(x, y, z, selected_options):
    result = (x * y) + z
    if 'Square' in selected_options:
        result *= result
    return result

# Fonction pour effectuer une autre opération mathématique (exemple : soustraction)
def f2(x, y, z, selected_options):
    result = (x - y) * z
    if 'Cube' in selected_options:
        result *= result * result
    return result

# Fonction principale pour l'interface utilisateur
def main():
    st.title("Calculateur Mathématique")

    # Demander trois entrées entières
    x = st.number_input("Entrez le premier nombre entier", value=1, step=1)
    y = st.number_input("Entrez le deuxième nombre entier", value=1, step=1)
    z = st.number_input("Entrez le troisième nombre entier", value=1, step=1)

    # Demander une entrée avec choix multiples
    options = ['Square', 'Cube']
    selected_options = st.multiselect("Sélectionnez les opérations", options)

    # Appeler les fonctions f1 et f2
    result_f1 = f1(x, y, z, selected_options)
    result_f2 = f2(x, y, z, selected_options)

    # Afficher les résultats
    st.header("Résultats:")
    st.write("Résultat de f1:", result_f1)
    st.write("Résultat de f2:", result_f2)

# Appeler la fonction principale
if __name__ == "__main__":
    main()