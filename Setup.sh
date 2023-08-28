#!/bin/bash

os=$(uname -s)
if [ "$os" == "Linux" ]; then
  dist=$(lsb_release -i | awk '/^Distributor:/ {print $2}')
  if [ "$dist" == "Ubuntu" ]; then
    echo "You are on Ubuntu. Installing Docker, Python3.11, and checking Git."
    sudo apt-get update
    sudo apt-get install ca-certificates curl gnupg
    sudo install -m 0755 -d /etc/apt/keyrings
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    sudo chmod a+r /etc/apt/keyrings/docker.gpg
    echo \
    "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
    "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
    sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    sudo apt-get update
    sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
    sudo apt install software-properties-common -y
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt install python3.11
    sudo apt-get install virtualenv -y
    sudo apt-get install pip -y

  elif [ "$dist" == "Linux Mint" ]; then
    echo "You are on Linux Mint."
  else
    echo "Unknown Linux distribution."
  fi
else
  echo "Unknown operating system."
fi

echo "Setting up Python environment"
python3 -m venv pythonlocalai
source pythonlocalai/bin/activate

echo "Installing Python Imports for LocalAi Demo Bot"
pip install openai
pip install langchain
python main.py