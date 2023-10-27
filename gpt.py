#!/usr/bin/env python3

import subprocess
import platform
import openai
import sys
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

pseudo = " ".join(sys.argv[1:])

if pseudo == "":
    print("USAGE: " +  sys.argv[0] + " <pseudo command>")
    sys.exit(1)

def make_command(pseudo_command):
    try:
        response = openai.ChatCompletion.create(
            request_timeout=10,
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": "Convert this pseudo command into a real command that can be run in the " + platform.system() + " terminal. Note that the command might include misspelled, invalid or imagined arguments or even imagined program names. Try your best to convert it into an actual command that would do what the command seems to be inteded to do.\n\n" + pseudo_command + "\n\nRespond only with the command."
                }
            ]
        )
    except openai.error.Timeout:
        retry = input("ERROR: OpenAI API Timeout! Try again? (y/n) ")
        if retry == "y":
            return make_command(pseudo_command)
        else:
            sys.exit(1)

    return response["choices"][0]["message"]["content"]

command = make_command(pseudo)

print("COMMAND: " + command)

confirmation = input("Run? (y/n) ")

if confirmation == "y":
    subprocess.run(command, shell=True)
