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


### Voting Contract

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


### Addresses for Voting

contract_address_1 = os.getenv("SMART_CONTRACT_ADDRESS_1")

contract_address_2 = os.getenv("SMART_CONTRACT_ADDRESS_2")

contract_address_3 = os.getenv("SMART_CONTRACT_ADDRESS_3")

################################################################################
# Voting System
################################################################################

st.title("Voting System")
st.write("Choose an account to get started")
accounts = w3.eth.accounts
address = st.selectbox("Select Account", options=accounts)
st.markdown("---")

### See all proposals

st.title("See all Proposals")

if st.button("Click here"):
    result_1 = contract_1.functions.getInfo().call()
    st.write("#### Proposal 1: ", result_1[1])
    result_2 = contract_2.functions.getInfo().call()
    st.write("#### Proposal 2: ", result_2[1])
    result_3 = contract_3.functions.getInfo().call()
    st.write("#### Proposal 3: ", result_3[1])

st.write("## Vote for Proposal 1")

if st.button("Vote Proposal 1"):
    try:
        tx_hash = contract_token.functions.transfer(contract_address_1, 1).transact({'from': address, 'gas': 1000000})

    except ValueError as error:
        if 'message' in error.args[0] and 'revert ERC20: transfer amount exceeds balance' in error.args[0]['message']:
            st.write("You do not have the power to vote!")
        else:
            raise error

st.write("## Vote for Proposal 2")

if st.button("Vote Proposal 2"):
    try:
        tx_hash = contract_token.functions.transfer(contract_address_2, 1).transact({'from': address, 'gas': 1000000})

    except ValueError as error:
        if 'message' in error.args[0] and 'revert ERC20: transfer amount exceeds balance' in error.args[0]['message']:
            st.write("You do not have the power to vote!")
        else:
            raise error

st.write("## Vote for Proposal 3")

if st.button("Vote Proposal 3"):
    try: 
        tx_hash = contract_token.functions.transfer(contract_address_3, 1).transact({'from': address, 'gas': 1000000})

    except ValueError as error:
        if 'message' in error.args[0] and 'revert ERC20: transfer amount exceeds balance' in error.args[0]['message']:
            st.write("You do not have the power to vote!")
        else:
            raise error

st.title("See Vote Tally")

if st.button("Vote Tally"):
    result_proposal_1 = contract_token.functions.balanceOf(contract_address_1).call()
    st.write("#### Proposal 1: ", result_proposal_1)
    result_proposal_2 = contract_token.functions.balanceOf(contract_address_2).call()
    st.write("#### Proposal 2: ",  result_proposal_2)
    result_proposal_3 = contract_token.functions.balanceOf(contract_address_3).call()
    st.write("#### Proposal 3: ", result_proposal_3)



