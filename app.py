from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Ruta principal
@app.route("/")
def home():
    return "Hola desde Flask en Docker y Railway 🚀"

# Ruta con parámetro
@app.route("/saludo/<nombre>")
def saludo(nombre):
    return jsonify({"saludo": f"Hola, {nombre} 👋"})

# Ruta POST con JSON para sumar
@app.route("/sumar", methods=["POST"])
def sumar():
    data = request.get_json()
    a = data.get("a", 0)
    b = data.get("b", 0)
    return jsonify({"resultado": a + b})

# Ejecución del servidor
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Railway asigna el puerto
    app.run(host="0.0.0.0", port=port)
