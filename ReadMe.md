# DAO Proposal & Voting System

![DAO_image](Images/DAO.jpeg)

# The Team
* Viktoria Osipova - Project Leader
* Dennis Mader - Lead Coder
* Lachlan Andrews - Support Coder/Beta Tester
* David Newman - Lead Presenter/Graphic Designer
* Florante Miranda - Git Master

# Project Goal

Build and demonstrate a decentralized autonomous organization (DAO) application on the Ethereum blockchain coupled with Streamlit for front-end functionality.


# About The Project

## Onchain Voting - DAO Application on a blockchain

Annual general meetings are a laborious necessity for corporate governance. However, this process is plagued with issues that can make decision making tricky. Nevertheless, with the advent of blockchain, this no longer has to be the case. A DAO is an entity with no central authority. It is a fully autonomous/transparent smart contract with several key features such as:
lays the foundational rules for the organization 
Permits the execution of agreed upon decisions
Allows members to put forth proposals for other members to vote on
Is immutable

This project aims to create an DAO application on the blockchain that allows proposals to be submitted with users voting on said proposals using an ERC20 token. 

### Methods

The project will consist of minting new ERC20 tokens on the Ethereum network, which will then be distributed to eligible candidates. These tokens will be used for voting on proposals put forth by the head of the DAO.

* Distribute ERC20 token VOTE to eligible users.
* Setup proposal contract, whereby the contract deployer can make one proposal per contract that represents what you are voting on (can be seen via GetInfo() call) e.g. 3 addresses for 3 different devs to potentially hire (Streamlit frontend shows which address represents who)

* Voters send their token to who they want to vote for
  * Basic functionality: 1 token = 1 vote (only whole numbers of tokens can be sent)
  * Added features: Able to send multiple tokens to vote on selected proposal
* Check total supply of each address
* Highest total supply of token in one of the proposal smart contracts wins.



### Streamlit Frontend:

We will be using Streamlit for our frontend to create a simpler and more professional interface that anyone of any skill level will be able to interact with.

* Minting tokens to addresses
* Creating proposals
* Voting on proposals using tokens
* Tallying number of votes for each proposal


### Steps to run Onchain Voting

1. Download all resources in Proposal folder.
2. Create accounts in Metamask using Ganache. 
3. Deploy Token.sol and three Proposal.sol smart contracts through Remix (recommended to use one address for all deployment).
4. Setup .env file with newly created smart contract addresses;
   SMART_CONTRACT_ADDRESS_1, SMART_CONTRACT_ADDRESS_2, SMART_CONTRACT_ADDRESS_3 are the variables for the proposal contract        addresses.
   SMART_CONTRACT_ADDRESS_TOKEN is the variable for the Vote token address.
5. Run streamlit interface.

Now you can mint tokens, create proposals onchain and vote for the proposals you like.


## Demonstration

### Token Minting
------

![token_minting](Images/Token.gif)

Here is an overview of the token minting process. Only the smart contract deployer of Token.sol has control over the minting process and is able to mint to a single or multiple addresses in one transaction (via the mint() or mintToMultiple() functions respectively). If minting is successful, there will be a confirmation of the amount of tokens minted and to which addresses they were sent to.

### Creating Proposals
------

![creating_proposals](Images/Proposal.gif)

Similarly, the proposal registry system can only be controlled by the smart contract deployer, and in our example we use the same address as the Token Deployer. Select the account that deployed the Proposal.sol smart contract. Now you are able to create three different proposals which are stored onchain via the makeProposal() function and are called back to the streamlit interface via the GetInfo() call function.

### Voting
------

![voting](Images/Vote.gif)

We have finally come up to the most exciting part, its time to vote! As shown above, the proposals are displayed again via the GetInfo() call function and the current vote tally is 0. This tally is obtained by calling the BalanceOf() call function of each smart contract which shows how many tokens have accumalated in each proposal contract. We can then select the accounts that hold tokens and vote with them. Input the desired amount of tokens you wish to vote with and click Vote for Proposal X. This then transfers the desired amount of tokens from the selected address to the selected Proposal contract via the transfer() function. The tally is then automatically updated with the new balances of tokens in each proposal contract.




### Languages / Tools / Resources Used:

* Smart Contracts: Solidity using Remix IDE
* Ganache: setup wallets & addresses
* ABI (Application Binary Interface) file in JSON format
* Metamask: interact with decentralized application
* VS Code for Streamlit front-end







