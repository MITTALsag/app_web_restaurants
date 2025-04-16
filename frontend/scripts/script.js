document.getElementById("loginForm").addEventListener("submit", async function(event) {
    event.preventDefault();
    await Connexion(); // Ajout de 'await' car la fonction est async
});


async function Connexion() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    try {
        const response = await fetch("/login", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({email, password})
        });

        const result = await response.json();
        
        if (result.status === "success") {
            alert("Connecté !");
            // Redirection ou traitement
        } else {
            alert(`Erreur: ${result.message}`);
        }
    } catch (error) {
        alert("Erreur réseau");
    }
}