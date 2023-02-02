import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st
import time

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


### Contract addresses to cast votes to

contract_address_1 = os.getenv("SMART_CONTRACT_ADDRESS_1")

contract_address_2 = os.getenv("SMART_CONTRACT_ADDRESS_2")

contract_address_3 = os.getenv("SMART_CONTRACT_ADDRESS_3")

################################################################################
# Voting System
################################################################################

st.title("Voting System")
accounts = w3.eth.accounts
address = st.selectbox("Select your Account", options=accounts)

## Check balance of voting token for selected address

token_balance = contract_token.functions.balanceOf(address).call()
st.write("##### Token Balance:", token_balance)
st.markdown("---")

### See all proposals

st.title("Proposals")

result_1 = contract_1.functions.getInfo().call()
st.write("#### Proposal 1: ", result_1[1])
result_2 = contract_2.functions.getInfo().call()
st.write("#### Proposal 2: ", result_2[1])
result_3 = contract_3.functions.getInfo().call()
st.write("#### Proposal 3: ", result_3[1])
st.markdown("---")


### Vote for proposal

st.title("Vote")

vote_power = st.text_input("Enter the amount of tokens you wish to vote with:", value = "0")
try:
    vote_power = float(vote_power)
    vote_power = int(round(vote_power))
except ValueError:
    st.write("Invalid input. Please enter a number.")

st.markdown("---")

if st.button("Vote Proposal 1"):
    try:
        tx_hash = contract_token.functions.transfer(contract_address_1, vote_power).transact({'from': address, 'gas': 1000000})
        st.write("You've succesfully voted for Proposal 1 with " + str(vote_power) + " Vote tokens.")

    except ValueError as error:
        if 'message' in error.args[0] and 'revert ERC20: transfer amount exceeds balance' in error.args[0]['message']:
            st.write("You do not have the power to vote!")
        else:
            raise error


if st.button("Vote Proposal 2"):
    try:
        tx_hash = contract_token.functions.transfer(contract_address_2, 1).transact({'from': address, 'gas': 1000000})
        st.write("You've succesfully voted for Proposal 2 with " + str(vote_power) + " Vote tokens.")

    except ValueError as error:
        if 'message' in error.args[0] and 'revert ERC20: transfer amount exceeds balance' in error.args[0]['message']:
            st.write("You do not have the power to vote!")
        else:
            raise error


if st.button("Vote Proposal 3"):
    try: 
        tx_hash = contract_token.functions.transfer(contract_address_3, 1).transact({'from': address, 'gas': 1000000})
        st.write("You've succesfully voted for Proposal 3 with " + str(vote_power) + " Vote tokens.")
        
    except ValueError as error:
        if 'message' in error.args[0] and 'revert ERC20: transfer amount exceeds balance' in error.args[0]['message']:
            st.write("You do not have the power to vote!")
        else:
            raise error

### Vote Tally

st.markdown("---")
st.title("Vote Tally")

result_proposal_1 = contract_token.functions.balanceOf(contract_address_1).call()
st.write("#### Proposal 1: ", result_proposal_1)
result_proposal_2 = contract_token.functions.balanceOf(contract_address_2).call()
st.write("#### Proposal 2: ",  result_proposal_2)
result_proposal_3 = contract_token.functions.balanceOf(contract_address_3).call()
st.write("#### Proposal 3: ", result_proposal_3)



