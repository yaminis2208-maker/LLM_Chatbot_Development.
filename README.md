# Education AI Chatbot Using Python and Ollama

## 1. Project Overview
This project develops an AI-powered chatbot that answers education-related questions using Python and Ollama. It also stores conversation history and analyzes chatbot response lengths.

## 2. Objectives
- Develop an interactive AI chatbot.
- Answer questions about Python, AI, and student learning.
- Save questions and responses to CSV files.
- Analyze response lengths using Pandas.
- Visualize results using Matplotlib.

## 3. Technologies Used
- Python
- Ollama
- Llama 3.2
- Pandas
- Matplotlib
- Visual Studio Code

## 4. Features
- Interactive question-and-answer interface.
- Automatic conversation logging.
- CSV-based data storage.
- Response length analysis.
- Response length chart.

## 5. Project Structure
```text
Chatbot_Development/
├── dataset/
│   ├── chat_history.csv
│   ├── responses.csv
│   ├── chatbot_logs.txt
│   ├── response_analysis.csv
│   └── response_length_chart.png
├── screenshots/
├── chatbot.py
├── markdowncell.py
├── requirements.txt
└── README.md
```

## 6. Installation and Execution
1. Install Python.
2. Install Ollama and download the model:
   `ollama pull llama3.2:1b`
3. Create and activate a Python virtual environment.
4. Install the dependencies:
   `python -m pip install -r requirements.txt`
5. Run the chatbot:
   `python chatbot.py`
6. Ask questions and type `exit` to stop.

## 7. Data Analysis
The project uses Pandas to read conversation history, check missing values, and calculate chatbot response lengths. The results are saved in `dataset/response_analysis.csv`.

Matplotlib generates a chart comparing response lengths.

## 8. Results
The chatbot successfully generated responses to test questions and saved the conversation history. In the initial test, two conversations were analyzed, with an average response length of 2,485 characters.

## 9. Limitations
- AI-generated answers may be inaccurate.
- Response length does not measure answer quality.
- The chatbot requires Ollama and a locally available model.

## 10. Conclusion
This project demonstrates how Python and Ollama can be used to build an educational chatbot. Pandas and Matplotlib support basic analysis and visualization of chatbot responses.
