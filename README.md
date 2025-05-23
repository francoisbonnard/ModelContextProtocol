# ModelContextProtocol

# UV tutorial

[Youtube tutorial](https://www.youtube.com/watch?v=6pttmsBSi8M)

[installing uv](https://docs.astral.sh/uv/getting-started/installation/)

[uv docs](https://docs.astral.sh/uv/)

## useful commands

    uv python list
    uv python install 3.14
    uv run main.py
    uv run --python 3.14 main.py
    uv run --with asyncio --python 3.14 
    uv run --with rich --with requests .\01-uv.py

uv init

    uv init --script 01-uv.py --python 3.13

will add the following lines :

    # /// script
    # requires-python = ">=3.13"
    # dependencies = []
    # ///

    uv add --script 01-uv.py "rich" "requests"

Python project

    uv init 
    uv init my-dir
    uv add asyncio
    uv add requests
    uv add requests==2.1.2

    uv add -r .\requirements.txt

Create venv with specific python  version 

uv venv --python 3.13 .venv
.\.venv\Scripts\activate
uv pip sync requirements.txt

# Asyncio

[Asyncio in python](https://www.youtube.com/watch?v=Qb9s3UiMSTA)

[Asyncio official doc](https://docs.python.org/3/library/asyncio.html)

## Event Loop


# MCP crash course

[Youtube course](https://www.youtube.com/watch?v=5xqFjh56AwM)
[MCP Crash Course for Python Developers in github](https://github.com/daveebbelaar/ai-cookbook/tree/main/mcp/crash-course)

# MCP Resources

[MCP Servers in Github](https://github.com/modelcontextprotocol/servers)



