import tempfile
import unittest
from pathlib import Path
from tareas import GestorTareas


class PruebasTareas(unittest.TestCase):
    def setUp(self):
        self.directorio = tempfile.TemporaryDirectory()
        self.addCleanup(self.directorio.cleanup)
        self.archivo = Path(self.directorio.name) / "tareas.json"
        self.gestor = GestorTareas(self.archivo)

    def test_agregar_tarea_pendiente(self):
        tarea = self.gestor.agregar("Estudiar Git")
        self.assertEqual(tarea["titulo"], "Estudiar Git")
        self.assertFalse(tarea["completada"])
        self.assertEqual(len(self.gestor.listar()), 1)

    def test_rechazar_titulo_vacio(self):
        with self.assertRaises(ValueError):
            self.gestor.agregar("   ")
        self.assertEqual(self.gestor.listar(), [])

    def test_completar_tarea(self):
        tarea = self.gestor.agregar("Hacer entrega")
        self.gestor.completar(tarea["id"])
        self.assertTrue(self.gestor.listar()[0]["completada"])

    def test_eliminar_tarea(self):
        tarea = self.gestor.agregar("Temporal")
        self.gestor.eliminar(tarea["id"])
        self.assertEqual(self.gestor.listar(), [])

    def test_id_inexistente(self):
        for accion in (self.gestor.completar, self.gestor.eliminar):
            with self.assertRaises(ValueError):
                accion(99)

    def test_persistencia(self):
        tarea = self.gestor.agregar("Preparar exposición ñ")
        self.gestor.completar(tarea["id"])
        otro = GestorTareas(self.archivo)
        self.assertEqual(otro.listar(), self.gestor.listar())

    def test_ids_sin_duplicados_al_eliminar(self):
        self.gestor.agregar("Uno")
        self.gestor.agregar("Dos")
        self.gestor.eliminar(1)
        nueva = self.gestor.agregar("Tres")
        self.assertEqual(nueva["id"], 3)

    def test_archivo_corrupto(self):
        self.archivo.write_text("archivo inválido", encoding="utf-8")
        with self.assertRaises(ValueError):
            GestorTareas(self.archivo)


if __name__ == "__main__":
    unittest.main()
