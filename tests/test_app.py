import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_app_starts():
    """Teste se o app Flask inicializa corretamente"""
    assert app is not None

def test_home_status_code(client):
    """Teste se a rota / retorna status 200"""
    response = client.get('/')
    assert response.status_code == 200

def test_home_content(client):
    """Teste se a rota / retorna o texto esperado"""
    response = client.get('/')
    assert "Olá, mundo! Meu projeto DevOps" in response.data.decode()

def test_404_status_code(client):
    """Teste se rota inexistente retorna 404"""
    response = client.get('/nao-existe')
    assert response.status_code == 404

def test_server_config():
    """Teste se o servidor está configurado para rodar no host e porta corretos"""
    # No app.py você roda host=0.0.0.0 e port=8000
    assert app.run.__defaults__[0] == "0.0.0.0"  # host
    assert app.run.__defaults__[1] == 8000       # port
