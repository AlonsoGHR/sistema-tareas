"""Lógica de tareas y persistencia JSON, sin dependencias externas."""
import json
from pathlib import Path


class GestorTareas:
    def __init__(self, archivo):
        self.archivo = Path(archivo)
        self.tareas = []
        if self.archivo.exists():
            datos = json.loads(self.archivo.read_text(encoding="utf-8"))
            if not isinstance(datos, list) or any(
                not isinstance(t, dict)
                or not isinstance(t.get("id"), int)
                or not isinstance(t.get("titulo"), str)
                or not isinstance(t.get("completada"), bool)
                for t in datos
            ):
                raise ValueError("El archivo de tareas tiene un formato inválido.")
            self.tareas = datos

    def guardar(self):
        self.archivo.parent.mkdir(parents=True, exist_ok=True)
        temporal = self.archivo.with_suffix(".tmp")
        temporal.write_text(
            json.dumps(self.tareas, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )
        temporal.replace(self.archivo)

    def agregar(self, titulo):
        titulo = titulo.strip()
        if not titulo:
            raise ValueError("El título no puede estar vacío.")

        tarea = {
            "id": max((t["id"] for t in self.tareas), default=0) + 1,
            "titulo": titulo,
            "completada": False
        }

        self.tareas.append(tarea)
        self.guardar()
        return tarea.copy()

    def listar(self):
        return [t.copy() for t in self.tareas]

    def completar(self, identificador):
        tarea = self._buscar(identificador)
        tarea["completada"] = True
        self.guardar()

    def eliminar(self, identificador):
        tarea = self._buscar(identificador)
        self.tareas.remove(tarea)
        self.guardar()

    def _buscar(self, identificador):
        for tarea in self.tareas:
            if tarea["id"] == identificador:
                return tarea
        raise ValueError("No existe una tarea con ese ID.")