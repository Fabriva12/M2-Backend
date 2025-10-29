import pytest
from flask import Flask
from unittest.mock import patch
from endpoints.user_endpoint_proyect import user_bp

# --- Creamos la app de testing ---
app = Flask(__name__)
app.register_blueprint(user_bp)


# --- Fixture para inyectar DB y JWT mocks ---
@pytest.fixture(autouse=True)
def mock_dependencies(monkeypatch):
    """
    Mock de db_manager y jwt_manager globales dentro del módulo.
    Los mocks validan datos y roles.
    """

    # --- Mock insert_user ---
    def mock_insert_user(email, password, role):
        if not email or not password or not role:
            raise ValueError("Datos incompletos")
        return True

    # --- Mock get_user ---
    def mock_get_user(email, password):
        if email == "admin@gmail.com" and password == "1234":
            return {"ID": 1, "role": "admin"}
        if email == "user@gmail.com" and password == "1234":
            return {"ID": 2, "role": "user"}
        return None

    # --- Mock delete_user ---
    def mock_delete_user(user_id):
        return True

    # --- Mock JWT ---
    def mock_encode(data):
        return "fake_token_123"

    def mock_decode(token):
        if token == "valid_admin_token":
            return {"id": 1, "role": "admin"}
        if token == "valid_user_token":
            return {"id": 2, "role": "user"}
        return None

    # --- Mock token_required: inyecta decoded automáticamente ---
    def mock_token_required():
        def decorator(f):
            def wrapper(*args, **kwargs):
                if "decoded" not in kwargs:
                    kwargs["decoded"] = {"id": 1, "role": "admin"}
                return f(*args, **kwargs)
            return wrapper
        return decorator

    from endpoints import user_endpoint_proyect as mod
    monkeypatch.setattr(mod.db_manager, "insert_user", mock_insert_user)
    monkeypatch.setattr(mod.db_manager, "get_user", mock_get_user)
    monkeypatch.setattr(mod.db_manager, "delete_user", mock_delete_user)
    monkeypatch.setattr(mod.jwt_manager, "encode", mock_encode)
    monkeypatch.setattr(mod.jwt_manager, "decode", mock_decode)
    monkeypatch.setattr(mod, "token_required", mock_token_required)


# --- TEST REGISTER ---
def test_register_success():
    client = app.test_client()
    response = client.post('/register', json={
        "email": "test@gmail.com", "password": "1234", "role": "user"
    })
    assert response.status_code == 200
    assert response.get_json() == "usuario registrado exitosamente"


def test_register_missing_fields():
    client = app.test_client()
    response = client.post('/register', json={})
    assert response.status_code == 400
    assert response.get_json() == {"error": "datos incorrectos ingrese email, password y role"}


# --- TEST LOGIN ---
def test_login_success():
    client = app.test_client()
    response = client.post('/login', json={
        "email": "admin@gmail.com", "password": "1234"
    })
    assert response.status_code == 200
    assert response.get_json()["token"] == "fake_token_123"


def test_login_user_not_registered():
    client = app.test_client()
    response = client.post('/login', json={
        "email": "noexiste@gmail.com", "password": "1234"
    })
    assert response.status_code == 401
    assert response.get_json() == {"error": "Usuario no registrado"}


def test_login_incomplete_data():
    client = app.test_client()
    response = client.post('/login', json={"email": ""})
    assert response.status_code == 400
    assert response.get_json() == {"error": "datos incorrectos ingrese email y password"}


# --- TEST DELETE USER ---


def test_delete_missing_id():
    client = app.test_client()
    headers = {"Authorization": "Bearer valid_admin_token"}
    response = client.delete('/delete', json={}, headers=headers)
    assert response.status_code == 403


def test_delete_not_admin():
    client = app.test_client()
    headers = {"Authorization": "Bearer valid_user_token"}
    response = client.delete('/delete', json={"ID": 3}, headers=headers)
    assert response.status_code == 403