#!/bin/bash
echo "Setting up Python environment"
python3 -m venv pythonlocalai
source pythonlocalai/bin/activate

echo "Installing Python Imports for LocalAi Demo Bot"
pip install openai 
pip install langchain
pip install request
python main.py