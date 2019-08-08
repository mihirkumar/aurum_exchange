pragma solidity ^0.5.0;

import "./ERC20.sol";
import "./SafeMath.sol";
import "./ERC20Mintable.sol";

contract MyToken is ERC20, ERC20Mintable {}