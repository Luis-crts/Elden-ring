from flask import Blueprint, jsonify
import requests
from app.models import get_connection

npcs_bp = Blueprint('npcs', __name__)

@npcs_bp.route("/importar/npcs")
def importar_npcs():
    url = "https://eldenring.fanapis.com/api/npcs?limit=100"
    response = requests.get(url)
    data = response.json().get("data", [])

    conn = get_connection()
    cursor = conn.cursor()

    for npc in data:
        cursor.execute("""
            INSERT IGNORE INTO npcs (id, name, image, description, quote, location)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            npc.get("id"),
            npc.get("name"),
            npc.get("image"),
            npc.get("description") if npc.get("description") != "Sin descripción disponible." else None,
            npc.get("quote"),
            npc.get("location")
        ))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"mensaje": "NPCs importados correctamente", "cantidad": len(data)})

@npcs_bp.route("/api/npcs")
def api_npcs():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM npcs")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(data)
