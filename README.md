# Project 3 - Group 3

![proj3_group3_final](Images/proj3_group3_final.png)

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

This project aims to create an DAO application on the blockchain that allows users to submit new proposals for their organization, voting on said proposals, and execution of proposals. 

### Methods

The project will consist of minting new tokens on the Ethereum network, which will then be distributed to eligible candidates. These new tokens will be used for voting on proposals put forth by other eligible users by coin holders depositing their tokens into a polling wallet.

* Distribute ERC20 token “VoteCoin” to eligible users.
* Setup proposal contract, whereby the contract deployer can make one proposal per contract that represents what you are voting on (can be seen via GetInfo() call) e.g. 3 addresses for 3 different devs to potentially hire (Streamlit frontend shows which address represents who) - store extended details of proposal on IPFS.

* Voters send their token to who they want to vote for (tokens are restricted to being sent to the eligible addresses ie can’t be sent to random addresses.)
  * Basic functionality: 1 token = 1 vote (only whole numbers of tokens can be sent - set decimals to 0)
  * Added features: Able to send multiple tokens to vote on selected proposal
* Check total supply of each address
Highest total supply of token in address wins.


### Languages / Tools / Resources Used:

* Smart Contracts: Solidity using Remix IDE
* ABI (Application Binary Interface) file in JSON format
* Metamask: store (vote) tokens, interact with decentralized application
* Pinata to store Smart Contracts events and capture the total votes
* VS Code for Python for Streamlit front-end


### Streamlit Frontend:

We will be using Streamlit for our frontend to create a simpler and more professional interface that anyone of any skill level will be able to interact with.

* Proposals
* Selecting wallet
* Checking if how many vote tokens the address holds
* Receiving wallet address (smart contract where proposals are held)
* Vote tally, everytime a vote is cast it automatically updates.


Steps to run Onchain Voting.
1. Create accounts in Metamask


## Demonstration

![token_minting](Images/Token.gif)




