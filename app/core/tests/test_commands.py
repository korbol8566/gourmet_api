"""Test costom Django management commands"""

from email.policy import default
from unittest.mock import patch
from psycopg2 import OperationalError as Psycopg2OpError

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase

@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    """Test command"""
    
    def test_Wait_for_db_ready(self, patched_check):
        """Tests waiting for db if db ready"""
        patched_check.return_value =True
        
        call_command('wait_for_db')
        
        patched_check.assert_called_once_with(databases=['default'])
    
    @patch('time.sleep')    
    def test_wait_for_db_delayed(self, patched_sleep, patched_check):
        """Test waiting for db when getting operationalError"""
        patched_check.side_effect = [Psycopg2OpError] * 2 + \
            [OperationalError] * 3 + [True]
        
        call_command('wait_for_db')
            
        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=['default'])