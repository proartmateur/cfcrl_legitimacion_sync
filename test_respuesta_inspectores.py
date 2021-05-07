from unittest import TestCase

from RespuestaInspector import RespuestaInspector


class TryTesting(TestCase):

    def test_checha_igualdad_is_equal_method(self):
        respuesta1 = RespuestaInspector(
            "1",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL"
        )

        respuesta2 = RespuestaInspector(
            "1",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL"
        )

        self.assertTrue(respuesta1.is_equal(respuesta2))

    def test_checha_igualdad_nativo(self):
        respuesta1 = RespuestaInspector(
            "1",
            None,
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL"
        )

        respuesta2 = RespuestaInspector(
            "1",
            None,
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL"
        )

        self.assertTrue(respuesta1 == respuesta2)

    def test_checha_igualdad_nativo_2(self):
        respuesta1 = RespuestaInspector(
            1,
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL"
        )

        respuesta2 = RespuestaInspector(
            1,
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL"
        )

        self.assertTrue(respuesta1 == respuesta2)

    def test_checha_no_igualdad_is_equal_method(self):
        respuesta1 = RespuestaInspector(
            "1",
            "HOLA",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL"
        )

        respuesta2 = RespuestaInspector(
            "1",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL2"
        )

        self.assertFalse(respuesta1.is_equal(respuesta2))

    def test_checha_no_igualdad_nativo(self):
        respuesta1 = RespuestaInspector(
            "1",
            "HOLITA",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL"
        )

        respuesta2 = RespuestaInspector(
            "1",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL"
        )

        self.assertFalse(respuesta1 == respuesta2)

    def test_busca_diferencias(self):
        respuesta1 = RespuestaInspector(
            "1",
            None,
            "COCA",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL"
        )

        respuesta2 = RespuestaInspector(
            "1",
            None,
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "WOW",
            "NULL",
            "NULL",
            "NULL",
            "NULL",
            "NULL"
        )
        dif = respuesta1.diferencias(respuesta2)
        self.assertEqual(2, len(dif))
        self.assertFalse(respuesta1 == respuesta2)
