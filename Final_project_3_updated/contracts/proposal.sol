pragma solidity ^0.5.0;

contract Proposal {
    address owner;
    string proposalMade;

    constructor() public {
        owner = msg.sender;
    }

    struct ProposalInfo {
        address sender;
        string content;
        
        
    }

    ProposalInfo public proposal;

    function makeProposal(address _sender, string memory _content) public {
    require(msg.sender == owner, "Only the contract owner can make a proposal.");
    proposal = ProposalInfo(_sender, _content);

}

    function getInfo() public view returns (address, string memory) {
        return (proposal.sender, proposal.content);
    }
}