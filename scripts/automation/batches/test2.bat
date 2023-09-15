@echo off
cd C:\cua-Binh\MyPython\Script
set string=test2
set python=venv\Scripts\python.exe
%python% test2.py %1 %string% %*
exit