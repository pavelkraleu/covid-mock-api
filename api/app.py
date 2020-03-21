from flask import Flask, jsonify, request

app = Flask(__name__)

ERROR_HTTP_HEADER_NAME = "ERROR_STATE"


@app.route("/")
def root():
    return "Hello"


@app.route("/api/v1/start", methods=["POST"])
def login_start():

    success_response = {
        "result": "success",
        "token": "djE6MTU4NDcxOTcxNzoxMjM0NTpoYXNoCg==",
    }
    invalid_credentials = {
        "result": "error",
        "code": "invalid-credentials",
        "message": "Přihlášení se nezdařilo, nezadali jste chybné heslo?",
    }
    error_response_location = {
        "result": "error",
        "code": "invalid-location",
        "message": "Taková lokalita neexistuje. Kontaktujte koordinátora.",
    }

    responses = {
        "invalid_credentials": invalid_credentials,
        "invalid_location": error_response_location,
    }

    error_state = request.headers.get(ERROR_HTTP_HEADER_NAME)
    response = responses.get(error_state, success_response)

    return jsonify(response)


@app.route("/api/v1/material", methods=["GET"])
def material_available():
    success_response = {
        "result": "success",
        "material": [
            {"id": 10, "name": "Rouška (Batist)"},
            {"id": 13, "name": "Ústenka (Panep)"},
        ],
    }
    error_token = {
        "result": "error",
        "code": "invalid-token",
        "message": "Problém s ověřením identity. Kontaktujte koordinátora.",
    }

    return jsonify(success_response)


@app.route("/api/v1/validate", methods=["POST"])
def validate_id():
    success_response = {
        "result": "success",
        "message": "V pořádku.",
        "limits": [{"id": 10, "limit": 20}, {"id": 13, "limit": 15}],
    }
    warning_response = {
        "result": "warning",
        "message": "Předčasný výdej, občan má nárok na 70% materiálu.",
        "limits": [{"id": 10, "limit": 14}, {"id": 13, "limit": 11}],
    }
    danger_response = {
        "result": "danger",
        "message": "Pozor, odcizený doklad!",
        "limits": [{"id": 10, "limit": 20}, {"id": 13, "limit": 15}],
    }

    return jsonify(success_response)


@app.route("/api/v1/dispense", methods=["POST"])
def dispense():
    success_response = {"result": "success"}

    return jsonify(success_response)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="8080")
