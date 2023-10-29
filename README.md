# TryRAG
Modular RAG framework for experimentation.

## App Description

The RAG Framework Python Package is designed to provide a convenient way to interact with various components of the RAG (Retrieval-Augmented Generation) framework. RAG is a powerful framework used for generating text-based responses, where users can select specific components like VectorDB, Language Model (LLM), Orchestrator, Langchain, or the Llama index, or simply use plain Python to generate text completions. The package allows users to select the desired components and obtain outputs from the RAG framework, including different methods of employing RAG.

## Installation

To use this package, follow these steps:

1. **Clone the Repository**: Clone the RAG Framework Python Package repository from GitHub.

    ```bash
    git clone https://github.com/SDcodehub/TryRAG.git
    cd rag-framework-python-package
    ```

2. **Create a Virtual Environment**: It is recommended to create a virtual environment to manage dependencies.

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use "venv\Scripts\activate"
    ```

3. **Install Dependencies**: Install the required dependencies from the `requirements.txt` file.

    ```bash
    pip install -r requirements.txt
    ```

4. **API Key Configuration**:

   - Create a `.env` file in the project directory.
   
     ```bash
     touch .env
     ```

   - Open the `.env` file and add your OpenAI API key as follows:

     ```plaintext
     OPENAI_API_KEY=your_api_key_here
     ```

## Notes

- For more information on the RAG framework and its components, refer to the official RAG framework documentation.
- Additional methods for employing RAG can be explored based on the specific use case and requirements.

## License

This package is distributed under the MIT License. See the `LICENSE` file for more details.

---

*Note: This README provides a basic structure. You may need to update and refine it based on the specific implementation of your RAG framework and package details.*
