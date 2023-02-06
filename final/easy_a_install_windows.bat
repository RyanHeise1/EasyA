@echo off

rem Install packages using pip
pip install matplotlib tkinter

rem Check if installation was successful
if %errorlevel% equ 0 (
  echo Installation successful
) else (
  echo Installation failed
)