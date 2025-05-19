from flask import Flask, render_template, request, jsonify
from datetime import datetime
from empleado import Empleado
from gestor_cierre_inspeccion import GestorCierreInspeccion
from orden_de_inspeccion import OrdenDeInspeccion
from motivo_tipo import MotivoTipo

app = Flask(__name__)

empleado = Empleado("Juan", "Pérez", "juan@example.com")
gestor = GestorCierreInspeccion(empleado, datetime.now(), "juan@example.com", None)
gestor.ordenes.append(OrdenDeInspeccion("ORD001", datetime.now()))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/confirmar", methods=["POST"])
def confirmar():
    data = request.json
    gestor.ingresar_observacion_cierre(data["observacion"])
    gestor.tomar_seleccion_motivo(MotivoTipo(data["motivo"]))
    gestor.solicitar_confirmacion_cierre(data["ordenId"])
    gestor.confirmar_cierre(data["ordenId"])
    return jsonify({"message": "Cierre confirmado correctamente"})

if __name__ == "__main__":
    app.run(debug=True)