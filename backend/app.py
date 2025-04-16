from flask import Flask, render_template, request, jsonify

app = Flask(
    __name__,
    template_folder="../frontend",                 # Dossier des templates
    static_folder="../frontend",            # Dossier des fichiers statiques (CSS/JS/images)
)



@app.route("/")
def home():
    return render_template("index.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if (request.method == 'POST'):
        if not request.is_json:  # <-- Ajoutez cette vérification
            return jsonify({"status": "error", "message": "Content-Type must be application/json"}), 415
        try:
            
            # Récupère les données JSON envoyées par le frontend
            data = request.get_json()
            email = data.get('email')
            password = data.get('password')

            print(data, email, password)

            return render_template("Login.html"), 200
            
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500
    else:
        return render_template("Login.html"), 200
    


if __name__ == "__main__":
    app.run(debug=True)