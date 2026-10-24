# Guía para trabajar después en GitHub

No ejecutes todo todavía si lo haremos juntos. Instala Git si no lo tienes. Abre PowerShell en la carpeta del proyecto.

## Identidad e inicio
Sustituye los valores de ejemplo por los tuyos:
```powershell
git config --global user.name "TU NOMBRE"
git config --global user.email "TU CORREO DE GITHUB"
git init -b main
```

## Cinco commits de grupos de archivos
Revisa y comprende cada grupo antes de registrarlo. Estos commits registran la incorporación de archivos preparados; no representan un historial previo de desarrollo.
```powershell
git add .gitignore LEEME_PRIMERO.txt
git commit -m "Crear base y exclusiones del proyecto"
git add tareas.py
git commit -m "Incorporar gestion y persistencia de tareas"
git add main.py INICIAR.bat
git commit -m "Agregar interfaz de consola e inicio en Windows"
git add tests PROBAR.bat
git commit -m "Agregar ocho pruebas automatizadas"
git add .github README.md docs
git commit -m "Configurar integracion continua y documentar uso"
```

Crea un repositorio vacío llamado sistema-tareas en GitHub (sin README, licencia ni gitignore). Sustituye TU_USUARIO:
```powershell
git remote add origin https://github.com/TU_USUARIO/sistema-tareas.git
git push -u origin main
```
Autentícate con el mecanismo que muestre Git. No compartas contraseñas o tokens en el chat. En GitHub abre Actions y espera el resultado; captura la ejecución exitosa y el historial de commits.

## Error controlado
1. En tareas.py, dentro de agregar, cambia exclusivamente `"completada": False` por `"completada": True`.
2. Ejecuta PROBAR.bat: test_agregar_tarea_pendiente debe fallar porque una tarea nueva debe estar pendiente.
3. Registra y sube:
```powershell
git add tareas.py
git commit -m "Demostrar fallo controlado en estado inicial de tarea"
git push
```
4. Espera que Actions falle. Guarda captura del detalle de la prueba y del cambio.
5. Restaura `"completada": False`, ejecuta PROBAR.bat y sube:
```powershell
git add tareas.py
git commit -m "Corregir estado inicial y recuperar pruebas exitosas"
git push
```
6. Espera la ejecución exitosa posterior y captura el resultado. No subas el fallo y la corrección juntos: necesitas conservar dos ejecuciones distintas.

## Explicación para exposición
- Git registra versiones; GitHub aloja el repositorio.
- main.py muestra el menú; tareas.py contiene reglas y persistencia.
- unittest compara el comportamiento con resultados esperados.
- GitHub Actions ejecuta esas verificaciones con cada cambio subido.
- Una tarea nueva marcada completa rompe la regla del proyecto; la prueba la detecta.
