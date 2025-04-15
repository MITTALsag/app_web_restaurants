from flask import Flask, render_template, request, jsonify

app = Flask(
    __name__,
    template_folder="../frontend",                 # Dossier des templates
    static_folder="../frontend/styles",            # Dossier des fichiers statiques (CSS/JS/images)
)



@app.route("/")
def home():
    return render_template("index.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if (request.method == 'POST'):
        try:
            # Récupère les données JSON envoyées par le frontend
            data = request.get_json()
            email = data.get('email')
            password = data.get('password')
            
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500
    else:
        return render_template("Login.html")
    


if __name__ == "__main__":
    app.run(debug=True)