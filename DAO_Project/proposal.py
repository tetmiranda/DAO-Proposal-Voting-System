import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

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

count1 = 0
count2 = 0
count3 = 0

### Proposal 1

st.title("Register Proposal 1")
proposal_1 = st.text_input("Enter the first proposal")

if st.button("Register Proposal 1"):
    tx_hash = contract_1.functions.makeProposal(address, proposal_1).transact({'from': address, 'gas': 1000000})
    count1 += 1

if st.button("See Proposal 1"):
    result = contract_1.functions.getInfo().call()
    st.write("#### Proposal 1: ", result[1])

### Proposal 2

st.title("Register Proposal 2")
proposal_2 = st.text_input("Enter the second proposal")

if st.button("Register Proposal 2"):
    tx_hash = contract_2.functions.makeProposal(address, proposal_2).transact({'from': address, 'gas': 1000000})
    count2 += 1

if st.button("See Proposal 2"):
    result = contract_2.functions.getInfo().call()
    st.write("#### Proposal 2: ", result[1])

### Proposal 3

st.title("Register Proposal 3")
proposal_3 = st.text_input("Enter the third proposal")

if st.button("Register Proposal 3"):
    tx_hash = contract_3.functions.makeProposal(address, proposal_3).transact({'from': address, 'gas': 1000000})
    count3 += 1

if st.button("See Proposal 3"):
    result = contract_3.functions.getInfo().call()
    st.write("#### Proposal 3: ", result[1])

### See all proposals

st.title("Proposal Vote Count")

st.write("Votes for Proposal 1: ", count1)
st.write("Votes for Proposal 2: ", count2)
st.write("Votes for Proposal 3: ", count3)