import unittest
import tkinter as tk
from tkinter import messagebox
from unittest.mock import patch

# IMPORTANT: Import your actual application classes here.
# Assuming your index.py has a LoginApp and InventoryApp class.
# from index import LoginApp, InventoryApp 

class TestInventorySystemGUI(unittest.TestCase):
    
    def setUp(self):
        """This runs BEFORE every single test. It sets up the Tkinter window."""
        self.root = tk.Tk()
        
        # Initialize your app here. We'll use a hypothetical LoginApp as the starting point.
        # self.app = LoginApp(self.root) 
        
        # Update the idle tasks so Tkinter actually renders the widgets in the background
        self.root.update_idletasks()

    def tearDown(self):
        """This runs AFTER every single test. It cleans up the window."""
        self.root.destroy()

    # ---------------------------------------------------------
    # Scenario 1: Login Tests
    # ---------------------------------------------------------
    
    @patch('tkinter.messagebox.showerror')
    def test_invalid_login(self, mock_showerror):
        """TC2: Negative Test - Try logging in with wrong credentials."""
        # 1. Simulate typing into the entry fields
        # self.app.username_entry.insert(0, "wrong_user")
        # self.app.password_entry.insert(0, "wrong_pass")
        
        # 2. Simulate clicking the login button
        # self.app.login_button.invoke()
        
        # 3. Assert the expected result: An error message box should pop up
        # mock_showerror.assert_called_with("Error", "Invalid credentials")

    def test_valid_login(self):
        """TC1: Positive Test - Log in successfully."""
        # 1. Simulate entering valid details
        # self.app.username_entry.insert(0, "admin")
        # self.app.password_entry.insert(0, "password123")
        
        # 2. Simulate clicking the login button
        # self.app.login_button.invoke()
        
        # 3. Assert the expected result: The app transitions to the Dashboard
        # Check if a specific dashboard widget now exists or if the view changed
        # self.assertTrue(hasattr(self.app, 'dashboard_frame')) 

    # ---------------------------------------------------------
    # Scenario 2: Add Product Tests
    # ---------------------------------------------------------

    @patch('tkinter.messagebox.showinfo')
    def test_add_valid_product(self, mock_showinfo):
        """TC3: Positive Test - Add a new product."""
        # Note: In a real test, you might need to mock the database connection 
        # or use a local SQLite test database like inventory_mvp.db so you don't mess up production data.
        
        # Bypass login for this test if your app allows, or call a method to switch to the Inventory view
        # inventory_app = InventoryApp(self.root) 
        
        # 1. Simulate typing in product details
        # inventory_app.sku_entry.insert(0, "SKU-999")
        # inventory_app.name_entry.insert(0, "Test Widget")
        # inventory_app.cost_entry.insert(0, "5.00")
        # inventory_app.price_entry.insert(0, "10.00")
        # inventory_app.min_stock_entry.insert(0, "20")
        
        # 2. Simulate clicking "Save Product"
        # inventory_app.save_product_button.invoke()
        
        # 3. Assert that a success message was shown
        # mock_showinfo.assert_called_with("Success", "Product added successfully")

    # ---------------------------------------------------------
    # Scenario 3: Stock Transactions
    # ---------------------------------------------------------

    @patch('tkinter.messagebox.showerror')
    def test_negative_stock_prevention(self, mock_showerror):
        """TC6: Negative Test - Attempt to sell more stock than is available."""
        # inventory_app = InventoryApp(self.root) 
        
        # 1. Simulate trying to record a 'Stock Out' of 500 items for a product that only has 10
        # inventory_app.transaction_sku_entry.insert(0, "SKU-001")
        # inventory_app.transaction_qty_entry.insert(0, "500")
        
        # Select "OUT" from a dropdown/radio button (depends on your UI design)
        # inventory_app.transaction_type_var.set("OUT")
        
        # 2. Click submit
        # inventory_app.record_transaction_button.invoke()
        
        # 3. Assert the system caught it and threw an error rather than creating negative stock
        # mock_showerror.assert_called_with("Error", "Stock Not Available")

if __name__ == '__main__':
    unittest.main()