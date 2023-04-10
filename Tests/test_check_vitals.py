import io
from unittest import TestCase
from unittest.mock import patch

from character import check_vitals


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_ready(self, mock_output):
        check_vitals()
        self.assertEqual(mock_output.getvalue(), "")
