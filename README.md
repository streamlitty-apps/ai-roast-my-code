# **AI, Roast My Code**

AI, Roast My Code is a web application designed to assess and improve users' Python coding skills—with a fun twist. This proposal describes the development and deployment of a Streamlit application powered by AIConfig.

## Prerequisites

To get started with AI, Roast My Code, make sure you have installed all dependencies listed in `requirements.txt`. To install these, run:

```bash
pip install -r requirements.txt
```

## Setting Up Your Development Environment

Clone the Repository to your local machine:

```bash
git clone https://github.com/yourusername/AI_Roast_My_Code.git
```

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

## Project Organization

Below is a breakdown of the files in this project, with additional information to help you understand their roles and how they fit into the overall structure:

    ├── streamlit_app.py        <- This is the main file that runs the Streamlit app
    |
    ├── requirements.txt        <- A list of Python packages that the project depends on
    |
    ├── README.md               <- The main README file for the project to help you get started
    |
    ├── .gitignore              <- This file tells Git which files and directories to ignore
    |
    └── LICENSE                 <- The license file containing the terms of use for the project

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.
