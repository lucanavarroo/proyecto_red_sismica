from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from datetime import datetime, timedelta
import random

from gestorCierreInspeccion import GestorCierreInspeccion
from ordenDeInspeccion import OrdenDeInspeccion
from estado import Estado

app = Flask(__name__)
app.secret_key = "clave_secreta_para_sesiones"

# Datos de usuarios simulados
usuarios = {
    "juan": "1234",
    "ana": "abcd"
}

# Instanciamos un gestor (esto debería ir a un archivo separado si crece)
gestor = GestorCierreInspeccion(
    empleadoLogueado="Juan Pérez",
    fechaActual=datetime.now(),
    mail="juan@empresa.com",
    sesionActual="SESION123"
)

# Cargamos una orden simulada completamente realizada
orden_simulada = OrdenDeInspeccion(
    numeroOrden="123",
    fechaInicio=datetime.now(),
    estado= Estado("Completamente Realizada",)
)
gestor.ordenes.append(orden_simulada)

# --- Rutas de la app ---

@app.route("/")
def login():
    print("Mostrando login.html")
    if session.get("usuario"):
        return redirect(url_for("index"))
    return render_template("login.html")


@app.route("/autenticar", methods=["POST"])
def autenticar():
    usuario = request.form.get("usuario")
    contrasena = request.form.get("contrasena")
    if usuarios.get(usuario) == contrasena:
        session["usuario"] = usuario
        return redirect(url_for("index"))
    else:
        return render_template("login.html", error="Usuario o contraseña incorrectos")

@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("login"))

@app.route("/index")
def index():
    if not session.get("usuario"):
        return redirect(url_for("login"))
    return render_template("index.html", usuario=session["usuario"])

@app.route("/confirmar", methods=["POST"])
def confirmar():
    if not session.get("usuario"):
        return jsonify({"error": "No autorizado"}), 401
    
    data = request.get_json()
    orden_id = data.get("orden_id")
    observacion = data.get("observacion")
    motivos = data.get("motivos")  # Lista de pares (descripcion, comentario)

    orden = gestor.buscar_orden(orden_id)
    if not orden:
        return jsonify({"error": "Orden no encontrada"}), 404
    
    gestor.ingresarObservacionCierre(observacion)
    gestor.tomarSeleccionMotivos(motivos)
    gestor.confirmarCierre(orden_id)

    return jsonify({"mensaje": f"Cierre de orden {orden_id} solicitado."}), 200

@app.route("/cerrar_orden")
def cerrar_orden():
    if not session.get("usuario"):
        return redirect(url_for("login"))
    
    # Generar 10 órdenes aleatorias con fecha_fin
    ordenes = []
    baseFecha = datetime.now()
    for i in range(10):
        dias = random.randint(1, 100)
        fechaFin = baseFecha - timedelta(days=dias)
        orden = OrdenDeInspeccion(
            numeroOrden=str(1000 + i),
            fechaInicio=fechaFin - timedelta(days=random.randint(1, 10)),
            fechaFin=fechaFin,
            estado="Completamente Realizada"
        )
        # Agregamos un id único para el select
        orden.id = f"{i+1}"
        ordenes.append(orden)
    
    # Ordenar por fecha_fin descendente (más reciente primero)
    ordenes.sort(key=lambda o: o.fechaFin, reverse=True)
    
    return render_template(
        "cerrar_orden.html",
        usuario=session["usuario"],
        ordenes=ordenes
    )

if __name__ == "__main__":
    app.run(debug=True)
