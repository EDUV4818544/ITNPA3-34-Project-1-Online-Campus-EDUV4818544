Question 1 & 2 Deployment Guide

Purpose

This Streamlit application classifies the text of a research abstract into one of two categories: artificial intelligence (ai) or classical research (classical).



The classifier uses character-level TF-IDF with Linear Support Vector Machine (Linear SVM). In the notebook, the selected configuration achieved 92.44% test accuracy. The saved deployment model was subsequently retrained on the full cleaned dataset.

Required deployment files

Keep these three files together in the deployment/ folder:

\- app.py, the Streamlit user interface and text-cleaning code.

\- research\_classifier.joblib, the saved TF-IDF + Linear SVM pipeline.

\- requirements.txt,  the Python packages required by the application.

Only load the .joblib model from a source you trust. A Joblib file is a Python-serialized object.

Requirements

\- Windows, macOS or Linux with a compatible Python installation.

\- Internet access to install Python packages, if they are not already installed.

\- Anaconda Prompt, Windows Command Prompt, or another terminal.

Prefer the Python/scikit-learn versions used to save the model. The requirements.txt supplied with this project pins the scikit-learn version used in the original environment.

Local deployment 

1\. Download and extract the repository, or clone it with Git.



2\. Open Anaconda Prompt and navigate to the repository root, the folder containing documentation, datasets, notebooks, and deployment. On Windows, for example:

cd /d "C:\\Users\\wikus\\ITNPA-Project 1-Online Campus-EDUV4818544" Or the path the folder is located on your machine

3\. Install the dependencies:

python -m pip install -r deployment/requirements.txt

4\. Run the app from the repository root:

python -m streamlit run deployment/app.py

5\. When Streamlit starts, it will normally open a browser tab. Otherwise open:



http://localhost:8501



If Streamlit prompts you to enter an email address on first use, you may leave it blank and press Enter.



6\. Paste a research abstract into the text area, click Classify Abstract, and read the predicted category.



7\. When finished, go back to the terminal and press Ctrl+C to stop Streamlit.

