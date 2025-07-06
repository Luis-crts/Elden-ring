from flask import Blueprint, jsonify
import requests
from app.models import get_connection

items_bp = Blueprint('items', __name__)

@items_bp.route("/importar/items")
def importar_items():
    url = "https://eldenring.fanapis.com/api/items?limit=100"
    response = requests.get(url)
    data = response.json().get("data", [])

    conn = get_connection()
    cursor = conn.cursor()

    for item in data:
        cursor.execute("""
            INSERT IGNORE INTO items (id, name, image, description, effect, type)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            item.get("id"),
            item.get("name") or "Desconocido",
            item.get("image") or "Desconocido",
            item.get("description") or "",
            item.get("effect") or "",
            item.get("type") or ""
        ))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"mensaje": "Items importados correctamente", "cantidad": len(data)})

@items_bp.route("/api/items")
def api_items():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM items")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(data)
