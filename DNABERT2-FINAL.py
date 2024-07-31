#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch


# In[3]:


tokenizer = AutoTokenizer.from_pretrained("farhan-shaik/Fine-Tuned-DNABERT2-For-Epigenetic-Mark-Prediction", trust_remote_code=True)
model = AutoModelForSequenceClassification.from_pretrained("farhan-shaik/Fine-Tuned-DNABERT2-For-Epigenetic-Mark-Prediction", trust_remote_code=True)


# In[4]:


def main():
    st.title("Epigenetic Marks Prediction")
    st.write("An application of DNA BERT2")

    # Sidebar with information
    st.sidebar.header("About")
    st.sidebar.write("This app uses DNA BERT2 to predict the presence of epigenetic marks in a given DNA sequence.")

    # User input
    user_input = st.text_area("Enter a DNA sequence:", height=150)

    # Predict when the user provides input
    if st.button("Classify Sequence"):
        if user_input:
            # Call the pred function for prediction
            predicted_class, confidence = pred(user_input)

            # Display the result
            st.subheader("Prediction Result")
            if predicted_class == 1:
                st.success("Epigenetic Mark detected!")
            else:
                st.info("No epigenetic mark found.")

            # Display progress bars with percentages
            st.subheader("Class Distribution")
            st.write("1 - Epigenetic mark found")
            st.progress(confidence)
            st.text(f"{confidence * 100:.2f}%")
            
            st.write("0 - Epigenetic mark not found")
            st.progress(1 - confidence)
            st.text(f"{(1 - confidence) * 100:.2f}%")

        else:
            st.warning("Please enter a DNA sequence for classification.")


# In[5]:


# Function for prediction
def pred(sequence):
    encoded_input = tokenizer(sequence, return_tensors='pt')
    
    # Pass the encoded input through the model
    with torch.no_grad():
        outputs = model(input_ids=encoded_input['input_ids'], attention_mask=encoded_input['attention_mask'])
        logits = outputs[0]
        predicted_class = logits.argmax(-1).item()
        confidence = logits.softmax(dim=-1)[0, 1].item()

    return predicted_class, confidence


# In[6]:


if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




