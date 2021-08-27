@echo off
cd /d %~dp0
poetry run python -u ".\collector.py"
pause
