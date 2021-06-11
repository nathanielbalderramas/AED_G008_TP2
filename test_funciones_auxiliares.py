import unittest
import funciones_auxiliares as f

class TestFunciones(unittest.TestCase):
    def test_calcular_puntaje(self):
        self.assertEqual(f.calcular_puntaje((1, 2, 3), True), 3)
        self.assertEqual(f.calcular_puntaje((1, 2, 3), False), -1)
        self.assertEqual(f.calcular_puntaje((4, 4, 4), True), 8)
        self.assertEqual(f.calcular_puntaje((4, 4, 4), False), -4)
        self.assertEqual(f.calcular_puntaje((1, 2, 2), True), -1)
        self.assertEqual(f.calcular_puntaje((1, 2, 2), False), 2)
        self.assertEqual(f.calcular_puntaje((3, 3, 3), True), -3)
        self.assertEqual(f.calcular_puntaje((3, 3, 3), False), 6)

    def test_check_acierto(self):
        self.assertEqual(f.check_acierto((1, 2, 3), True), True)
        self.assertEqual(f.check_acierto((1, 2, 3), False), False)
        self.assertEqual(f.check_acierto((3, 3, 3), True), False)
        self.assertEqual(f.check_acierto((3, 3, 3), False), True)

    def test_check_acierto_critico(self):
        self.assertEqual(f.check_acierto_critico((1, 2, 3), True), False)
        self.assertEqual(f.check_acierto_critico((1, 2, 3), False), False)
        self.assertEqual(f.check_acierto_critico((3, 3, 3), True), False)
        self.assertEqual(f.check_acierto_critico((3, 3, 3), False), True)


if __name__ == "__main__":
    unittest.main()
