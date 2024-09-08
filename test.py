import unittest
from bascula import Bascula, Usuario

class TestBascula(unittest.TestCase):

    def setUp(self):
        self.usuario = Usuario(id=1, nombre="Juan", altura=1.75)
        self.bascula = Bascula()

    def test_registrar_medicion(self):
        resultado = self.bascula.registrar_medicion(self.usuario, 70)
        self.assertTrue(resultado)
        self.assertEqual(len(self.bascula.mediciones), 1)

    def test_calcular_masa_corporal(self):
        masa_corporal = self.bascula.calcular_masa_corporal(self.usuario)
        self.assertEqual(masa_corporal, 16)

    
     

if __name__ == '__main__':
    unittest.main()