# Crea un'API RESTful utilizzando Flask. L'API dovrebbe fornire ricette alimentari in formato JSON.
# (1) inizia con il memorizzando i seguenti dati in una variabile recipes. Si tratta di un dizionario che contiene diverse ricette.
# (2) La tua API dovrebbe servire qualsiasi ricetta in formato JSON all'indirizzo: http://127.0.0.1:5000/recipes/{id} dove "id" è l'ID della ricetta fornito dall'utente.
# (3) Visitando la homepage http://127.0.0.1:5000 dovrebbe essere visualizzato un semplice testo "Homepage"
from flask import Flask

recipes = {
    1: {'id': 1, 'title': 'Spaghetti Carbonara', 'ingredients': ['spaghetti', 'eggs', 'pecorino cheese', 'guanciale'], 'instructions': 'Cook pasta, fry guanciale, mix with eggs and cheese, and combine with pasta.'},
    2: {'id': 2, 'title': 'Tomato Soup', 'ingredients': ['tomato', 'water', 'salt'], 'instructions': 'Boil all together until mushy, blend, and serve.'},
    3: {'id': 3, 'title': 'Grilled Cheese Sandwich', 'ingredients': ['bread', 'cheese', 'butter'], 'instructions': 'Butter bread, place cheese between slices, grill until golden.'}
}

app = Flask(__name__)


@app.route('/')
def index():
    return "Homepage"


@app.route('/recipes/<int:id>', methods=["GET"])
def get_recipes(id):
    recipe = recipes.get(id)
    if recipe:
        return recipe
    else:
        return {'message': 'recipe not found'}, 404


app.run(debug=True)
