import unittest
from pion import Pion

class TestPion(unittest.TestCase):
    def test_initialisation(self):
        pion = Pion("Pion 1")
        self.assertEqual(pion.nom, "Pion 1")
        self.assertEqual(pion.position, 0)

    def test_deplacer(self):
        pion = Pion("Pion 1")
        pion.deplacer(5)
        self.assertEqual(pion.position, 5)
        pion.deplacer(3)
        self.assertEqual(pion.position, 8)

    def test_deplacer_en_negatif(self):
        pion = Pion("Pion 1")
        with self.assertRaises(ValueError):
            pion.deplacer(-3)

    def test_reculer(self):
        pion = Pion("Pion 1")
        pion.deplacer(5)
        pion.reculer(3)
        self.assertEqual(pion.position, 2)

    def test_reculer_moins_de_zero(self):
        pion = Pion("Pion 1")
        pion.reculer(1)
        self.assertEqual(pion.position, 0)

    def test_reculer_a_zero(self):
        pion = Pion("Pion 1")
        pion.deplacer(5)
        pion.reculer(5)
        self.assertEqual(pion.position, 0)

    def test_sur_case(self):
        pion = Pion("Pion 2")
        pion.deplacer(5)
        self.assertTrue(pion.est_sur_case(5))
        self.assertFalse(pion.est_sur_case(4))

    def test_sur_case_limites(self):
        pion = Pion("Pion 2")
        pion.deplacer(100)
        self.assertTrue(pion.est_sur_case(100))
        self.assertFalse(pion.est_sur_case(99))

    def test_grands_deplacements(self):
        pion = Pion("Pion 2")
        pion.deplacer(1_000_000)
        self.assertEqual(pion.position, 1_000_000)
        pion.reculer(500_000)
        self.assertEqual(pion.position, 500_000)

if __name__ == "__main__":
    unittest.main()
