# 📝 MCQ Generator Chatbot using LangChain and Hugging Face
Welcome to the MCQ Generator Chatbot! This project allows users to generate multiple-choice questions (MCQs) from uploaded documents, such as PDFs or text files. The chatbot leverages advanced language models from Hugging Face, integrated with LangChain, to create high-quality MCQs in various subjects and tones. It also evaluates the complexity of the generated questions to ensure they are appropriate for the target audience.

## 📋 Project Overview
This chatbot is designed to make the creation of MCQs from any document simple and efficient. Users can upload a document, specify the number of MCQs, choose a subject, and set the tone or complexity level of the questions. The chatbot processes the document and returns a set of well-formatted MCQs along with an evaluation of their complexity.

## 🌟 Features
- 📄 Document Upload: Upload PDF or text files to generate MCQs.
- ⚙️ Customizable MCQs: Specify the number, subject, and complexity level of the MCQs.
- 🤖 LLM-Powered Question Generation: Uses an advanced language model from Hugging Face for generating high-quality MCQs.
- 🧠 MCQ Evaluation: Provides an analysis of the complexity of the generated MCQs to ensure they are suitable for the target audience.
- 💻 Streamlit Interface: A user-friendly web interface for easy interaction.

## 🚀 How to Run
Follow these steps to get the project up and running on your local machine:

### Clone the Repository:

Clone the repository to your local machine:

```bash
git clone https://github.com/amber-bagchi/MCQ-Generator.git
```
```bash
cd MCQ-Generator
```
### Create and Activate a Conda Environment:

Create a Conda environment with Python 3.8:

```bash
conda create -n mcq_generator python=3.8 -y
```
```bash
conda activate mcq_generator
```
### Install Requirements:

Install the necessary packages:

```bash
pip install -r requirements.txt
```

### Set Up Environment Variables:

Create a .env file in the root directory and add your Hugging Face API key:

```bash
HUGGINGFACE_API_KEY=your_huggingface_api_key
```
### Run the Application:

Run the Streamlit application:

```bash

streamlit run Streamlit.py
```
## Interact with the Application:

- 📤 Upload a Document: Upload a PDF or text file containing the content from which you want to generate MCQs.
- 📝 Specify MCQ Details: Enter the number of MCQs, the subject, and the desired tone or complexity level.
- ⚡ Generate MCQs: Click the "Create MCQs" button and wait for the results.

## 📽️ Project Video

![MCQ_Generator-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/f3b20b3c-4406-41f4-a00b-53e6bcd9e9b4)

## 🛠 Tech Stack
- Python: Programming language used for development.
- LangChain: Framework for developing applications powered by language models.
- Hugging Face: Provides the language models used for generating and evaluating MCQs.
- Streamlit: Framework for creating web applications with Python.
- dotenv: Used for managing environment variables.
- PyPDF2: Library for reading and extracting text from PDF files.

## 📂 Project Structure
```bash
MCQ-Generator/
│
├── src/
│   ├── mcqgenerator/
│   │   ├── MCQGenerator.py   # Core logic for generating and evaluating MCQs
│   │   ├── utils.py          # Utility functions for reading files
│   │   └── logger.py         # Logger configuration
│
├── Streamlit.py               # Streamlit interface for user interaction
├── requirements.txt           # Required packages for the project
├── setup.py                   # Setup file for the package
└── .env                       # Environment variables (not included in the repository)
```

## 🤝 Contributing
Feel free to fork this repository, make improvements, and submit pull requests. Your contributions are always welcome!

## 📜 License
This project is licensed under the MIT License. See the LICENSE file for more details.

