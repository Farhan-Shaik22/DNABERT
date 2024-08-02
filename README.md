# Fine-Tuned DNA BERT2 Model for Epigenetic Mark Prediction

This repository contains the official implementation of the Fine-Tuned DNA BERT2 model for predicting epigenetic marks. The model is based on the DNA BERT2 architecture and has been fine-tuned specifically for epigenetic mark prediction tasks.

## Model

You can find the Fine-Tuned DNA BERT2 model on Hugging Face at the following URL:
[Fine-Tuned DNA BERT2 Model for Epigenetic Mark Prediction](https://huggingface.co/farhan-shaik/Fine-Tuned-DNABERT2-For-Epigenetic-Mark-Prediction)

## Demo 

you can try out the working of the streamlit app in the following URL:
[Streamlit App for Epigenetic Mark Prediction](https://huggingface.co/spaces/farhan-shaik/StreamLit-App-for-Epigenetic-Mark-Prediction-using-DNABERT2)

For Testing use the data in the following URL:
[Testing Data](https://docs.google.com/spreadsheets/d/1sdOJdD-N_XV-Xh7vJkK9EJ_paXYCWzzF/edit?usp=drive_link&ouid=115779110561581468310&rtpof=true&sd=true)

## Project Overview

For a detailed explanation of the project, please refer to this [PowerPoint presentation](https://docs.google.com/presentation/d/1RiFGJW_lrbUEFNWD1sSUIiBYshqH4iru/edit?usp=sharing&ouid=115779110561581468310&rtpof=true&sd=true)

## Setup Instructions

To set up and run the project, follow these steps:

1. **Clone the Repository**
   - Clone this repository to your local machine using the following command:
     ```bash
     git clone https://github.com/Farhan-Shaik22/Finetuned-DNABERT2.git
     ```
   - Navigate into the project directory:
     ```bash
     cd Finetuned-DNABERT2
     ```

2. **Download Python**
   - Ensure that Python is installed on your system. You can download it from the official [Python website](https://www.python.org/downloads/).

3. **Install Dependencies**
   - Install all required dependencies using the provided `requirements.txt` file. Run the following command in your terminal or command prompt:
     ```bash
     pip install -r requirements.txt
     ```

4. **Run the Application**
   - Open your command prompt or terminal.
   - Navigate to the project directory where `DNABERT2-FINAL.py` is located (if you are not already in that directory).
   - Execute the following command to start the Streamlit application:
     ```bash
     streamlit run DNABERT2-FINAL.py
     ```

5. **Access the Application**
   - Open your web browser and go to `http://localhost:8501` to interact with the application.

## Troubleshooting

- If you encounter any errors, try reloading the page in your browser.
- If the issue persists uninstall Triton
   ```bash
     pip uninstall Triton
   ```
- If the issue persists, ensure that all dependencies are correctly installed and compatible with your Python version.

## Contact

For any questions or issues, please contact [Farhan/farhan2262003@gmail.com].

