# **AI, Roast My Code**

AI, Roast My Code is a web application designed to assess and improve users' Python coding skills—with a fun twist. This proposal describes the development and deployment of a Streamlit application powered by AIConfig.

Requirements
------------
- [OpenAI API-KEY](https://platform.openai.com/docs/api-reference/api-keys)

Getting Started
------------
1. `git clone git@github.com:streamlitty-apps/ai-roast-my-code.git`
2. `cd ai-roast-my-code`
3. `pip install -r requirements.txt`
4. `streamlit run app/Roast_My_Code.py`

Opening AIConfig Editor
------------
AIConfig Editor allows you to visually create and edit the prompt chains and model parameters that are stored as AIConfigs. You can also chain prompts and use global and local parameters in your prompts. Learn more about [AIConfig Editor](https://aiconfig.lastmileai.dev/docs/editor).

1. Open your Terminal
2. Run this command: `aiconfig edit --aiconfig-path=app/roast_my_code.aiconfig.json`

This will open AIConfig Editor in your default browser at http://localhost:8080/. Here you can run and update the prompts locally, and when you run the prompts the outputs will render in the updated `roast_my_code.aiconfig.json` file.

Setting Up Your Development Environment
------------

Creating a Branch:

```bash
git checkout -b feature/YourAmazingFeature
```

Now you're ready to start making changes. After you've made your changes, you'll need to stage them for a commit:

```bash
git add .
```

Commit your changes using meaningful commit messages that describe what your changes do:

```bash
git commit -m 'Add a detailed description of your changes'
```

Push your changes to the remote repository:

```bash
git push --set-upstream origin feature/YourAmazingFeature
```

**Caveat**:

1. Only the first commit will request the command above. For any other push to the remote repository you can do a simple `git push`.
2. If you already have a branch or is starting to work with the `main` one, it's a good practice to execute `git pull` to sync the code.

Running Unit Tests
------------
1. `python -m unittest tests/test_openai_client.py`

Project Organization
------------

Below is a breakdown of the files in this project, with additional information to help you understand their roles and how they fit into the overall structure:

    ├── app/
    │   ├── helpers/
    │   │   └── openai_client.py <- Helper module for interacting with OpenAI services
    │   ├── views/
    │   │   └── aiconfig_page.py <- The page detailing the aiconfig file for this app
    │   │   └── roast_my_code_page.py <- The page where users get feedback on their code
    │   │   └── initial_page_load.py <- What users see on the initial page load
    │   └── roast_my_code.aiconfig.json <- The configuration file for aiconfig
    │   └── streamlit_app.py     <- This is the main file that runs the Streamlit app
    │   ├── chromadb_utils/
    │   |   ├── chroma.db/ <- Files generated from running ingest.py script containing created collection
    │   |   ├── pep8_sections/ <- Contains txt files with the contents of the PEP 8 documentation
    │   |   ├── ingest.py <- Script for RAG data ingestion & indexing with chromadb
    │   |   ├── chromadb_helpers.py <- Helper module for interacting with chromadb for RAG
    |
    ├── tests/
    │   └── test_openai_client.py <- Test file for the openai_client module
    |
    ├── requirements.txt         <- A list of Python packages that the project depends on
    |
    ├── README.md                <- The main README file to help you get started
    |
    ├── .gitignore               <- This file tells Git which files and directories to ignore
    |
    └── LICENSE                  <- The license file containing the terms of use for the project

License
------------
This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.
