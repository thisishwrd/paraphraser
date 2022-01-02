# -*- coding: utf-8 -*-
# ! pip install streamlit -q
# ! npm install -g localtunnel
# ! pip install pyngrok
# ! pip install git+https://github.com/PrithivirajDamodaran/Parrot_Paraphraser.git


from parrot import Parrot
import torch
import streamlit as st
import warnings
warnings.filterwarnings("ignore")

PAGE_CONFIG = {"page_title":"Paraphraser","page_icon":":smiley:","layout":"centered"}
st.set_page_config(**PAGE_CONFIG)

# For reproducibility
def random_state(seed):
  torch.manual_seed(seed)
  if torch.cuda.is_available():
    torch.cuda.manual_seed_all(seed)

random_state(1234)


def main():

    st.title("Automatic generator of paraphrases")
    st.subheader("This web app takes a sentence and an integer N as input and paraphrases the input sentence N times.")

    sentence = ""
    # numbInput = 0
    button_result = False


    st.text("Please add the sentence you want to have paraphrased below:")
    sentence = st.text_input('Input sentence', "")
    # numbInput = st.slider("Enter the number of new sentences you'd like:", min_value=1, max_value=20, value=1, step=1)
    # numbInput = int(numbInput)

    st.text("Click the button to see the result")

    if st.button('Click for results'):
      try:
        with st.spinner('Running model...'):
         
          parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5", use_gpu=True)
          para_phrases = parrot.augment(input_phrase=sentence,
                                      max_return_phrases = 20)
          
        st.text("-"*100)
        st.text("Paraphrased sentences for '%s'" %(sentence))
        st.text("-"*100)
        
        for para_phrase in para_phrases:
          st.text(para_phrase[0])
          
      except:
        st.error("Oops! Looks like this algorithm does't work.\
                  We'll need to fix it!")
  
if __name__ == '__main__':
    main()
