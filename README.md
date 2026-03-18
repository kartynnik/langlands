# kartynnik/langlands
A new, computational light on the Langlands program,
a.k.a.
the language of mathematics as design meta-language


## Where to start
Study [annotated_code.py](annotated_code.py) and
[closing-the-loop.md](closing-the-loop.md).

Then proceed to [projections/](projections/) as desired.


## Pasting into an LLM (AI Chatbot)
For now, only major Unix-like (Linux, macOS, Windows Subsystem for Linux)
environments are supported. Consider asking on StackOverflow how to add yours.

First, install Git into your command-line enviroment and clone the repository:
```sh
git clone https://github.com/kartynnik/langlands && cd langlands
```

Then use [./scripts/summarize-to-clipboard.sh](scripts/summarize-to-clipboard.sh)
to get a version of this repository paste-able into an LLM.

Or use `./scripts/summarize.sh > /tmp/YOUR_FILE` manually if the LLM UI snaps
:smile:.
