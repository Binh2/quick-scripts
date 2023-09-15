@echo off
cd C:\cua-Binh\MyPython\Script
set python=venv\Scripts\python.exe
set website=mazii
%python% web_search.py %website% %*
exit