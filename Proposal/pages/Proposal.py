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


image = Image.open('proposal.png')
st.image(image, caption='# ') 

# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

################################################################################
# Load_Contract Function
################################################################################


### Contract 1

@st.cache(allow_output_mutation=True)
def load_contract_1():

    # Load the contract ABI
    with open(Path('./contracts/compiled/proposal_abi.json')) as f:
        contract_abi = json.load(f)

    # Set the contract address's of each proposal contract

    contract_address_1 = os.getenv("SMART_CONTRACT_ADDRESS_1")

# Get the contract
    contract_1 = w3.eth.contract(
        address=contract_address_1,
        abi=contract_abi
    )

    return contract_1

    
# Load the contract
contract_1 = load_contract_1()

### Contract 2

@st.cache(allow_output_mutation=True)
def load_contract_2():

    # Load the contract ABI
    with open(Path('./contracts/compiled/proposal_abi.json')) as f:
        contract_abi = json.load(f)

    # Set the contract address's of each proposal contract

    contract_address_2 = os.getenv("SMART_CONTRACT_ADDRESS_2")

# Get the contract
    contract_2 = w3.eth.contract(
        address=contract_address_2,
        abi=contract_abi
    )

    return contract_2

    
# Load the contract
contract_2 = load_contract_2()

### Contract 3

@st.cache(allow_output_mutation=True)
def load_contract_3():

    # Load the contract ABI
    with open(Path('./contracts/compiled/proposal_abi.json')) as f:
        contract_abi = json.load(f)

    # Set the contract address's of each proposal contract

    contract_address_3 = os.getenv("SMART_CONTRACT_ADDRESS_3")

# Get the contract
    contract_3 = w3.eth.contract(
        address=contract_address_3,
        abi=contract_abi
    )

    return contract_3

    
# Load the contract
contract_3 = load_contract_3()

################################################################################
# Setting up streamlit interface
################################################################################

st.title("Proposal Registry System")
st.write("Choose an account to get started")
accounts = w3.eth.accounts
address = st.selectbox("Select Account", options=accounts)
st.markdown("---")

### Proposal 1

st.title("Register Proposal 1")
proposal_1 = st.text_input("Enter the first proposal")

if st.button("Register Proposal 1"):
    try:
        tx_hash = contract_1.functions.makeProposal(address, proposal_1).transact({'from': address, 'gas': 1000000})

    except ValueError as error:
        if 'message' in error.args[0] and 'revert Only the contract owner can make a proposal' in error.args[0]['message']:
            st.write("You are not permitted to make a proposal.")
    else:
        if proposal_1:
             st.write("Proposal 1: " + proposal_1)


### Proposal 2

st.title("Register Proposal 2")
proposal_2 = st.text_input("Enter the second proposal")

if st.button("Register Proposal 2"):
    try: 
        tx_hash = contract_2.functions.makeProposal(address, proposal_2).transact({'from': address, 'gas': 1000000})
    
    except ValueError as error:
        if 'message' in error.args[0] and 'revert Only the contract owner can make a proposal' in error.args[0]['message']:
            st.write("You are not permitted to make a proposal.")
    else:
        if proposal_2:
             st.write("Proposal 2: " + proposal_2)

### Proposal 3

st.title("Register Proposal 3")
proposal_3 = st.text_input("Enter the third proposal")

if st.button("Register Proposal 3"):
    try: 
        tx_hash = contract_3.functions.makeProposal(address, proposal_3).transact({'from': address, 'gas': 1000000})
    
    except ValueError as error:
        if 'message' in error.args[0] and 'revert Only the contract owner can make a proposal' in error.args[0]['message']:
            st.write("You are not permitted to make a proposal.")
    else:
        if proposal_3:
             st.write("Proposal 3: " + proposal_3)


### See all proposals

st.title("See all Proposals")

if st.button("Click here"):
    result_1 = contract_1.functions.getInfo().call()
    st.write("#### Proposal 1: ", result_1[1])
    result_2 = contract_2.functions.getInfo().call()
    st.write("#### Proposal 2: ", result_2[1])
    result_3 = contract_3.functions.getInfo().call()
    st.write("#### Proposal 3: ", result_3[1])

