import subprocess
import smtplib
from email.mime.text import MIMEText
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

# Configuration de l'alerting par email
smtp_server = 'xxxxxx'
smtp_port = 25
smtp_username = 'xxxxxx'
smtp_password = 'xxxxxx'
email_from = 'monitoring@example.com'
email_to = 'xxxxx@xxxxx'

# Définir la liste des services à surveiller
services = [
    {"name": "Service 1", "host": "http://ip_ou_url_service_1", "status": "UNKNOWN", "message": ""},
]

def check_service_status(service):
    if service["host"].startswith("http"):
        # Si l'hôte est une URL, utiliser curl pour vérifier le statut
        result = subprocess.run(["curl", "-Is", service["host"]], capture_output=True)
        if result.returncode == 0:
            output = result.stdout.decode()
            response_code = int(output.split(" ")[1])  # Obtenir le code de réponse HTTP
            if 200 <= response_code < 300:
                return "UP", output
            else:
                service["message"] = f"Code de statut HTTP : {response_code}"  # Mettre à jour le message avec le code de statut HTTP
                return "DOWN", output
        else:
            service["message"] = "Le service est inaccessible"  # Mettre à jour le message lorsque le service est inaccessible
            return "DOWN", ""


    else:
        # Sinon, utiliser ping pour vérifier le statut de l'hôte
        result = subprocess.run(["ping", "-c", "1", service["host"]], capture_output=True)
        if result.returncode == 0:
            return "UP", ""
        else:
            return "DOWN", ""

def send_alert_email(service):
    subject = f"Service indisponible : {service['name']}"
    body = f"Le service {service['name']} à l'adresse {service['host']} est indisponible."
    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = email_from
    message['To'] = email_to

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(email_from, [email_to], message.as_string())

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        host = request.form.get("host")
        if name and host:
            # Ajouter un nouvel hôte à surveiller
            services.append({"name": name, "host": host, "status": "UNKNOWN", "message": ""})
        else:
            error_message = "Veuillez remplir tous les champs du formulaire."
            return render_template("index.html", services=services, error_message=error_message)
    elif request.method == "GET" and "delete" in request.args:
        # Supprimer un hôte surveillé
        host_to_delete = request.args.get("delete")
        services[:] = [service for service in services if service["host"] != host_to_delete]

    # Mettre à jour l'état de chaque service
    for service in services:
        status, message = check_service_status(service)
        if service["status"] != status:
            service["status"] = status
            service["message"] = message
            if status == "DOWN":
                send_alert_email(service)

    return render_template("index.html", services=services)

if __name__ == "__main__":
    app.run(port=8000,debug=True)
