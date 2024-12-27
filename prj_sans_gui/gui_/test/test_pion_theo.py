import unittest
from pion import Pion
#differents tests unitaires pour la class pion
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

    def test_reculer(self):
        pion = Pion("Pion 1")
        pion.deplacer(5)
        pion.reculer(3)
        self.assertEqual(pion.position, 2)

    def test_reculer_sous_zero(self):
        pion = Pion("Pion 2")
        pion.reculer(1)
        self.assertEqual(pion.position, 0)

    def test_est_sur_case(self):
        pion = Pion("Pion 2")
        pion.deplacer(5)
        self.assertTrue(pion.est_sur_case(5))
        self.assertFalse(pion.est_sur_case(4))

if __name__ == "__main__":
    unittest.main()