# LangChain-GenAI

LangChain-GenAI is an integration package connecting Google's Generative AI package and LangChain. This project provides utilities and integrations to work with LangChain and Google's Generative AI.


### Prerequisites
- Docker


## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-repo/langchain-genai.git
    ```

2. Build the Docker image:
    ```sh
    docker build -t langchain .
    ```

## Running the Project

To run the project using Docker, execute the following command:

```sh
docker run --name langchain-dev -d -v ${PWD}:/app langchain tail -f /dev/null
```

## Project Structure
.env
file:///app/compose.yml
dockerfile
langchain_genai/
    __init__.py
    main.py
file:///app/poetry.lock
file:///app/pyproject.toml
file:///app/README.md
tests/
    __init__.py




## Contributing
Anyone who loves to build AI Applications can contribute to this project 

