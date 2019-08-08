pragma solidity ^0.5.0;

contract ETHEscrowInterface {
    
    enum State {OPEN, PUZZLE, CLOSED}
    
    State public currentState;
    
    address public tokenAddress;
    address payable public seller;
    
    uint256 public timeLimit;
    
    bytes32 public puzzle = 0xc505fe01b44140477f4a6ccad01f4b21f34243e809c0717e6cef4283b04359fa;
    
    modifier onlySeller { require(msg.sender == seller); _; }
    modifier onlyTimeout { require(now >= timeLimit); _; }

    constructor(address payable _seller, uint256 _timeLimit) public {
        seller = _seller;
        timeLimit = _timeLimit;
        currentState = State.OPEN;
    }
    
    function () external payable {}
    
    function confirmDeposit() public returns(bool){
        currentState = State.PUZZLE;
        return true;
    }
    
    function withdraw(address payable _to, string memory _key) public {
        require(puzzle == sha256(abi.encodePacked(_key)));
        _to.transfer(address(this).balance);
        currentState = State.CLOSED;
    }
    
    function refund() onlySeller onlyTimeout public {
        seller.transfer(address(this).balance);
        currentState = State.CLOSED;
    }
    
    function setLargerTimeLimit(uint256 _newTimeLimit) onlySeller public {
        require(_newTimeLimit > timeLimit);
        timeLimit = _newTimeLimit;
    }
}