async function Connexion() {
    const emailInput = document.getElementById("email") as HTMLInputElement;
    const passwordInput = document.getElementById("password") as HTMLInputElement;

    const email = emailInput.value.trim();
    const password = passwordInput.value; // <-- Supprimez les parenthèses : .value au lieu de .value()

    if (!email || !password) {
        alert("Veuillez remplir tous les champs."); // <-- Affichez le message à l'utilisateur
        return;
    }

    try {
        const response = await fetch("http://127.0.0.1:5000/login", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ email, password })
        });

        const data = await response.json();

        if (data.status === "success") {
            alert("Connexion réussie !");
            // Redirigez ou faites une action post-connexion
        } else {
            alert(data.message); // Affiche l'erreur retournée par le serveur
        }

    } catch(error) {
        alert("Erreur de connexion au serveur.");
        console.error("Erreur :", error);
    }
}