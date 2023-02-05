import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st
import time
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
add_bg_from_local('background.jpg')


image = Image.open('token.jpg')
st.image(image, caption='# ') 

load_dotenv()

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

st.title("Token Minting")
accounts = w3.eth.accounts
address = st.selectbox("Select your Account", options=accounts)

st.markdown("---")

st.title("Single Address Minting")

single_address = st.text_input("Enter the address you wish to mint the token(s) to:")

amount = st.text_input("Enter the amount of VOTE tokens you would like to mint:", value='0')
amount = int(amount)

if st.button("Mint tokens"):
    tx_hash = contract_token.functions.mint(single_address, amount).transact({'from': address, 'gas': 1000000})
    st.write("You've successfully minted " + str(amount) + " VOTE tokens.")

st.markdown("---")

st.title("Multiple Address Minting")

addresses_input = st.text_input("Enter the addresses you wish to mint the tokens to (separated by a comma):")
recipients = [address.strip() for address in addresses_input.split(',')]

amount_multiple = st.text_input("Enter the amount of VOTE tokens you would like to mint to each address:", value='0')
amount_multiple = int(amount_multiple)

if st.button("Mint token(s)"):
    tx_hash = contract_token.functions.mintToMultiple(recipients, amount_multiple).transact({'from': address, 'gas': 1000000})
    st.write("You've successfully minted " + str(amount_multiple) + " VOTE tokens to the following addresses: " + str(recipients))

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