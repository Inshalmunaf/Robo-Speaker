import os


if __name__ == '__main__':

    print("Welcome to Robo Speaker\n")
    while True:
        x= input("Enter what you  want me to say : ")
        if x=='q':
            break;
        command = f'powershell -Command "Add-Type -AssemblyName System.Speech; $speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; $speak.Speak(\'{x}\')"'
        os.system(command)

