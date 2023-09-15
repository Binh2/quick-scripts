@echo off
cd C:\cua-Binh\MyPython\Script
cls
set website=google
py web_search.py %website% %*
exit