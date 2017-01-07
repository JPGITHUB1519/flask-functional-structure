from flask import Flask

app = Flask(__name__)
from .views import admin, home, control_panel

app.register_blueprint(admin.admin_blueprint, url_prefix='/admin')
app.register_blueprint(home.home_blueprint)
app.register_blueprint(control_panel.control_panel_blueprint , url_prefix='/control')