@echo off
echo =========================================
echo Ejecutando script.py en Docker...
echo =========================================

docker run --rm -v "%cd%":/app entorno-datos

echo.
echo =========================================
echo Ejecucion terminada.
pause