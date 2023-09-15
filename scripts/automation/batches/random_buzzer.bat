rem @echo off
cd C:\cua-Binh\MyPython\Script\automation

rem set python=venv\Scripts\python.exe
rem %python% timer.py %*
rem python timer.py %*
rem start cmd @cmd /k "venv&python timer.py %*"

venv & python random_buzzer.py %*
pause
exit