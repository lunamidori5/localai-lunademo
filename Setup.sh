#!/bin/bash
echo "Setting up Python environment"
python3 -m venv pythonlocalai
source pythonlocalai/bin/activate
echo "Installing Python Imports for LocalAi Demo Bot"
pip install openai
pip install langchain
echo Waiting for 50 seconds to give time to docker to setup LocalAi...
sleep 50
python main.py