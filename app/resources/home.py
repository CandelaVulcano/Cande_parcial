from flask import Blueprint, render_template, jsonify

home_bp = Blueprint('home', __name__, template_folder='templates')

@home_bp.route('/')
def index():
    """Página principal del sistema académico"""
    return render_template('index.html')

@home_bp.route('/api/health')
def health_check():
    """Endpoint para verificar el estado de la aplicación"""
    return jsonify({
        "status": "healthy",
        "message": "Sistema Académico funcionando correctamente"
    }), 200

@home_bp.route('/dashboard')
def dashboard():
    """Dashboard principal del sistema"""
    return render_template('dashboard.html')

@home_bp.route('/api/info')
def app_info():
    """Información general de la aplicación"""
    return jsonify({
        "name": "Sistema Académico",
        "version": "1.0.0",
        "description": "Sistema de gestión académica universitaria"}),200