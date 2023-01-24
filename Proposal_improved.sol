pragma solidity ^0.5.0;

contract Proposal {
    address owner;
    bool proposalMade;

    constructor() public {
        owner = msg.sender;
    }

    struct ProposalInfo {
        string content;
    }

    ProposalInfo public proposal;

    function makeProposal(string memory _content) public {
        require(msg.sender == owner, "Only the contract owner can make a proposal.");
        require(!proposalMade, "A proposal has already been made.");
        proposal = ProposalInfo(_content);
        proposalMade = true;
    }

    function getInfo() public view returns (string memory) {
        return proposal.content;
    }
}