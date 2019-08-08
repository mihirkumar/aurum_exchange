pragma solidity ^0.5.0;

import "./testToken.sol";

contract ERC20EscrowInterface {
    
    enum State {OPEN, PUZZLE, CLOSED}
    
    State public currentState;
    
    address public tokenAddress;
    address public seller;
    
    uint256 public timeLimit;
    
    bytes32 public puzzle = 0xa915bf1b0b6afbe466bcb10c0711cc2ed6023e5501bc6958fc0acb502e10c31a;
    
    modifier onlySeller { require(msg.sender == seller); _; }
    modifier onlyTimeout { require(now >= timeLimit); _; }

    constructor(address _tokenAdd, address _seller, uint256 _timeLimit) public {
        tokenAddress = _tokenAdd;
        seller = _seller;
        timeLimit = _timeLimit;
        currentState = State.OPEN;
    }
    
    function confirmDeposit() payable public returns(bool){
        currentState = State.PUZZLE;
        return true;
    }
    
    function withdraw(address _to, string memory _key) public {
        require(puzzle == sha256(abi.encodePacked(_key)));
        MyToken myToken = MyToken(tokenAddress);
        myToken.transfer(_to, myToken.balanceOf(address(this)));
        currentState = State.CLOSED;
    }
    
    function refund() onlySeller onlyTimeout public {
        MyToken myToken = MyToken(tokenAddress);
        myToken.transfer(seller, myToken.balanceOf(address(this)));
        currentState = State.CLOSED;
    }
    
    function setLargerTimeLimit(uint256 _newTimeLimit) onlySeller public {
        require(_newTimeLimit > timeLimit);
        timeLimit = _newTimeLimit;
    }
}