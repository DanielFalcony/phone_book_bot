@echo off

call %~dp0venv\Scripts\activate

cd %~dp0bot_pack

set TOKEN=5601243555:AAH93TKtvFElJjFJwtzsW0PfeTONsAYPn7s

python main_bot.py

pause