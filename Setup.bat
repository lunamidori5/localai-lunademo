@echo off
title Loading Python environment
echo Setting up Python environment
python -m venv pythonlocalai
call pythonlocalai\Scripts\activate.bat
title Python: Pip install -r all
echo Installing Python Imports for LocalAi Demo Bot
pip install openai 
pip install langchain
pip install requests
pip install python-on-whales
python main.py