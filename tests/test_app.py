import sys
import os
import pytest

# adiciona a raiz do projeto no sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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
    """Teste se o app está configurado para rodar em modo de teste"""
    # garante que a app pode ser colocada em modo TESTING
    app.config['TESTING'] = True
    assert app.config['TESTING'] is True