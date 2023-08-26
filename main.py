import os
import time
import openai
import random
import urllib.request

openai.api_base = "http://localhost:8080/v1"
openai.api_key = "sx-xxx"
OPENAI_API_KEY = "sx-xxx"
os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
file_url = "https://huggingface.co/TheBloke/WizardLM-13B-V1.2-GGML/resolve/main/wizardlm-13b-v1.2.ggmlv3.q2_K.bin"
file_name = "lunademo.bin"
new_file = 'lunademo.bin'
folder_path = "models"

if os.name == 'nt':  # for Windows
    os.system('title Docker')
    os.system('cls')
else:  # for Linux and macOS
    os.system('clear')
    
print("Do you have the LocalAI docker already set up?")
user_input_type = str(input("Yes or No: "))
user_input_type = user_input_type.lower()

if user_input_type != "yes":
    if os.name == 'nt':  # for Windows
        os.system('title Setting up Docker-Compose File')
        os.system('cls')
    else:  # for Linux and macOS
        os.system('clear')
    
    print("Would you like to run this docker with GPU or CPU? (GPU is CUDA only for now)")
    user_input_type = str(input("CPU or GPU: "))
    user_input_type = user_input_type.lower()

    if user_input_type == "gpu":
        print("Alright setting up docker-compose with GPU - Cuda")
        current_file = 'GPU.yaml'
    elif user_input_type == "cuda":
        print("Alright setting up docker-compose with GPU - Cuda")
        current_file = 'GPU.yaml'
    elif user_input_type == "cpu":
        print("Alright setting up docker-compose with CPU")
        current_file = 'CPU.yaml'
    else:
        print("Fallingback to setting up docker-compose with CPU")
        current_file = 'CPU.yaml'

    os.rename(current_file, "docker-compose.yaml")
    os.system('docker-compose up -d --pull always')


if os.name == 'nt':  # for Windows
    os.system('title Downloading Model')
    os.system('cls')
else:  # for Linux and macOS
    os.system('clear')
    
print("Please pick a model based on computer speed starting at 0 for low ram to 3 being high ram")
user_input_model_level = int(input("Model Ram Level: "))

if user_input_model_level > 3:
    print("Error level higher than 3 seen, setting level to 3")
    print("Downloading 30b Model...")
    file_url = "https://huggingface.co/TheBloke/WizardLM-30B-Uncensored-GGML/resolve/main/WizardLM-30B-Uncensored.ggmlv3.q4_0.bin"
    current_file = 'WizardLM-30B-Uncensored.ggmlv3.q4_0.bin'

if user_input_model_level == 3:
    print("Downloading 30b Model...")
    file_url = "https://huggingface.co/TheBloke/WizardLM-30B-Uncensored-GGML/resolve/main/WizardLM-30B-Uncensored.ggmlv3.q4_0.bin"
    current_file = 'WizardLM-30B-Uncensored.ggmlv3.q4_0.bin'
    
if user_input_model_level == 2:
    print("Downloading 13b Model...")
    file_url = "https://huggingface.co/TheBloke/WizardLM-13B-V1.2-GGML/resolve/main/wizardlm-13b-v1.2.ggmlv3.q4_K_M.bin"
    current_file = 'wizardlm-13b-v1.2.ggmlv3.q4_K_M.bin'
    
if user_input_model_level == 1:
    print("Downloading 13b Low Ram Model...")
    file_url = "https://huggingface.co/TheBloke/WizardLM-13B-V1.2-GGML/resolve/main/wizardlm-13b-v1.2.ggmlv3.q2_K.bin"
    current_file = 'wizardlm-13b-v1.2.ggmlv3.q2_K.bin'
    
if user_input_model_level == 0:
    print("Downloading 7b Model...")
    file_url = "https://huggingface.co/TheBloke/WizardLM-7B-uncensored-GGML/resolve/main/WizardLM-7B-uncensored.ggmlv3.q2_K.bin"
    current_file = 'WizardLM-7B-uncensored.ggmlv3.q2_K.bin'

if os.name == 'nt':  # for Windows
    os.system('title Downloading Model')
    os.system('cls')
else:  # for Linux and macOS
    os.system('clear')
    
file_path = os.path.join(folder_path, file_name)

if os.path.isfile(file_path):
    print("File already exists in the folder.")
else:
    print("File does not exist in the folder. Proceed with downloading.")
    print("Downloading the WizardLM Model... Please wait...")
    file_path = os.path.join(folder_path, os.path.basename(file_url))
    urllib.request.urlretrieve(file_url, file_path)
    os.rename(current_file, new_file)

print("If LocalAI is done building in the docker hit enter")
user_input_type = str(input(""))

os.system('docker-compose restart')

if os.name == 'nt':  # for Windows
    os.system('title Welcome to LocalAI - Chat Demo')
    os.system('cls')
else:  # for Linux and macOS
    os.system('clear')

system_text = "LocalAi is a helpful Ai that helps the user what what ever task the user asks them to do. "
session_inside = [{"role": "system", "content": "I am running normally!"}]

response = "Welcome to LocalAI demo by Luna Midori, To get started just type something in!"

while True:
    print(response)
    user_input = input("Chat with LoaclAI: ")
    
    message_gpt = [{"role": "system", "content": system_text}, *session_inside,
                    {"role": "user", "content": f"Type a short reply to this question: {user_input}:"}, ]
    messages = [{"role": msg["role"], "content": msg["content"]} for msg in message_gpt]

    completion2 = openai.ChatCompletion.create(
                    model="lunademo",
                    frequency_penalty=0.5,
                    presence_penalty=0.6,
                    repeat_penalty=0.5,
                    messages=messages,
                    temperature=0.55,
                    max_tokens=1800,
                    stream=False,
                    seed=random.randint(100000, 999999),
                    top_p=0.75
    )
    response = str(completion2.choices[0].message.content)
    
    session_inside.append({"role": "user", "content": f"user) says {user_input}"})
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
        max_tokens=1500
    )
    
    textout = str(text_out_unmoded.choices[0].message.content)
    
    session_inside = [{"role": "system", "content": textout }]
    
    if os.name == 'nt':  # for Windows
        os.system('cls')
    else:  # for Linux and macOS
        os.system('clear')
