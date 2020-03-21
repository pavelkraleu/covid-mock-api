from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def root():
    return "Hello"


@app.route("/api/v1/start", methods=["POST"])
def login_start():
    success_response = {
        "result": "success",
        "token": "djE6MTU4NDcxOTcxNzoxMjM0NTpoYXNoCg==",
    }
    error_response = {
        "result": "error",
        "code": "invalid-credentials",
        "message": "Přihlášení se nezdařilo, nezadali jste chybné heslo?",
    }
    error_response_location = {
        "result": "error",
        "code": "invalid-location",
        "message": "Taková lokalita neexistuje. Kontaktujte koordinátora.",
    }

    return jsonify(success_response)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="8080")
