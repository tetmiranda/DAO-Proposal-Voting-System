import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st
import base64
from PIL import Image
from streamlit.components.v1 import html

load_dotenv()


################################################################################
# Function adding background to the streamlit page
################################################################################

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('background.jpg')


image = Image.open('token.jpg')
st.image(image, caption='# ') 


# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

################################################################################
# Load_Contract Function
################################################################################

### Token Contract

@st.cache(allow_output_mutation=True)
def load_contract_token():

    # Load the contract ABI
    with open(Path('./contracts/compiled/vote_abi.json')) as f:
        contract_abi = json.load(f)

    # Set the contract address's of each proposal contract

    contract_address_token = os.getenv("SMART_CONTRACT_ADDRESS_TOKEN")

# Get the contract
    contract_token = w3.eth.contract(
        address=contract_address_token,
        abi=contract_abi
    )

    return contract_token

# Load the contract
contract_token = load_contract_token()

##################################################################################
## Token Minting System (contract deployer only)
##################################################################################

### Select account

st.title("Token Minting")
accounts = w3.eth.accounts
address = st.selectbox("Select your Account", options=accounts)

st.markdown("---")

### Single address token minting

st.title("Single Address Minting")

single_address = st.text_input("Enter the address you wish to mint the token(s) to:")

amount = st.text_input("Enter the amount of VOTE tokens you would like to mint:", value='0')
try:
    amount = float(amount)
    amount = int(round(amount))
except ValueError:
    st.write("Invalid input. Please enter a number.")

if st.button("Mint tokens"):
    try:
        tx_hash = contract_token.functions.mint(single_address, amount).transact({'from': address, 'gas': 1000000})
        st.write("You've successfully minted " + str(amount) + " VOTE token(s).")
    
    except ValueError as error:
        if 'message' in error.args[0] and 'revert You do not have permission to mint these tokens!' in error.args[0]['message']:
            st.write("You are not permitted to mint tokens.")

st.markdown("---")

### Multiple address token minting

st.title("Multiple Address Minting")

addresses_input = st.text_input("Enter the addresses you wish to mint the tokens to (separated by a comma):")
recipients = [address.strip() for address in addresses_input.split(',')]

amount_multiple = st.text_input("Enter the amount of VOTE tokens you would like to mint to each address:", value='0')
try:
    amount_multiple = float(amount_multiple)
    amount_multiple = int(round(amount_multiple))
except ValueError:
    st.write("Invalid input. Please enter a number.")

if st.button("Mint token(s)"):
    try: 
        tx_hash = contract_token.functions.mintToMultiple(recipients, amount_multiple).transact({'from': address, 'gas': 1000000})
        st.write("You've successfully minted " + str(amount_multiple) + " VOTE tokens to the following addresses: " + str(recipients))

    except ValueError as error:
        if 'message' in error.args[0] and 'revert You do not have permission to mint these tokens!' in error.args[0]['message']:
            st.write("You are not permitted to mint tokens.")        

