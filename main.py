"""Interfaz de consola del sistema de tareas."""
from pathlib import Path
from tareas import GestorTareas


def main():
    try:
        gestor = GestorTareas(Path(__file__).parent / "datos" / "tareas.json")
    except (ValueError, OSError) as error:
        print(f"No se pudo abrir el archivo: {error}")
        print("Revisa datos/tareas.json antes de continuar; no se sobrescribió.")
        return 1
    while True:
        print("\n=== SISTEMA DE TAREAS ===")
        print("1. Agregar tarea\n2. Consultar tareas\n3. Completar tarea\n4. Eliminar tarea\n5. Salir")
        try:
            opcion = input("Selecciona una opción: ").strip()
            if opcion == "1":
                tarea = gestor.agregar(input("Título: "))
                print(f"Tarea registrada con ID {tarea['id']}.")
            elif opcion == "2":
                tareas = gestor.listar()
                if not tareas:
                    print("Todavía no hay tareas.")
                for tarea in tareas:
                    estado = "COMPLETADA" if tarea["completada"] else "PENDIENTE"
                    print(f"{tarea['id']}. [{estado}] {tarea['titulo']}")
            elif opcion in ("3", "4"):
                identificador = int(input("ID de la tarea: "))
                if opcion == "3":
                    gestor.completar(identificador)
                    print("Tarea completada.")
                else:
                    gestor.eliminar(identificador)
                    print("Tarea eliminada.")
            elif opcion == "5":
                print("Hasta pronto. Tus cambios están guardados.")
                return 0
            else:
                print("Elige una opción del 1 al 5.")
        except (ValueError, OSError) as error:
            print(f"No se pudo realizar la operación: {error}")
        except (EOFError, KeyboardInterrupt):
            print("\nPrograma cerrado.")
            return 0


if __name__ == "__main__":
    raise SystemExit(main())
