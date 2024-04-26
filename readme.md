# AI, Roast My Code

## Objective

AI, Roast My Code is a web application designed to assess and improve users' Python coding skills—with a fun twist. This proposal describes the development and deployment of a Streamlit application powered by AIConfig.

## Prerequisites

To get started with AI, Roast My Code, make sure you have installed all dependencies listed in `requirements.txt`. To install these, run:

```bash
pip install -r requirements.txt
```

## Repository Structure

```graphql
AI_Roast_My_Code/
│
├── app/                      # Application source files
│   ├── __init__.py           # Initializes Python app as a package
│   ├── main.py               # Entry point for the Streamlit application
│   ├── config.py             # Configuration settings for the app
│   └── utils.py              # Utility functions used across the application
│
├── tests/                    # Test cases for the application
│   ├── __init__.py
│   ├── test_main.py          # Tests for main application functionality
│   └── test_utils.py         # Tests for utility functions
│
├── ai/                       # AI and machine learning models
│   ├── __init__.py
│   ├── model.py              # AI models to assess Python code
│   └── preprocess.py         # Preprocessing scripts for the model input
│
├── data/                     # Data used by the models
│   ├── raw/                  # Raw data, unprocessed
│   └── processed/            # Processed data ready for modeling
│
├── docs/                     # Documentation files
│   ├── installation.md
│   ├── usage.md
│   └── contribution.md
│
├── notebooks/                # Jupyter notebooks for exploration and presentations
│   └── explorations.ipynb
│
├── requirements.txt          # Project dependencies
├── LICENSE                   # License file
└── README.md                 # Project README with general info
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

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.
