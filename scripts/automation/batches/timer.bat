cd %~dp0
cd ../
rem set python=venv\Scripts\python.exe
rem %python% timer.py %*
rem python timer.py %*
rem start cmd @cmd /k "venv&python timer.py %*"

python timer.py %*
pause
exit