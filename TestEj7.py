import unittest
import Ej7


class TestEj7(unittest.TestCase):
    def test_agenda(self):
        personas = {"Mateo": 4323454231, "Ivan": 4356721312,
                    "Manuel": 4356749876}
        self.assertEquals(Ej7.agenda("Mateo", personas), 4323454231)
        self.assertEquals(Ej7.agenda("Ivan", personas), 4356721312)
        self.assertEquals(Ej7.agenda("Manuel", personas), 4356749876)
        with self.assertRaises(ValueError):
            Ej7.agenda(32321, personas)

    def test_nuevo_persona(self):
        personas = {"Mateo": 4323454231, "Ivan": 4356721312,
                    "Manuel": 4356749876}
        self.assertEquals(Ej7.nueva_persona("Facundo", 4356456724,  personas),
                                           ("Facundo", 4356456724))
        self.assertEquals(Ej7.nueva_persona("Pedro", 4325342536, personas),
                                           ("Pedro", 4325342536))
        self.assertEquals(Ej7.nueva_persona("Jose", 4315462578, personas),
                                           ("Jose", 4315462578))


if __name__ == "__main__":
    unittest.main()
