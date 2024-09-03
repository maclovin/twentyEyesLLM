# twentyEyesLLM

Gere insights de rotina baseados no seu histórico de screenshots com motores de LLM como Ollama ou Openai.

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

