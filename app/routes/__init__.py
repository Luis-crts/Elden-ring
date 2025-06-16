from .bosses    import bosses_bp
from .items     import items_bp
from .creatures import creatures_bp
from .npcs      import npcs_bp
from .home      import home_bp
from .auth      import auth_bp

def register_routes(app):

    app.register_blueprint(bosses_bp)
    app.register_blueprint(items_bp)
    app.register_blueprint(creatures_bp)
    app.register_blueprint(npcs_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp)
