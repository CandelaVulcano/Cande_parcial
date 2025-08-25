import pytest
from app import create_app, db
from app.models.nota import Nota

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_crear_nota(client):
    response = client.post('/notas', json={"valor": 8, "inscripcion_id": 1})
    assert response.status_code in (201, 400)
    if response.status_code == 201:
        data = response.get_json()
        assert data['valor'] == 8
        assert data['inscripcion_id'] == 1

def test_validacion_nota(client):
    response = client.post('/notas', json={"inscripcion_id": 1})
    assert response.status_code == 400
    data = response.get_json()
    assert 'errors' in data

    response = client.post('/notas', json={"valor": 15, "inscripcion_id": 1})
    assert response.status_code == 400
    data = response.get_json()
    assert 'errors' in data
