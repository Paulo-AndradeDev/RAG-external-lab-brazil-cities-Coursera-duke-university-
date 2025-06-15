# Introduction to Retrieval Augmented Generation (RAG) External Lab

## Overview
This repository contains an external lab hands-on project for the course *Introduction to Retrieval Augmented Generation (RAG)* offered by Duke University on Coursera. The objective of this external lab is to implement the RAG pattern using custom data, following the example code provided in the course.

## Course Information
- **Course Name**: Introduction to Retrieval Augmented Generation (RAG)
- **Platform**: Coursera
- **Link**: [https://www.coursera.org/learn/introduction-to-rag/home/welcome](https://www.coursera.org/learn/introduction-to-rag/home/welcome)

## Objective
The primary goal of this project is to:
- Implement the RAG pattern with custom data.
- Use the `llamafile` LLM model on Windows for generating responses.
- Leverage open government data from Brazil to build a knowledge base.

## Data Source
The dataset used in this project is sourced from the Brazilian government's open data portal: [https://dados.gov.br](https://dados.gov.br). Specifically, the dataset is the list of all municipalities in Brazil, available as `brazilian_cities.csv`.

## Tools and Technologies
- **LLM Model**: `llamafile` (Windows-compatible)
  - For more information about `llamafile`, visit: [https://github.com/Mozilla-Ocho/llamafile](https://github.com/Mozilla-Ocho/llamafile?tab=readme-ov-file)
- **Python Libraries**:
  - `pandas`: For data manipulation.
  - `qdrant_client`: For vector database operations.
  - `sentence_transformers`: For embedding generation.
- **Environment**: Python virtual environment.

## Project Structure
The project structure is as follows:
```
├── brazilian_cities.csv         # Dataset containing Brazilian municipalities
├── llava-v1.5-7b-q4.llamafile.exe # LLM model executable
├── rag_llamafile.py             # Main script for implementing RAG with llamafile
├── requirements.txt             # List of dependencies
└── README.md                    # This file
```

## Getting Started
To run this project, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone git@github.com:Paulo-AndradeDev/RAG-external-lab-brazil-cities-Coursera-duke-university-.git
   cd RAG-external-lab-brazil-cities-Coursera-duke-university-
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Llamafile Server**:
   - Download the `llava-v1.5-7b-q4.llamafile.exe` from [Mozilla Ocho's llamafile repository](https://github.com/Mozilla-Ocho/llamafile).
   - Execute the file to start the server on `http://localhost:8080`:
     ```bash
     ./llava-v1.5-7b-q4.llamafile.exe
     ```

## Dataset Description
The dataset `brazilian_cities.csv` contains information about all municipalities in Brazil. Below is a sample of the dataset:
```
1100106,Guajará-Mirim,RO
1100379,Alto Alegre dos Parecis,RO
1100205,Porto Velho,RO
1100452,Buritis,RO
1100122,Ji-Paraná,RO
```

## Example Code: Manipulating the Dataset with Pandas
Here are some examples of how to load and manipulate the dataset using Pandas:

**Load the Dataset**
   ```python
   import pandas as pd

   # Load the dataset
   df = pd.read_csv('brazilian_cities.csv', encoding='latin-1')

   # Display the first few rows
   print(df.head())
   ```


## Acknowledgments
- **Data Source**: Brazilian government open data portal ([https://dados.gov.br](https://dados.gov.br/dados/conjuntos-dados/tabela-de-rgos-e-municpios)).
- **LLM Model**: `llamafile` by Mozilla Ocho ([https://github.com/Mozilla-Ocho/llamafile](https://github.com/Mozilla-Ocho/llamafile)).
- **Course**: Introduction to Retrieval Augmented Generation (RAG) by Duke University on Coursera.

## Contact
If you have any questions or feedback, feel free to reach out!
