from flask import Blueprint, jsonify
import requests
from app.models import get_connection

bosses_bp = Blueprint('bosses', __name__)

@bosses_bp.route("/importar/bosses")
def importar_bosses():
    raw_data = requests.get("https://eldenring.fanapis.com/api/bosses?limit=100") \
                       .json() \
                       .get("data", [])

    vistos = set()
    data = []
    for boss in raw_data:
        nombre = boss.get("name")
        if nombre and nombre not in vistos:
            vistos.add(nombre)
            data.append(boss)

    conn   = get_connection()
    cursor = conn.cursor()
    cursor.execute("TRUNCATE TABLE bosses;")

    insert_sql = """
        INSERT INTO bosses
          (id, name, image, description, location, drops, healthPoints)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    for boss in data:
        cursor.execute(insert_sql, (
            boss.get("id"),
            boss.get("name"),
            boss.get("image"),
            boss.get("description"),
            boss.get("location"),
            ", ".join(boss.get("drops", [])) or None,
            boss.get("healthPoints")
        ))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({
        "mensaje":  "Jefes importados correctamente",
        "cantidad": len(data)
    })


@bosses_bp.route("/api/bosses")
def api_bosses():
    conn   = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM bosses;")
    datos = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(datos)

    return jsonify({"mensaje": "Jefes importados correctamente", "cantidad": len(data)})
