import subprocess
import requests
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

# Définir les informations de l'alerte
smtp_server = "smtp.example.com"
smtp_port = 587
smtp_username = "monitoring@example.com"
smtp_password = "password"
email_from = "monitoring@example.com"
email_to = "alert@example.com"

def check_service_status(host):
    if host.startswith("http"):
        # Vérifier l'état du service en effectuant une requête avec curl
        response = subprocess.run(["curl", "-Is", host], capture_output=True)
        if response.returncode == 0:
            if "200 OK" in response.stdout.decode():
                return "UP"
            else:
                return "DOWN"
        else:
            return "DOWN"
    else:
        # Vérifier l'état du service en effectuant une requête de ping
        result = subprocess.run(["ping", "-c", "1", host], capture_output=True)
        if result.returncode == 0:
            return "UP"
        else:
            return "DOWN"

def send_alert(service):
    subject = f"Service {service['name']} est indisponible"
    body = f"Le service {service['name']} ({service['host']}) est indisponible."
    # Envoyer l'alerte par e-mail
    # Code pour envoyer l'e-mail via le serveur SMTP configuré

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        host = request.form.get("host")
        status = check_service_status(host)
        if status == "DOWN":
            send_alert({"name": "service", "host": host})
        return render_template("index.html", services=[{"name": "service", "host": host, "status": status}])

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
