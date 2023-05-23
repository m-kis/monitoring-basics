import subprocess
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

# Définir la liste des services à surveiller
services = [
    {"name": "service", "host": "ip_ou_url_service"},
    #  {"name": "Service 2", "host": "ip_ou_url_service_2"},
    # Ajouter d'autres services à surveiller
]

def check_service_status(service):
    # Vérifier l'état du service en effectuant une requête de ping ou autre méthode
    result = subprocess.run(["ping", "-c", "1", service["host"]], capture_output=True)
    if result.returncode == 0:
        return "UP"
    else:
        return "DOWN"

@app.route("/")
def index():
    # Récupérer l'état de chaque service et mettre à jour la liste des services
    for service in services:
        service["status"] = check_service_status(service)
    # Rendre le template HTML avec les données mises à jour
    return render_template("index.html", services=services)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
