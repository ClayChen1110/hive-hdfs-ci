"""Tests for main module."""

import unittest
from unittest.mock import patch, MagicMock
from src.python.main import check_database_exists


class TestMain(unittest.TestCase):
    """Test cases for main function."""

    @patch('src.python.main.hive.Connection')
    def test_check_database_exists_found(self, mock_connection):
        """Test when database exists."""
        # Mock cursor and connection
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [('default',), ('product',), ('test',)]
        mock_conn = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_connection.return_value = mock_conn
        
        # Test
        result = check_database_exists("product")
        
        # Assertions
        self.assertTrue(result)
        mock_cursor.execute.assert_called_once_with("SHOW DATABASES")
        
    @patch('src.python.main.hive.Connection')
    def test_check_database_exists_not_found(self, mock_connection):
        """Test when database does not exist."""
        # Mock cursor and connection
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [('default',), ('test',)]
        mock_conn = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_connection.return_value = mock_conn
        
        # Test
        result = check_database_exists("product")
        
        # Assertions
        self.assertFalse(result)
        
    @patch('src.python.main.hive.Connection')
    def test_check_database_exists_connection_error(self, mock_connection):
        """Test connection error handling."""
        # Mock connection to raise exception
        mock_connection.side_effect = Exception("Connection failed")
        
        # Test
        result = check_database_exists("product")
        
        # Assertions
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
