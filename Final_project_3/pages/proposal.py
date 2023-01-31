import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st
import base64
from PIL import Image
from streamlit.components.v1 import html

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
add_bg_from_local('IMG_9426.jpg')


image = Image.open('proposal.png')
st.image(image, caption='# ') 



################################################################################
# Load_Contract Function
################################################################################
load_dotenv()

# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

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
    tx_hash = contract_1.functions.makeProposal(address, proposal_1).transact({'from': address, 'gas': 1000000})

if st.button("See Proposal 1"):
    result = contract_1.functions.getInfo().call()
    st.write("#### Proposal 1: ", result[1])

### Proposal 2

st.title("Register Proposal 2")
proposal_2 = st.text_input("Enter the second proposal")

if st.button("Register Proposal 2"):
    tx_hash = contract_2.functions.makeProposal(address, proposal_2).transact({'from': address, 'gas': 1000000})

if st.button("See Proposal 2"):
    result = contract_2.functions.getInfo().call()
    st.write("#### Proposal 2: ", result[1])

### Proposal 3

st.title("Register Proposal 3")
proposal_3 = st.text_input("Enter the third proposal")

if st.button("Register Proposal 3"):
    tx_hash = contract_3.functions.makeProposal(address, proposal_3).transact({'from': address, 'gas': 1000000})

if st.button("See Proposal 3"):
    result = contract_3.functions.getInfo().call()
    st.write("#### Proposal 3: ", result[1])

### See all proposals

st.title("See all Proposals")

if st.button("Click here"):
    result_1 = contract_1.functions.getInfo().call()
    st.write("#### Proposal 1: ", result_1[1])
    result_2 = contract_2.functions.getInfo().call()
    st.write("#### Proposal 2: ", result_2[1])
    result_3 = contract_3.functions.getInfo().call()
    st.write("#### Proposal 3: ", result_3[1])

################################################################################
# Function navigation to the next page
################################################################################

def nav_page(page_name, timeout_secs=3):
    nav_script = """
        <script type="text/javascript">
            function attempt_nav_page(page_name, start_time, timeout_secs) {
                var links = window.parent.document.getElementsByTagName("a");
                for (var i = 0; i < links.length; i++) {
                    if (links[i].href.toLowerCase().endsWith("/" + page_name.toLowerCase())) {
                        links[i].click();
                        return;
                    }
                }
                var elasped = new Date() - start_time;
                if (elasped < timeout_secs * 1000) {
                    setTimeout(attempt_nav_page, 100, page_name, start_time, timeout_secs);
                } else {
                    alert("Unable to navigate to page '" + page_name + "' after " + timeout_secs + " second(s).");
                }
            }
            window.addEventListener("load", function() {
                attempt_nav_page("%s", new Date(), %d);
            });
        </script>
    """ % (page_name, timeout_secs)
    html(nav_script)


st.title("Now Let's Vote")
if st.button("To Vote"):
    nav_page("vote")