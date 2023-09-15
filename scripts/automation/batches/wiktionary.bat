@echo off
cd C:\cua-Binh\MyPython\Script
set python=venv\Scripts\python.exe
set website=wiktionary
%python% web_search.py %website% %*
exit