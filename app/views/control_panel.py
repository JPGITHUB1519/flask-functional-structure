from flask import Blueprint, render_template

control_panel_blueprint = Blueprint('control_panel', __name__, template_folder='templates')

@control_panel_blueprint .route('/')
def control_panel():
	return render_template('control_panel/control_panel.html')