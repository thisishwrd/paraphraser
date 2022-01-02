# -*- coding: utf-8 -*-
pip install streamlit -q
!npm install -g localtunnel
!pip install pyngrok
!pip install git+https://github.com/PrithivirajDamodaran/Parrot_Paraphraser.git


from pyngrok import ngrok
from parrot import Parrot
import torch
import warnings
warnings.filterwarnings("ignore")

# For reproducibility
def random_state(seed):
  torch.manual_seed(seed)
  if torch.cuda.is_available():
    torch.cuda.manual_seed_all(seed)

random_state(1234)

# Commented out IPython magic to ensure Python compatibility.
%%writefile app.py
import streamlit as st
from parrot import Parrot
import warnings
warnings.filterwarnings("ignore")


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
      st.text("Here we go...")

      parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5", use_gpu=True)

      para_phrases = parrot.augment(input_phrase=sentence,
                                      max_return_phrases = 20)

      st.text("-"*100)
      st.text("Paraphrased sentences for '%s'" %(sentence))
      st.text("-"*100)

      for para_phrase in para_phrases:
        st.text(para_phrase[0])

if __name__ == '__main__':
    main()


# substitute private ngrok token for TOKEN below and uncomment
!ngrok authtoken 232fN5BEH6Z0Bgkh5oQODhJeVFn_4Y8FZuHzMM3TiS3CMLVyC

!streamlit run --server.port 80 app.py &>/dev/null&
!pgrep streamlit

public_url = ngrok.connect(port='80')
public_url

# ! python -m http.server 80
# ! ngrok  http 80



# !ngrok_kill()
