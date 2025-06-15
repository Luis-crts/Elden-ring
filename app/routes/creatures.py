from flask import Blueprint, jsonify
import requests
from app.models import get_connection

creatures_bp = Blueprint('creatures', __name__)

@creatures_bp.route("/importar/creatures")
def importar_creatures():
    url = "https://eldenring.fanapis.com/api/creatures?limit=100"
    response = requests.get(url)
    data = response.json().get("data", [])

    conn = get_connection()
    cursor = conn.cursor()

    for creature in data:
        cursor.execute("""
            INSERT IGNORE INTO creatures (id, name, image, description, location, drops)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            creature.get("id"),
            creature.get("name"),
            creature.get("image"),
            creature.get("description"),
            creature.get("location"),
            ", ".join(creature.get("drops", [])) if creature.get("drops") else None
        ))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"mensaje": "Criaturas importadas correctamente", "cantidad": len(data)})

@creatures_bp.route("/api/creatures")
def api_creatures():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM creatures")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(data)
