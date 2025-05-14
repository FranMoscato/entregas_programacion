import unittest
import semana_02 as s2

class Test_invertir_lista(unittest.TestCase):
    def test_listas_untipo(self):
        self.assertListEqual(s2.invertir_lista([1,2,3,4,5]),[5,4,3,2,1])
        self.assertListEqual(s2.invertir_lista([11,14,8,4]),[4,8,14,11])
        self.assertListEqual(s2.invertir_lista(['a','b','c']),['c','b','a'])
        self.assertListEqual(s2.invertir_lista(['e','d','c','c','b','a']),['a','b','c','c','d','e'])

    def test_listas_variostipos(self):
        self.assertListEqual(s2.invertir_lista([1,2,3,4,5,'a','b','c']),['c','b','a',5,4,3,2,1])
        self.assertListEqual(s2.invertir_lista(['gato',13,['mani','almendra'],8.9,'perro']),['perro',8.9,['mani','almendra'],13,'gato'])

    def test_listas_largos(self):
        self.assertListEqual(s2.invertir_lista([]),[])
        self.assertListEqual(s2.invertir_lista(['gato']),['gato'])
        self.assertListEqual(s2.invertir_lista([1,2,3,4,5,6,7,8,9,10]),[10,9,8,7,6,5,4,3,2,1])
        self.assertListEqual(s2.invertir_lista([i for i in range(10000)]),[9999-i for i in range(10000)])

class Test_collatz(unittest.TestCase):
    def test_pares(self):
        self.assertEqual(s2.collatz(2),1)
        self.assertEqual(s2.collatz(4),2)
        self.assertEqual(s2.collatz(8),3)

    
    def test_impares(self):
        self.assertEqual(s2.collatz(1),0)
        self.assertEqual(s2.collatz(3),7)
        self.assertEqual(s2.collatz(7),16)

    def test_grandes(self):
        self.assertEqual(s2.collatz(27),111)
        self.assertEqual(s2.collatz(1000),111)
        self.assertEqual(s2.collatz(16854),159)

class Test_contar_def(unittest.TestCase):
    def test_def_unicas(self):
        self.assertDictEqual(s2.contar_definiciones({"gato":['animal'],"perro":['animal']}), {"gato":1,"perro":1})
        self.assertDictEqual(s2.contar_definiciones({"empanada":['alimento']}), {"empanada":1})

    def test_def_varias(self):
        self.assertDictEqual(s2.contar_definiciones({"gato":['animal','felino','mamifero'],"perro":['animal','can']}), {"gato":3,"perro":2})
        self.assertDictEqual(s2.contar_definiciones({"empanada":['alimento','relleno','tradicional','docena'],"cepillo":['instrumento','de dientes','de barrer']}), {"empanada":4,"cepillo":3})

    def test_casos_extremos(self):
        self.assertDictEqual(s2.contar_definiciones({"gato":[]}), {"gato":0})
        self.assertDictEqual(s2.contar_definiciones({f"c{pos}": [i for i in range(valor)] for pos, valor in enumerate(range(100))}),{f"c{pos}":int(valor) for pos, valor in enumerate(range(100))})

class Test_canitdad_claves(unittest.TestCase):
    def test_ninguna_clave(self):
        self.assertEqual(s2.cantidad_de_claves_letra({"gato":['animal'],"perro":['animal']},"c"), 0)
        self.assertEqual(s2.cantidad_de_claves_letra({"empanada":['alimento']},"a"), 0)

    def test_pocas_claves(self):
        self.assertEqual(s2.cantidad_de_claves_letra({"gato":['animal'],"perro":['animal'],"pinguino":['animal'],"pajaro":['animal']},"p"), 3)
        self.assertEqual(s2.cantidad_de_claves_letra({"empanada":['alimento']},"e"), 1)
    
    def test_muchas_claves(self):
        self.assertEqual(s2.cantidad_de_claves_letra({"gato": ["animal"],"perro": ["animal"],"pinguino": ["animal"],"pajaro": ["animal"],"pantera": ["animal"],"pulpo": ["animal"],"puma": ["animal"],"peces": ["animal"],"pavo": ["animal"],"perico": ["animal"],"pitón": ["animal"]},"p"), 10)
        self.assertEqual(s2.cantidad_de_claves_letra({f"c{pos}": [i for i in range(valor)] for pos, valor in enumerate(range(100))},"c"), 100)

class Test_propagar(unittest.TestCase):
    def test_propagacion_der(self):
        self.assertListEqual(s2.propagar([1,0,0,0,0]),[1,1,1,1,1])
        self.assertListEqual(s2.propagar([1,0,-1,0,0]),[1,1,-1,0,0])
        self.assertListEqual(s2.propagar([0,0,-1,1,0]),[0,0,-1,1,1])

    def test_propagacion_izq(self):
        self.assertListEqual(s2.propagar([0,0,0,0,1]),[1,1,1,1,1])
        self.assertListEqual(s2.propagar([0,1,-1,0,0]),[1,1,-1,0,0])
        self.assertListEqual(s2.propagar([0,0,-1,0,1]),[0,0,-1,1,1])

    def test_propagacion_todos_iguales(self):
        self.assertListEqual(s2.propagar([0,0,0,0,0]),[0,0,0,0,0])
        self.assertListEqual(s2.propagar([1,1,1,1,1]),[1,1,1,1,1])
        self.assertListEqual(s2.propagar([-1,-1,-1,-1,-1]),[-1,-1,-1,-1,-1])

    def test_propagacion_extremos(self):
        self.assertListEqual(s2.propagar([0,0,-1,0,1,-1,0,0]),[0,0,-1,1,1,-1,0,0]) #extremos que no se queman
        self.assertListEqual(s2.propagar([1,0,-1,0,1,-1,0,0]),[1,1,-1,1,1,-1,0,0]) #un extremo incendiado
        self.assertListEqual(s2.propagar([0,0,-1,0,1,-1,0,1]),[0,0,-1,1,1,-1,1,1]) #un extremo incendiado
        self.assertListEqual(s2.propagar([-1,0,0,-1,1,-1,0,-1]),[-1,0,0,-1,1,-1,0,-1]) #extremos ya quemados
        self.assertListEqual(s2.propagar([0,-1,0,0,1,-1,0,-1]),[0,-1,1,1,1,-1,0,-1]) #ya quemado en segunda posicion
    
if __name__=='__main__':
    unittest.main()
