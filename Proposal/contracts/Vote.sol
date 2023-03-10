pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Detailed.sol";

contract VoteToken is ERC20, ERC20Detailed {
    address payable owner;

    modifier onlyOwner {
        require(msg.sender == owner, "You do not have permission to mint these tokens!");
        _;
    }

    constructor(uint initial_supply) ERC20Detailed("VoteToken", "VOTE", 0) public {
        owner = msg.sender;
        _mint(owner, initial_supply);
    }

    function mintToMultiple(address[] memory recipients, uint amount) public onlyOwner { // Allowing minting to multiple addresses at once
        for (uint i = 0; i < recipients.length; i++) 
        _mint(recipients[i], amount);
    }

    function mint(address recipient, uint amount) public onlyOwner {
        _mint(recipient, amount);
    }
    
}