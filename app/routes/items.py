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
            item.get("name"),
            item.get("image"),
            item.get("description"),
            item.get("effect"),
            item.get("type")
        ))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"mensaje": "Items importados correctamente", "cantidad": len(data)})
