# AI-Chat-Bot
A tiny command line assistant that sends the prompt to OpenAI and prints the raw chat completion result. It reads the API key from an environment variable and keeps a running list of user messages in memory.

Features
Minimal Python script that calls the Chat Completions API with the model gpt-4o.
Reads API key from the OPENAI_API_KEY environment variable.
Keeps a simple in memory history of user messages across calls.

How it works
The script creates an OpenAI client with the API key from the environment and defines a function named completion.
Each run asks for a prompt in the terminal, sends it to the API, and prints the raw response object to stdout.
A global messages list stores only user messages, which keeps inputs across calls inside the same process.

Requirements
Python 3.8 or newer.
An OpenAI API key set as an environment variable named OPENAI_API_KEY.
Internet access for API calls.

Installation
Create and activate a virtual environment if desired.
Install the OpenAI Python package:
pip install openai
Save the provided script as main.py in the project folder.

Environment setup
Export the API key in the current shell session.
macOS or Linux:
export OPENAI_API_KEY="sk‑replace_with_real_key"
Windows PowerShell:
setx OPENAI_API_KEY "sk‑replace_with_real_key"
Close and reopen the terminal after setx so the variable is available.

Run
From the project folder, run:
python main.py
When prompted, type a question and press Enter to send it to the model gpt-4o.

Expected output
The script prints the raw completion object returned by the SDK.
To print only the assistant text, replace the print line with:
print(chat_completion.choices.message.content)

Configuration
Model: change gpt-4o to another available model string if needed.

History: the script only appends user messages to messages. To preserve full chat context, also append the assistant reply after each call.

File structure
main.py: entry point with the client setup, input prompt, and completion function.
