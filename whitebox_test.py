import pytest
from unittest.mock import patch
from backend.service import InventoryService


@pytest.fixture
def mock_service():
    # Patch DatabaseManager where it is used in backend.service
    with patch('backend.service.DatabaseManager') as MockDB:
        service = InventoryService()
        # Grab the active mocked instance assigned during initialization
        mock_db = service.db 
        return service, mock_db


# ✅ ADD PRODUCT
def test_add_product_valid(mock_service):
    service, mock_db = mock_service
    mock_db.execute_query.return_value = True

    success, msg = service.add_product("SKU001", "Widget A", 5.0, 10.0, 20)

    assert success is True
    assert "Product added" in msg


def test_add_product_invalid(mock_service):
    service, _ = mock_service

    # Testing with missing SKU
    success, msg = service.add_product("", "Widget", 5.0, 10.0, 5)

    assert success is False
    assert "SKU and Name are required" in msg


# ✅ LOGIN
def test_login_valid(mock_service):
    service, mock_db = mock_service
    # Database fetchone returns a tuple
    mock_db.fetch_one.return_value = ("Admin",)

    success, role = service.login_user("admin", "1234")

    assert success is True
    assert role == "Admin"


def test_login_invalid(mock_service):
    service, mock_db = mock_service
    # Simulate user not found in DB
    mock_db.fetch_one.return_value = None

    success, role = service.login_user("admin", "wrong")

    assert success is False
    assert role is None


# ✅ TRANSACTION
def test_transaction_in(mock_service):
    service, mock_db = mock_service

    # process_transaction calls execute_query 3 times sequentially. 
    # We use side_effect to provide the 3 expected returns.
    mock_db.execute_query.side_effect = [
        [(1, 10, "Item", 5)],  # 1. Select Product (returns list of tuples)
        True,                  # 2. Update Stock
        True                   # 3. Insert Transaction Record
    ]

    success, msg = service.process_transaction("SKU001", "IN", 5)

    assert success is True
    assert "Transaction recorded" in msg


def test_transaction_out_insufficient(mock_service):
    service, mock_db = mock_service

    # Simulate finding the product, but current stock is only 5
    mock_db.execute_query.return_value = [(1, 5, "Item", 2)]

    success, msg = service.process_transaction("SKU001", "OUT", 10)

    assert success is False
    assert "Insufficient stock" in msg


# ✅ DELETE USER
def test_delete_user_self(mock_service):
    service, _ = mock_service

    # Trying to delete the currently logged-in user
    success, msg = service.delete_user("admin", "admin")

    assert success is False
    assert "cannot delete yourself" in msg


def test_delete_user_other(mock_service):
    service, mock_db = mock_service
    mock_db.execute_query.return_value = True
    
    success, msg = service.delete_user("employee", "admin")
    
    assert success is True
    assert "User deleted" in msg