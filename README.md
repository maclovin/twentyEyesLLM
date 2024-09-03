# twentyEyesLLM

Use LLM to generate a daily-routine report on computer. You can run it using a inference server locally or remotely with Ollama and OpenAI. 

This small program basically take a screenshot between dired a time-interval, submit it to the inference along a system prompt and process the result, aggregating them all into a local history file. Then you can generate Markdown reports about your local computer activities in a specific day.

## Usage
Running using Ollama
```console
$ python -m twentyEyesLLM --ollama --interval 7
```

Running using Openai
```console
$ OPENAI_API_KEY=...
$ python -m twentyEyesLLM --openai --interval 7
```
_**ATTENTION**: During the first running you will be asked to grant Screen Recording permissions to the terminal. It is necessary in order to allow this program to take screenshots and submit to the inference server, remember, you can choose between use a local inference server (Ollama) or a remote server (OpenAI)._ 

Show local history and generate report with selected history
```console
$ python -m twentyEyesLLM history --list
24_06_02
24_05_04
24_06_07
24_06_06
$ python -m twentyEyesLLM report --date 24_06_07 > my_report.md
```

Clear local history
```console
$ python -m twentyEyesLLM history --clear
```

Get the full arguments descriptions
```console
$ python -m twentyEyesLLM --help
```

