import os
import time
import openai
import random
import requests
import urllib.request

openai.api_key = "sx-xxx"
OPENAI_API_KEY = "sx-xxx"
os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
model = "lunademo"
file_url = "https://huggingface.co/TheBloke/WizardLM-13B-V1.2-GGML/resolve/main/wizardlm-13b-v1.2.ggmlv3.q2_K.bin"
file_name = "lunademo.bin"
new_file = 'lunademo.bin'
folder_path = "models"
sudo = ""

if os.name == 'nt':  # for Windows
    os.system('title Docker')
    os.system('cls')
else:  # for Linux and macOS
    print("It seems as you are on Linux, does your system use ``sudo``? If so please type in the word ``sudo``, If not, please hit enter: ")
    sudo = str(input("Please enter text: "))
    os.system('clear')
    
print("Do you have the LocalAI docker already set up?")
user_input_type = str(input("Yes or No: "))
user_input_type = user_input_type.lower()

if user_input_type != "yes":
    if os.name == 'nt':  # for Windows
        os.system('title Downloading Model')
        os.system('cls')
    else:  # for Linux and macOS
        os.system('clear')
        time.sleep(25)
    
    print("Please choose a text model based on your preferred level of system memory. Level 0 represents 4GB of system memory, while Level 3 represents 64GB of system memory and 16GB of VRAM. Which level would you like to select?")
    user_input_model_level = int(input("Model Ram Level: (0 <-> 3)"))

    if user_input_model_level > 3:
        print("Error level higher than 3 seen, setting level to 3")
        print("Downloading 30b Model...")
        file_url = "https://huggingface.co/TheBloke/WizardLM-30B-uncensored-GGUF/resolve/main/WizardLM-30B-Uncensored.Q5_0.gguf"
        current_file = 'WizardLM-30B-Uncensored.Q5_0.gguf'

    if user_input_model_level == 3:
        print("Downloading 30b Model...")
        file_url = "https://huggingface.co/TheBloke/WizardLM-30B-uncensored-GGUF/resolve/main/WizardLM-30B-Uncensored.Q5_0.gguf"
        current_file = 'WizardLM-30B-Uncensored.Q5_0.gguf'
        
    if user_input_model_level == 2:
        print("Downloading 13b Model...")
        file_url = "https://huggingface.co/TheBloke/WizardLM-13B-Uncensored-GGUF/resolve/main/WizardLM-13B-Uncensored.Q6_K.gguf"
        current_file = 'WizardLM-13B-Uncensored.Q6_K.gguf'
        
    if user_input_model_level == 1:
        print("Downloading 13b Low Ram Model...")
        file_url = "https://huggingface.co/TheBloke/WizardLM-13B-Uncensored-GGUF/resolve/main/WizardLM-13B-Uncensored.Q2_K.gguf"
        current_file = 'WizardLM-13B-Uncensored.Q2_K.gguf'
        
    if user_input_model_level == 0:
        print("Downloading 7b Model...")
        file_url = "https://huggingface.co/TheBloke/WizardLM-7B-uncensored-GGUF/resolve/main/WizardLM-7B-uncensored.Q2_K.gguf"
        current_file = 'WizardLM-7B-uncensored.Q2_K.gguf'
        
    file_path = os.path.join(folder_path, file_name)

    if os.path.isfile(file_path):
        print("File already exists in the folder.")
    else:
        print("File does not exist in the folder. Proceed with downloading.")
        file_path = os.path.join(folder_path, os.path.basename(new_file))
        urllib.request.urlretrieve(file_url, file_path)
        time.sleep(1.2)
    
    print("Alright lets setup a docker-compose using port 9095, to edit the config please edit the files `gpu.yaml` or `cpu.yaml` before you type in here.")
    print("Would you like to run this docker with GPU or CPU? (GPU is CUDA only for now)")
    user_input_type = str(input("CPU or GPU: "))
    user_input_type = user_input_type.lower()

    if user_input_type == "gpu":
        print("Alright setting up docker-compose with GPU - Cuda")
        current_file_docker = 'GPU.yaml'
        openai_port = 9095
    elif user_input_type == "cuda":
        print("Alright setting up docker-compose with GPU - Cuda")
        current_file_docker = 'GPU.yaml'
        openai_port = 9095
    elif user_input_type == "cpu":
        print("Alright setting up docker-compose with CPU")
        current_file_docker = 'CPU.yaml'
        openai_port = 9095
    else:
        print("Fallingback to setting up docker-compose with CPU")
        current_file_docker = 'CPU.yaml'
        openai_port = 9095

    os.rename(current_file_docker, "docker-compose.yaml")
    if os.name == 'nt':  # for Windows
        os.system('title Setting up Windows Docker-Compose File')
        os.system('docker-compose down --rmi all')
        os.system('start docker-compose up --pull --force-recreate')
    else:  # for Linux and macOS
        os.system(f'echo "{sudo} docker-compose down" > docker-setup.sh')
        os.system(f'echo "{sudo} docker-compose up" >> docker-setup.sh')
        os.system('chmod +x docker-setup.sh')
        os.system('gnome-terminal -- ./docker-setup.sh')

    if os.name == 'nt':  # for Windows
        os.system('title Setting up Docker-Compose File')
    else:  # for Linux and macOS
        print("If the window only poped up for a moment and is not still running. Please open a new command line in and run 'sudo docker-compose up' or 'docker-compose up'")

    print("Alright, I opened a new window that is setting up the docker-compose right now.")
    print("We will need to wait a few more moments before we can move on!")
    print("Waiting for a for more moments so that the docker can get fully set up and ready...")
    time.sleep(600)

    if os.name == 'nt':  # for Windows
        os.system('title Waiting on LocalAI docker')
        os.system('cls')
    else:  # for Linux and macOS
        os.system('clear')
    os.rename("docker-compose.yaml", current_file_docker)
else:
    if os.name == 'nt':  # for Windows
        os.system('Local AI Info')
        os.system('cls')
    else:  # for Linux and macOS
        os.system('clear')

    openai_port = int(input("What port is LocalAI running on?: "))
    model = str(input("What model would you like to use? (enter `xxx` to have this program do a `best guess` install): "))

    if model == "xxx":
        url = f"http://localhost:{str(openai_port)}/models/apply"
        headers = {"Content-Type": "application/json"}
        data = {"url": "https://raw.githubusercontent.com/go-skynet/model-gallery/main/llama2-7b-chat-gguf.yaml", "name": "lunademo"}

        response = requests.post(url, headers=headers, json=data)
        print(str(response))
        response.raise_for_status()
        print(str("Please wait for a few moments as LocalAi downloads and sets up the model..."))
        time.sleep(240)

if os.name == 'nt':  # for Windows
    os.system('title Welcome to LocalAI - Chat Demo')
    os.system('cls')
else:  # for Linux and macOS
    os.system('clear')

system_text = "Becca is a helpful Ai that helps the user by using Localai to do what what ever task the user asks them to do. "
session_inside = [{"role": "system", "content": "I am running normally!"}]

response = "Welcome to LocalAI demo by Luna Midori, To get started just type something in!"

with open("chatlog.log", "w") as file:
    file.write(response)

while True:
    print(response)
    user_input = input("Chat with LocalAI: ")
    response = ""
    loop_number = 0
    completion_text = ''
    collected_messages = []
    openai.api_base = f"http://localhost:{str(openai_port)}/v1"
    
    message_gpt = [{"role": "system", "content": system_text}, *session_inside,
                    {"role": "user", "content": f"Type a short reply to this question: {user_input}:"}, ]
    messages = [{"role": msg["role"], "content": msg["content"]} for msg in message_gpt]

    completion2 = openai.ChatCompletion.create(
                    model=model,
                    frequency_penalty=0.5,
                    presence_penalty=0.6,
                    repeat_penalty=0.5,
                    messages=messages,
                    temperature=0.55,
                    max_tokens=8000,
                    stream=True,
                    seed=random.randint(100000, 999999),
                    top_p=0.75
    )
    for chunk in completion2:
        loop_number = loop_number + 1
        if 'delta' in chunk['choices'][0] and chunk['choices'][0]['delta']:
            event_text = chunk['choices'][0]['delta']
            collected_messages.append(event_text)
        else:
            break  # exit the loop if delta is empty
        if loop_number > 2:
            sudo_message = ''.join([m.get('content', '') for m in collected_messages])
            if os.name == 'nt':  # for Windows
                os.system('cls')
            else:  # for Linux and macOS
                os.system('clear')
            print("Streaming message: " + str(sudo_message))
            loop_number = 0
    full_reply_content = ''.join([m.get('content', '') for m in collected_messages])
    response = full_reply_content
    
    session_inside.append({"role": "user", "content": f"(user) says {user_input}"})
    session_inside.append({"role": "assistant", "content": f"{response}"})
    
    text_out_unmoded = openai.ChatCompletion.create(
        model="lunademo",
        temperature=0,
        n=1,
        messages=[
            {"role": "system",
             "content": f"I am a AI that summarizes statements. I will share as much details.", },
            {"role": "user",
             "content": f"Summarize this memory: {str(session_inside)} "},
        ],
        max_tokens=3000
    )

    with open("chatlog.log", "r") as file:
            existing_content = file.read()
    
    updated_content = existing_content + "\n" + user_input + "\n" + response

    with open("chatlog.log", "w") as file:
            file.write(updated_content)
    
    textout = str(text_out_unmoded.choices[0].message.content)
    
    session_inside = [{"role": "system", "content": textout }]
    
    if os.name == 'nt':  # for Windows
        os.system('cls')
    else:  # for Linux and macOS
        os.system('clear')
