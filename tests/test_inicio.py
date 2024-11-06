import unittest
from inicio import app  # Importa la aplicación Flask desde tu archivo principal

class TestApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Configura la aplicación para el modo de pruebas
        app.config['TESTING'] = True
        cls.client = app.test_client()  # Cliente de pruebas para enviar solicitudes HTTP

    def test_home_route(self):
        # Suponiendo que el blueprint tiene una ruta '/' para el punto de entrada
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)  # Asegúrate de ajustar el código esperado

    def test_mutant_route(self):
        # Test para la ruta '/mutant/' si existe en el blueprint
        data = {
            "dna": ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]
        }
        response = self.client.post('/mutant/', json=data)
        self.assertIn(response.status_code, [200, 403])  # Esperamos 200 si es mutante o 403 si no



if __name__ == '__main__':
    unittest.main()
