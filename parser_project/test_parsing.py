import unittest
from unittest.mock import patch, MagicMock
from main import Parsing

class TestParsing(unittest.TestCase):
    
    @patch("requests.get")
    def test_init_success(self, mock_get):
        mock_get.return_value.text = "<html></html>"
        parser = Parsing()
        self.assertIsNotNone(parser.html)
    
    @patch("requests.get")
    def test_init_failure(self, mock_get):
        mock_get.side_effect = Exception("Request failed")
        with self.assertRaises(Exception):
            Parsing()
    
    @patch("requests.get")
    def test_parse(self, mock_get):
        mock_html = '''
        <div class="brochure-thumb">
            <strong>Test Brochure</strong>
            <img src="test_thumbnail.jpg" class="brochure-image" />
            <img class="lazyloadLogo" alt="Test Shop Logo" />
            <small class="hidden-sm">von 01.01.2024 bis 10.01.2024</small>
        </div>
        '''
        
        mock_get.return_value.text = mock_html
        parser = Parsing()
        parser.parse()
        
        self.assertEqual(len(parser.brochures), 1)
        self.assertEqual(parser.brochures[0]["title"], "Test Brochure")
        self.assertEqual(parser.brochures[0]["thumbnail"], "test_thumbnail.jpg")
        self.assertEqual(parser.brochures[0]["shop_name"], "Test Shop")
        self.assertEqual(parser.brochures[0]["valid_from"], "von 01.01.2024")
        self.assertEqual(parser.brochures[0]["valid_to"], "10.01.2024")

    @patch("builtins.open", new_callable=unittest.mock.mock_open)
    @patch("json.dump")
    def test_save(self, mock_json_dump, mock_open):
        parser = Parsing()
        parser.brochures = [{"title": "Test Brochure", "thumbnail": "test.jpg", "shop_name": "Test Shop", "valid_from": "01.01.2024", "valid_to": "10.01.2024", "parsed_time": "2024-03-14 12:00:00"}]
        parser.save()
        
        mock_open.assert_called_once()
        mock_json_dump.assert_called_once()
        
if __name__ == "__main__":
    unittest.main()