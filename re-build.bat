@echo off
echo =========================================
echo Construyendo la imagen de Docker...
echo =========================================

docker build -t entorno-datos .

echo.
echo =========================================
echo Construccion terminada.
pause