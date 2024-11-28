# RAG Based Chatbot

The RAG-based AI ChatBot is designed to streamline information retrieval from lengthy PDF files, catering to professionals like Researchers, Teachers, Engineers, and anyone. Utilizing **Pinecone Vector Database, Gemini API,** and **Sarvam AI**, it generates relevant answers from internal documents. It also generates speech from the response using an LLM. Built with Streamlit for the frontend and FastAPI endpoints for the backend, the chatbot leverages Langchain to handle queries efficiently. The project offers fast and accurate insights, optimizing document-based research and decision-making processes.

Give this a try. The project is deployed upon **Hugging Face Spaces** using **Docker**. [Click to try it](https://huggingface.co/spaces/aadil732/RAG-ChatBOT)

[Click to watch the YouTube Video](https://youtu.be/wphBupOCq28)


## 💻 Built with

Python is used as the main language to build this project.

### Python Libraries mainly used in the project:

* Streamlit [Check here](https://docs.streamlit.io/)
* Langchain [Check here](https://python.langchain.com/docs/introduction/)
* FastAPI [Check here](https://fastapi.tiangolo.com/learn/)

### APIs used in the project:

* Sarvam AI Text to Speech [Check here](https://docs.sarvam.ai/api-reference-docs/endpoints/text-to-speech)
* Google Gemini 1.5 Flash [Check here](https://ai.google.dev/gemini-api)
* Pinecone Vector Database [Check here](https://www.pinecone.io/)

### Version control tool and containerization technologies:

* Docker [Check here](https://www.docker.com/)
* GitHub [Check here](https://github.com/aadil080)

## 🧐 Features

Here are some of the project's best features:

* Completely built with Python.
* Agent based query handling.
* Containerized whole project using Docker.
* Support for long content files.
* Free and open-source resources used to built. 

## 🛠️ Installation Steps

### By Basic Way

1. Clone the repo

    ```bash
    git clone https://github.com/aadil080/Sarvam-ML-Assignment.git
    ```

2. Change the working directory and install the requirements

    ```bash
    pip install -r requirements.txt
    ```

3. Create & add environment variables in the ".env" file

    ```plaintext
    PINECONE_API_KEY = <your_pinecone_index_api_key>
    PINECONE_INDEX_NAME = <your_pinecone_name>
    GOOGLE_API_KEY = <your_google_gemini_1.5_flash_api_key>
    SARVAM_API_KEY = <your_sarvam_ai_text_to_speech_api_key>
    ```

4. Execute the bash file

    ```bash
    bash start.sh
    ```

### Using Docker

1. Clone the repo

    ```bash
    git clone https://github.com/aadil080/Sarvam-ML-Assignment.git
    ```

2. Create & add environment variables in the ".env" file

    ```plaintext
    PINECONE_API_KEY = <your_pinecone_index_api_key>
    PINECONE_INDEX_NAME = <your_pinecone_name>
    GOOGLE_API_KEY = <your_google_gemini_1.5_flash_api_key>
    SARVAM_API_KEY = <your_sarvam_ai_text_to_speech_api_key>
    ```

3. Execute the Docker image creation command

    ```bash
    docker build -t <image_name> . # here period represents the dockerfile path
    ```

4. Create a new container from the created image

    ```bash
    docker run -p 8000:80 <image_name>
    ```

## Usage

After all the above steps, open your browser on the same machine and type the address below:

```bash 
http://localhost:8501
```



## 🛡️ License

This project is licensed under the Apache-2.0 license.
