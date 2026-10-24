# Sistema de tareas pendientes

## Objetivo
Organizar tareas personales mediante una aplicación de consola y demostrar el uso de Git e integración continua para detectar errores automáticamente.

## Funcionalidades
- Agregar tareas con un título obligatorio.
- Consultar tareas pendientes y completadas.
- Completar o eliminar tareas por ID.
- Guardar automáticamente en `datos/tareas.json`.

## Herramientas
Python 3.10 o superior, biblioteca estándar (json, pathlib, unittest), Git, GitHub y GitHub Actions. El flujo usa Python 3.12. No requiere pip ni paquetes externos.
Las versiones instaladas deben registrarse en el equipo del alumno con `py --version` y `git --version`.

## Ejecutar en Windows
1. Extraer completamente el ZIP.
2. Abrir la carpeta `sistema-tareas`.
3. Hacer doble clic en `INICIAR.bat`.

Alternativa en PowerShell dentro de esta carpeta:
```powershell
py -3 main.py
```
Si no existe el comando `py`, usar `python main.py`.

## Pruebas
Abrir `PROBAR.bat` o ejecutar:
```powershell
py -3 -m unittest discover -s tests -v
```
Son 8 pruebas independientes. Usan archivos temporales y no modifican las tareas personales.

## Estructura
```text
sistema-tareas/
  main.py                     Menú e interacción
  tareas.py                   Reglas y guardado
  tests/test_tareas.py         Pruebas automatizadas
  .github/workflows/ci.yml     Integración continua
  .gitignore                  Exclusiones de Git
  INICIAR.bat                 Inicio para Windows
  PROBAR.bat                  Pruebas para Windows
  docs/                       Guías de entrega
```

## Integración continua
Cada push o pull request ejecuta el flujo: descarga el código, prepara Python, revisa sintaxis y ejecuta las pruebas. Una prueba fallida produce un código de salida distinto de cero y marca el flujo como fallido. También puede iniciarse manualmente desde Actions.

## Estado de la entrega
Código y pruebas preparados. El repositorio, los commits del alumno y las ejecuciones remotas deben realizarse en su propia cuenta. No se incluyen capturas ni resultados remotos inventados. Consultar `docs/GUIA_GITHUB.md` y `docs/GUIA_ENTREGA.md`.
