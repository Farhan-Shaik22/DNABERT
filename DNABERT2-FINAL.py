
import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification, BertConfig
import torch

model_name = "farhan-shaik/Fine-Tuned-DNABERT2-For-Epigenetic-Mark-Prediction"


config = BertConfig.from_pretrained(model_name)


tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)


model = AutoModelForSequenceClassification.from_pretrained(model_name, trust_remote_code=True, config=config)

def main():
    st.title("Epigenetic Marks Prediction")
    st.write("An application of DNA BERT2")


    st.sidebar.header("About")
    st.sidebar.write("This app uses DNA BERT2 to predict the presence of epigenetic marks in a given DNA sequence.")


    user_input = st.text_area("Enter a DNA sequence:", height=150)

    if st.button("Classify Sequence"):
        if user_input:

            predicted_class, confidence = pred(user_input)


            st.subheader("Prediction Result")
            if predicted_class == 1:
                st.success("Epigenetic Mark detected!")
            else:
                st.info("No epigenetic mark found.")

            st.subheader("Class Distribution")
            st.write("1 - Epigenetic mark found")
            st.progress(confidence)
            st.text(f"{confidence * 100:.2f}%")
            
            st.write("0 - Epigenetic mark not found")
            st.progress(1 - confidence)
            st.text(f"{(1 - confidence) * 100:.2f}%")

        else:
            st.warning("Please enter a DNA sequence for classification.")


def pred(sequence):
    encoded_input = tokenizer(sequence, return_tensors='pt')
    
    with torch.no_grad():
        outputs = model(**encoded_input)
        logits = outputs.logits
        predicted_class = logits.argmax(-1).item()
        confidence = logits.softmax(dim=-1)[0, 1].item()

    return predicted_class, confidence

if __name__ == "__main__":
    main()