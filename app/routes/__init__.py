from app.routes.bosses import bosses_bp
from app.routes.items import items_bp
from app.routes.creatures import creatures_bp
from app.routes.npcs import npcs_bp
from app.routes.home import home_bp
from app.routes.auth import auth_bp

def register_routes(app):
    app.register_blueprint(bosses_bp)
    app.register_blueprint(items_bp)
    app.register_blueprint(creatures_bp)
    app.register_blueprint(npcs_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp)
