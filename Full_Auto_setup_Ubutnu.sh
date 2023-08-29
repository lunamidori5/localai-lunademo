#!/bin/bash

echo "You are on Ubuntu. Installing Docker, Python3.11"
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg -y
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
echo \
"deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
"$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.11 python3.10-venv pip docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin docker-compose -y

echo "Setting up Python environment"
python3 -m venv pythonlocalai
source pythonlocalai/bin/activate

echo "Installing Python Imports for LocalAi Demo Bot"
pip install openai
pip install langchain
python main.py