from flask import Blueprint, jsonify
import requests
from app.models import get_connection


bosses_bp = Blueprint('bosses', __name__)

@bosses_bp.route("/importar/bosses")
def importar_bosses():
    url = "https://eldenring.fanapis.com/api/bosses?limit=100"
    response = requests.get(url)
    data = response.json().get("data", [])

    conn = get_connection()
    cursor = conn.cursor()

    for boss in data:
        cursor.execute("""
            INSERT IGNORE INTO bosses (id, name, image, description, location, drops, healthPoints)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            boss.get("id"),
            boss.get("name"),
            boss.get("image"),
            boss.get("description"),
            boss.get("location"),
            ", ".join(boss.get("drops", [])) if boss.get("drops") else None,
            boss.get("healthPoints")
        ))

    conn.commit()
    cursor.close()
    conn.close()

@bosses_bp.route("/api/bosses")
def api_bosses():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM bosses")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(data)
    

    return jsonify({"mensaje": "Jefes importados correctamente", "cantidad": len(data)})
