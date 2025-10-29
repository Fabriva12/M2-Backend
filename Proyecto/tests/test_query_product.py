import pytest
from sqlalchemy import insert, select, update
from unittest.mock import MagicMock
from queries.product_queries_proyect import Product_DB  


@pytest.fixture
def mock_engine(monkeypatch):
    """Mock del engine y su contexto de conexión."""
    mock_conn = MagicMock()
    mock_engine = MagicMock()
    mock_engine.begin.return_value.__enter__.return_value = mock_conn
    return mock_engine


@pytest.fixture
def product_db(mock_engine):
    """Instancia de Product_DB con el engine mockeado."""
    db = Product_DB()
    db.engine = mock_engine
    return db


# --- TEST INSERT ---
def test_insert_product_success(product_db):
    product_db.insert_product("Laptop", "SKU123", 1200, 10)
    conn = product_db.engine.begin.return_value.__enter__.return_value
    conn.execute.assert_called_once()  # se ejecutó una consulta


# --- TEST GET ---
def test_get_product_success(product_db, monkeypatch):
    mock_result = {"ID": 1, "name": "Laptop", "price": 1200, "stock": 10, "SKU": "SKU123"}

    # Simular el resultado del execute().mappings().first()
    conn = product_db.engine.begin.return_value.__enter__.return_value
    execute_mock = MagicMock()
    execute_mock.mappings.return_value.first.return_value = mock_result
    conn.execute.return_value = execute_mock

    result = product_db.get_product(1)
    assert result == mock_result
    conn.execute.assert_called_once()


# --- TEST DELETE ---
def test_delete_product_success(product_db):
    product_db.delete_product(1)
    conn = product_db.engine.begin.return_value.__enter__.return_value
    conn.execute.assert_called_once()


# --- TEST UPDATE (éxito) ---
def test_update_product_success(product_db):
    conn = product_db.engine.begin.return_value.__enter__.return_value

    update_data = {"name": "Nuevo nombre", "price": 999}
    result = product_db.update_product(1, update_data)
    assert result is None  # el método no devuelve nada en éxito
    conn.execute.assert_called_once()


# --- TEST UPDATE (campos no válidos) ---
def test_update_product_invalid_fields(product_db):
    result = product_db.update_product(1, {"invalid_field": "value"})
    assert result is False  # no actualiza nada
    conn = product_db.engine.begin.return_value.__enter__.return_value
    conn.execute.assert_not_called()


# --- TEST UPDATE (lanza excepción) ---
def test_update_product_exception(product_db, monkeypatch):
    conn = product_db.engine.begin.return_value.__enter__.return_value
    conn.execute.side_effect = Exception("DB error")

    # No debería lanzar excepción, solo imprimir el error
    result = product_db.update_product(1, {"name": "Nuevo"})
    assert result is None