@echo off
title Loading Python environment
echo Setting up Python environment
python -m venv pythonlocalai
call pythonlocalai\Scripts\activate.bat
title Python: Pip install -r all
echo Installing Python Imports for LocalAi Demo Bot
pip install openai
pip install langchain
title So how are you today? Doing okay? Good, sit back and wait for localai docker to load.
echo Waiting for 50 seconds for docker to setup...
timeout /T 50 /nobreak >nul
python main.py