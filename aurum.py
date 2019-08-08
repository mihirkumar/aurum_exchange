import json, hashlib, sys
from web3 import Web3
from eth_account import Account

# Set up web3 connection with Ganache
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

abc_abi = json.loads('[ { "constant": false, "inputs": [ { "name": "account", "type": "address" } ], "name": "addMinter", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "account", "type": "address" } ], "name": "addOperator", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "spender", "type": "address" }, { "name": "value", "type": "uint256" } ], "name": "approve", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "spender", "type": "address" }, { "name": "value", "type": "uint256" } ], "name": "approveAndCall", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "spender", "type": "address" }, { "name": "value", "type": "uint256" }, { "name": "data", "type": "bytes" } ], "name": "approveAndCall", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "amount", "type": "uint256" } ], "name": "burn", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "account", "type": "address" }, { "name": "amount", "type": "uint256" } ], "name": "burnFrom", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "spender", "type": "address" }, { "name": "subtractedValue", "type": "uint256" } ], "name": "decreaseAllowance", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [], "name": "enableTransfer", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [], "name": "finishMinting", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "spender", "type": "address" }, { "name": "addedValue", "type": "uint256" } ], "name": "increaseAllowance", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "to", "type": "address" }, { "name": "value", "type": "uint256" } ], "name": "mint", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "tokenAddress", "type": "address" }, { "name": "tokenAmount", "type": "uint256" } ], "name": "recoverERC20", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "account", "type": "address" } ], "name": "removeMinter", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "account", "type": "address" } ], "name": "removeOperator", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [], "name": "renounceMinter", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [], "name": "renounceOperator", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [], "name": "renounceOwnership", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "to", "type": "address" }, { "name": "value", "type": "uint256" } ], "name": "transfer", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "to", "type": "address" }, { "name": "value", "type": "uint256" } ], "name": "transferAndCall", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "to", "type": "address" }, { "name": "value", "type": "uint256" }, { "name": "data", "type": "bytes" } ], "name": "transferAndCall", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "from", "type": "address" }, { "name": "to", "type": "address" }, { "name": "value", "type": "uint256" } ], "name": "transferFrom", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "from", "type": "address" }, { "name": "to", "type": "address" }, { "name": "value", "type": "uint256" }, { "name": "data", "type": "bytes" } ], "name": "transferFromAndCall", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "from", "type": "address" }, { "name": "to", "type": "address" }, { "name": "value", "type": "uint256" } ], "name": "transferFromAndCall", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "newOwner", "type": "address" } ], "name": "transferOwnership", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "name": "name", "type": "string" }, { "name": "symbol", "type": "string" }, { "name": "decimals", "type": "uint8" }, { "name": "cap", "type": "uint256" }, { "name": "initialSupply", "type": "uint256" }, { "name": "transferEnabled", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "constructor" }, { "anonymous": false, "inputs": [], "name": "MintFinished", "type": "event" }, { "anonymous": false, "inputs": [], "name": "TransferEnabled", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "name": "previousOwner", "type": "address" }, { "indexed": true, "name": "newOwner", "type": "address" } ], "name": "OwnershipTransferred", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "name": "account", "type": "address" } ], "name": "OperatorAdded", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "name": "account", "type": "address" } ], "name": "OperatorRemoved", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "name": "account", "type": "address" } ], "name": "MinterAdded", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "name": "account", "type": "address" } ], "name": "MinterRemoved", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "name": "from", "type": "address" }, { "indexed": true, "name": "to", "type": "address" }, { "indexed": false, "name": "value", "type": "uint256" } ], "name": "Transfer", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "name": "owner", "type": "address" }, { "indexed": true, "name": "spender", "type": "address" }, { "indexed": false, "name": "value", "type": "uint256" } ], "name": "Approval", "type": "event" }, { "constant": true, "inputs": [ { "name": "owner", "type": "address" }, { "name": "spender", "type": "address" } ], "name": "allowance", "outputs": [ { "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [ { "name": "account", "type": "address" } ], "name": "balanceOf", "outputs": [ { "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "builtOn", "outputs": [ { "name": "", "type": "string" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "cap", "outputs": [ { "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "decimals", "outputs": [ { "name": "", "type": "uint8" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [ { "name": "account", "type": "address" } ], "name": "isMinter", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [ { "name": "account", "type": "address" } ], "name": "isOperator", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "isOwner", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "mintingFinished", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "name", "outputs": [ { "name": "", "type": "string" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "owner", "outputs": [ { "name": "", "type": "address" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [ { "name": "interfaceId", "type": "bytes4" } ], "name": "supportsInterface", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "symbol", "outputs": [ { "name": "", "type": "string" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "totalSupply", "outputs": [ { "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "transferEnabled", "outputs": [ { "name": "", "type": "bool" } ], "payable": false, "stateMutability": "view", "type": "function" } ]')

abc_bytecode = "60806040526200001e3362000024640100000000026401000000009004565b620002a1565b620000488160036200008e64010000000002620015aa179091906401000000009004565b8073ffffffffffffffffffffffffffffffffffffffff167f6ae172837ea30b801fbfcdd4108aa1d5bf8ff775444fd70256b44e6bf3dfc3f660405160405180910390a250565b620000a982826200017d640100000000026401000000009004565b1515156200011f576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252601f8152602001807f526f6c65733a206163636f756e7420616c72656164792068617320726f6c650081525060200191505060405180910390fd5b60018260000160008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060006101000a81548160ff0219169083151502179055505050565b60008073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff16141515156200024a576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260228152602001807f526f6c65733a206163636f756e7420697320746865207a65726f20616464726581526020017f737300000000000000000000000000000000000000000000000000000000000081525060400191505060405180910390fd5b8260000160008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060009054906101000a900460ff16905092915050565b6117b580620002b16000396000f3fe6080604052600436106100ba576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168063095ea7b3146100bf57806318160ddd1461013257806323b872dd1461015d57806339509351146101f057806340c10f191461026357806370a08231146102d6578063983b2d561461033b578063986502751461038c578063a457c2d7146103a3578063a9059cbb14610416578063aa271e1a14610489578063dd62ed3e146104f2575b600080fd5b3480156100cb57600080fd5b50610118600480360360408110156100e257600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff16906020019092919080359060200190929190505050610577565b604051808215151515815260200191505060405180910390f35b34801561013e57600080fd5b5061014761058e565b6040518082815260200191505060405180910390f35b34801561016957600080fd5b506101d66004803603606081101561018057600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190803573ffffffffffffffffffffffffffffffffffffffff16906020019092919080359060200190929190505050610598565b604051808215151515815260200191505060405180910390f35b3480156101fc57600080fd5b506102496004803603604081101561021357600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190803590602001909291905050506106a7565b604051808215151515815260200191505060405180910390f35b34801561026f57600080fd5b506102bc6004803603604081101561028657600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff1690602001909291908035906020019092919050505061074c565b604051808215151515815260200191505060405180910390f35b3480156102e257600080fd5b50610325600480360360208110156102f957600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610805565b6040518082815260200191505060405180910390f35b34801561034757600080fd5b5061038a6004803603602081101561035e57600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff16906020019092919050505061084d565b005b34801561039857600080fd5b506103a16108fc565b005b3480156103af57600080fd5b506103fc600480360360408110156103c657600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff16906020019092919080359060200190929190505050610907565b604051808215151515815260200191505060405180910390f35b34801561042257600080fd5b5061046f6004803603604081101561043957600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff16906020019092919080359060200190929190505050610a0a565b604051808215151515815260200191505060405180910390f35b34801561049557600080fd5b506104d8600480360360208110156104ac57600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610a21565b604051808215151515815260200191505060405180910390f35b3480156104fe57600080fd5b506105616004803603604081101561051557600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610a3e565b6040518082815260200191505060405180910390f35b6000610584338484610ac5565b6001905092915050565b6000600254905090565b60006105a5848484610d46565b61069c843361069785606060405190810160405280602881526020017f45524332303a207472616e7366657220616d6f756e742065786365656473206181526020017f6c6c6f77616e6365000000000000000000000000000000000000000000000000815250600160008b73ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020546110ca9092919063ffffffff16565b610ac5565b600190509392505050565b6000610742338461073d85600160003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008973ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205461118c90919063ffffffff16565b610ac5565b6001905092915050565b600061075733610a21565b15156107f1576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260308152602001807f4d696e746572526f6c653a2063616c6c657220646f6573206e6f74206861766581526020017f20746865204d696e74657220726f6c650000000000000000000000000000000081525060400191505060405180910390fd5b6107fb8383611216565b6001905092915050565b60008060008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020549050919050565b61085633610a21565b15156108f0576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260308152602001807f4d696e746572526f6c653a2063616c6c657220646f6573206e6f74206861766581526020017f20746865204d696e74657220726f6c650000000000000000000000000000000081525060400191505060405180910390fd5b6108f9816113d3565b50565b6109053361142d565b565b6000610a0033846109fb85606060405190810160405280602581526020017f45524332303a2064656372656173656420616c6c6f77616e63652062656c6f7781526020017f207a65726f000000000000000000000000000000000000000000000000000000815250600160003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008a73ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020546110ca9092919063ffffffff16565b610ac5565b6001905092915050565b6000610a17338484610d46565b6001905092915050565b6000610a3782600361148790919063ffffffff16565b9050919050565b6000600160008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054905092915050565b600073ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff1614151515610b90576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260248152602001807f45524332303a20617070726f76652066726f6d20746865207a65726f2061646481526020017f726573730000000000000000000000000000000000000000000000000000000081525060400191505060405180910390fd5b600073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff1614151515610c5b576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260228152602001807f45524332303a20617070726f766520746f20746865207a65726f20616464726581526020017f737300000000000000000000000000000000000000000000000000000000000081525060400191505060405180910390fd5b80600160008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020819055508173ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff167f8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925836040518082815260200191505060405180910390a3505050565b600073ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff1614151515610e11576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260258152602001807f45524332303a207472616e736665722066726f6d20746865207a65726f20616481526020017f647265737300000000000000000000000000000000000000000000000000000081525060400191505060405180910390fd5b600073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff1614151515610edc576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260238152602001807f45524332303a207472616e7366657220746f20746865207a65726f206164647281526020017f657373000000000000000000000000000000000000000000000000000000000081525060400191505060405180910390fd5b610f8b81606060405190810160405280602681526020017f45524332303a207472616e7366657220616d6f756e742065786365656473206281526020017f616c616e636500000000000000000000000000000000000000000000000000008152506000808773ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020546110ca9092919063ffffffff16565b6000808573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000208190555061101e816000808573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205461118c90919063ffffffff16565b6000808473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020819055508173ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef836040518082815260200191505060405180910390a3505050565b60008383111582901515611179576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825283818151815260200191508051906020019080838360005b8381101561113e578082015181840152602081019050611123565b50505050905090810190601f16801561116b5780820380516001836020036101000a031916815260200191505b509250505060405180910390fd5b5060008385039050809150509392505050565b600080828401905083811015151561120c576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252601b8152602001807f536166654d6174683a206164646974696f6e206f766572666c6f77000000000081525060200191505060405180910390fd5b8091505092915050565b600073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff16141515156112bb576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252601f8152602001807f45524332303a206d696e7420746f20746865207a65726f20616464726573730081525060200191505060405180910390fd5b6112d08160025461118c90919063ffffffff16565b600281905550611327816000808573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205461118c90919063ffffffff16565b6000808473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020819055508173ffffffffffffffffffffffffffffffffffffffff16600073ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef836040518082815260200191505060405180910390a35050565b6113e78160036115aa90919063ffffffff16565b8073ffffffffffffffffffffffffffffffffffffffff167f6ae172837ea30b801fbfcdd4108aa1d5bf8ff775444fd70256b44e6bf3dfc3f660405160405180910390a250565b61144181600361168790919063ffffffff16565b8073ffffffffffffffffffffffffffffffffffffffff167fe94479a9f7e1952cc78f2d6baab678adc1b772d936c6583def489e524cb6669260405160405180910390a250565b60008073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff1614151515611553576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260228152602001807f526f6c65733a206163636f756e7420697320746865207a65726f20616464726581526020017f737300000000000000000000000000000000000000000000000000000000000081525060400191505060405180910390fd5b8260000160008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060009054906101000a900460ff16905092915050565b6115b48282611487565b151515611629576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252601f8152602001807f526f6c65733a206163636f756e7420616c72656164792068617320726f6c650081525060200191505060405180910390fd5b60018260000160008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060006101000a81548160ff0219169083151502179055505050565b6116918282611487565b151561172b576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260218152602001807f526f6c65733a206163636f756e7420646f6573206e6f74206861766520726f6c81526020017f650000000000000000000000000000000000000000000000000000000000000081525060400191505060405180910390fd5b60008260000160008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060006101000a81548160ff021916908315150217905550505056fea165627a7a723058200409eaf60ca12a66494cfaf251d9993d30d82b875186a2d1071285c4f7f2306f0029"

class User:
    def __init__(self, address, privateKey, puzzleKey, ganacheIndex, depositCurrency, expectedCurrency, ERC20EscrowContractAddress, ERC20EscrowContractABI, ETHEscrowContractAddress, ETHEscrowContractABI, depositAmount, expectedAmount, tolerance, ERCtoETHrate, ETHtoERCrate):
        self.address = address
        self.privateKey = privateKey
        self.puzzleKey = puzzleKey
        self.ganacheIndex = ganacheIndex
        self.depositCurrency = depositCurrency
        self.expectedCurrency = expectedCurrency

        self.ERC20EscrowContractAddress = ERC20EscrowContractAddress
        self.ERC20EscrowContractABI = ERC20EscrowContractABI
        if ERC20EscrowContractAddress is None or ERC20EscrowContractABI is None:
            self.ERC20EscrowContract = None
        else:
            self.ERC20EscrowContract = web3.eth.contract(address=self.ERC20EscrowContractAddress, abi=self.ERC20EscrowContractABI)
        
        self.ETHEscrowContractAddress = ETHEscrowContractAddress
        self.ETHEscrowContractABI = ETHEscrowContractABI
        if ETHEscrowContractAddress is None or ETHEscrowContractABI is None:
            self.ETHEscrowContract = None
        else:
            self.ETHEscrowContract = web3.eth.contract(address=self.ETHEscrowContractAddress, abi=self.ETHEscrowContractABI)

        self.depositAmount = depositAmount
        self.expectedAmount = expectedAmount
        self.tolerance = tolerance
        self.ERCtoETHrate = ERCtoETHrate
        self.ETHtoERCrate = ETHtoERCrate
    
    # Getters

    def getAddress(self):
        return self.address

    def getPrivateKey(self):
        return self.privateKey

    def getPuzzleKey(self):
        return self.puzzleKey

    def getGanacheIndex(self):
        return self.ganacheIndex

    def getDepositCurrency(self):
        return self.depositCurrency

    def getExpectedCurrency(self):
        return self.expectedCurrency

    def getERC20EscrowContractAddress(self):
        return self.ERC20EscrowContractAddress

    def getDepositAmount(self):
        return self.depositAmount

    def getExpectedAmount(self):
        return self.expectedAmount

    def getTolerance(self):
        return self.tolerance

    def getERC20EscrowContract(self):
        return self.ERC20EscrowContract

    def getETHEscrowContract(self):
        return self.ETHEscrowContract

    def getETHEscrowContractAddress(self):
        return self.ETHEscrowContractAddress

    def getERCtoETHrate(self):
        return self.ERCtoETHrate

    def getETHtoERCrate(self):
        return self.ETHtoERCrate


    # Setters

    def setAddress(self, address):
        self.address = address

    def setPuzzleKey(self, puzzleKey):
        self.puzzleKey = puzzleKey

    def setGanacheIndex(self, ganacheIndex):
        self.ganacheIndex = ganacheIndex

    def setDepositCurrency(self, depositCurrency):
        self.depositCurrency = depositCurrency

    def setExpectedCurrency(self, expectedCurrency):
        self.expectedCurrency = expectedCurrency

    def setERC20EscrowAddress(self, ERC20EscrowContractAddress):
        self.ERC20EscrowContractAddress = ERC20EscrowContractAddress
        self.ERC20EscrowContract = web3.eth.contract(address=self.ERC20EscrowContractAddress, abi=self.ERC20EscrowContractABI)

    def setERC20EscrowABI(self, ERC20EscrowContractABI):
        self.ERC20EscrowContractABI = ERC20EscrowContractABI
        self.ERC20EscrowContract = web3.eth.contract(address=self.ERC20EscrowContractAddress, abi=self.ERC20EscrowContractABI)

    def setETHEscrowAddress(self, ETHEscrowContractAddress):
        self.ETHEscrowContractAddress = ETHEscrowContractAddress
        self.ETHEscrowContract = web3.eth.contract(address=self.ETHEscrowContractAddress, abi=self.ETHEscrowContractABI)

    def setETHEscrowABI(self, ETHEscrowContractABI):
        self.ETHEscrowContractABI = ETHEscrowContractABI
        self.ETHEscrowContract = web3.eth.contract(address=self.ETHEscrowContractAddress, abi=self.ETHEscrowContractABI)

    def setDepositAmount(self, depositAmount):
        self.depositAmount = depositAmount

    def setExpectedAmount(self, expectedAmount):
        self.expectedAmount = expectedAmount

    def setTolerance(self, tolerance):
        self.tolerance = tolerance

    def setERCtoETHrate(self, newERCtoETHrate):
        self.ERCtoETHrate = newERCtoETHrate

    def setETHtoERCrate(self, newETHtoERCrate):
        self.ETHtoERCrate = newETHtoERCrate

    def updatePrices(self):
        # The reserve can implement an algorithm here of their choice to determine new prices to remain competetive
        return True

class ERC20Token:
    def __init__(self, tokenAddress, abi, bytecode):
        self.tokenAddress = tokenAddress
        self.abi = abi
        self.bytecode = bytecode
        if bytecode is None or abi is None:
            self.contract = None
        else:
            self.contract = web3.eth.contract(address=self.tokenAddress, abi=self.abi, bytecode=self.bytecode)

    # Setters

    def setTokenAddress(self, tokenAddress):
        self.tokenAddress = tokenAddress

    def setABI(self, abi):
        self.abi = abi

    def setBytecode(self, bytecode):
        self.bytecode = bytecode

    # Getters

    def getTokenAddress(self):
        return self.tokenAddress

    def getTokenContract(self):
        return web3.eth.contract(address=self.tokenAddress, abi=self.abi, bytecode=self.bytecode)

class KyberExchange:
    def __init__(self, ERCReserves, ETHReserves):
        self.ERCReserves = ERCReserves
        self.ETHReserves = ETHReserves
    
    # Getters

    def getETHReserves(self):
        return self.ETHReserves

    def getERCReserves(self):
        return self.ERCReserves
    
    # Methods

    def addETHReserve(self, newReserve):
        self.ETHReserves.append(newReserve)
    
    def removeETHReserve(self, reserve):
        self.ETHReserves.remove(reserve)

    def addERCReserve(self, newReserve):
        self.ERCReserves.append(newReserve)
    
    def removeERCReserve(self, reserve):
        self.ERCReserves.remove(reserve)

    def getConversionRates(self, baseCurrency, amountInBaseCurrency):
        lowestPrice = -1;

        desiredCurrency = "ETH" if baseCurrency is "ABC" else "ABC"
        reserves = self.ETHReserves if desiredCurrency is "ETH" else self.ERCReserves

        proposed_deals = []

        for reserve in reserves:
            conversionRate = reserve.getERCtoETHrate() if desiredCurrency is "ETH" else reserve.getETHtoERCrate()
            reserveAvailableBalance = min(conversionRate*amountInBaseCurrency, ABC.getTokenContract().caller.balanceOf(reserve.getAddress()))
            if ABC.getTokenContract().caller.balanceOf(reserve.getAddress()) < conversionRate*amountInBaseCurrency:
                reserve.setDepositAmount(ABC.getTokenContract().caller.balanceOf(reserve.getAddress()))
            proposed_txn_details = {'rate': conversionRate, 'amountInDesiredCurrency': reserveAvailableBalance, 'reserve': reserve}
            proposed_deals.append(proposed_txn_details)

        return proposed_deals
    
    def kyberBestAvailableTrade(self, baseCurrency, amountInBaseCurrency):
        desiredCurrency = "ETH" if baseCurrency is "ABC" else "ABC"
        available_deals = self.getConversionRates(baseCurrency, amountInBaseCurrency)

        best_deal = {}
        best_rate = sys.maxsize

        for deal in available_deals:
            if deal['rate'] < best_rate:
                best_rate = deal['rate']
                best_deal = deal
        
        return best_deal

    def executeSingleKyberTrade(self, sender, baseCurrency, amountInBaseCurrency):
        sender.setDepositCurrency(baseCurrency)
        sender.setDepositAmount(amountInBaseCurrency)
        
        reserve = self.kyberBestAvailableTrade(baseCurrency, amountInBaseCurrency)['reserve']

        user_token_destination = kyberERC if baseCurrency is "ABC" else kyberETH
        reserve_token_destination = kyberETH if baseCurrency is "ABC" else kyberERC

        userFundsLockup = ArwenAtomicSwap(sender, kyberERC) if baseCurrency is "ABC" else ArwenAtomicSwap(sender, kyberETH)
        userFundsLockup.lockERC20InEscrow(sender, kyberERC) if baseCurrency is "ABC" else userFundsLockup.lockETHInEscrow(sender, kyberETH)

        reserveFundsLockup = ArwenAtomicSwap(reserve, kyberETH) if baseCurrency is "ABC" else ArwenAtomicSwap(reserve, kyberERC)
        reserveFundsLockup.lockETHInEscrow(reserve, kyberETH) if baseCurrency is "ABC" else reserveFundsLockup.lockERC20InEscrow(reserve)

        userFundsWithdrawal = ArwenAtomicSwap(sender, kyberETH) if baseCurrency is "ABC" else ArwenAtomicSwap(sender, kyberERC)
        userFundsWithdrawal.withdrawETHInEscrow(sender, kyberETH) if baseCurrency is "ABC" else userFundsLockup.withdrawERC20InEscrow(sender, kyberERC)

        reserveFundsWithdrawal = ArwenAtomicSwap(reserve, kyberERC) if baseCurrency is "ABC" else ArwenAtomicSwap(reserve, kyberETH)
        reserveFundsWithdrawal.withdrawERC20InEscrow(reserve, kyberERC) if baseCurrency is "ABC" else reserveFundsWithdrawal.withdrawETHInEscrow(reserve, kyberETH)

        return True

    def executeFullKyberTrade(self, sender, baseCurrency, amountInBaseCurrency):
        amountLeftToTransact = amountInBaseCurrency

        while (amountLeftToTransact > 0):
            senderBalanceBefore = ABC.getTokenContract().caller.balanceOf(sender.getAddress()) if baseCurrency is "ABC" else web3.eth.getBalance(sender.getAddress())
            self.executeSingleKyberTrade(sender, baseCurrency, amountInBaseCurrency)
            senderBalanceAfter = ABC.getTokenContract().caller.balanceOf(sender.getAddress()) if baseCurrency is "ABC" else web3.eth.getBalance(sender.getAddress())
            amountLeftToTransact = amountLeftToTransact - (senderBalanceBefore - senderBalanceAfter)
        
        return (amountLeftToTransact <= 0)


class ArwenAtomicSwap:
    def __init__(self, user, exchange):
        self.user = user
        self.exchange = exchange

    # Setters

    def setUser(self, user):
        self.user = user
    
    def setExchange(self, exchange):
        self.exchange = exchange

    # Getters

    def getUser(self):
        return user
    
    def getExchange(self):
        return exchange

    def lockERC20InEscrow(self, sender, kyberEscrow = None):
        printNewLine()
        if sender.depositCurrency == "ETH":
            print('Aborting ERC20 fund lockup.')
            return False

        oldActiveAccount = web3.eth.defaultAccount
        web3.eth.defaultAccount = web3.eth.accounts[sender.getGanacheIndex()]

        print('Locking ERC20 tokens in Escrow...')
        print('Sender is ' + sender.getAddress())
        print('Sender balance before: ' + str(ABC.getTokenContract().caller.balanceOf(sender.getAddress())))
        depositAddress = kyberEscrow.getERC20EscrowContractAddress() if kyberEscrow is not None else sender.getERC20EscrowContractAddress()
        sender_balance_before = ABC.getTokenContract().caller.balanceOf(sender.getAddress())
        tx_hash_deposit = ABC.getTokenContract().functions.transfer(depositAddress, sender.getDepositAmount()).transact() #test
        tx_deposit_receipt = web3.eth.waitForTransactionReceipt(tx_hash_deposit)
        sender_balance_after = ABC.getTokenContract().caller.balanceOf(sender.getAddress())
        if (sender.getDepositAmount() == (sender_balance_before - sender_balance_after)):
            sender.getERC20EscrowContract().functions.confirmDeposit().transact()
            print("Confirmed deposit of expected amount.")
        print('Deposit hash: ' + Web3.toHex(tx_hash_deposit))
        print('Sender balance after: ' + str(ABC.getTokenContract().caller.balanceOf(sender.getAddress())))

        web3.eth.defaultAccount = oldActiveAccount
        printNewLine()

    def withdrawERC20InEscrow(self, receiver, sender):
        printNewLine()
        if receiver.expectedCurrency == "ETH":
            print('Aborting ERC20 fund withdrawal.')
            return False
        
        oldActiveAccount = web3.eth.defaultAccount
        web3.eth.defaultAccount = web3.eth.accounts[receiver.getGanacheIndex()]

        print('Withdrawing ERC20 tokens in Escrow...')
        print('Receiver is ' + receiver.getAddress())
        print('Receiver balance before: ' + str(ABC.getTokenContract().caller.balanceOf(receiver.getAddress())))
        receiver_balance_before = ABC.getTokenContract().caller.balanceOf(receiver.getAddress())
        # Receiver gets puzzle key from the sender through another means in this implementation
        tx_hash_retrieval = sender.getERC20EscrowContract().functions.withdraw(receiver.getAddress(), sender.getPuzzleKey()).transact()
        tx_deposit_receipt = web3.eth.waitForTransactionReceipt(tx_hash_retrieval)
        receiver_balance_after = ABC.getTokenContract().caller.balanceOf(receiver.getAddress())
        if ((receiver.getExpectedAmount()*(1+receiver.getTolerance()/100)) > (receiver_balance_after - receiver_balance_before)) and ((receiver.getExpectedAmount()*(1-receiver.getTolerance()/100)) < (receiver_balance_after - receiver_balance_before)):
            print('Received expected amount.')
        print('Retrieval hash: ' + Web3.toHex(tx_hash_retrieval))
        print('Receivers balance after: ' + str(ABC.getTokenContract().caller.balanceOf(receiver.getAddress())))

        web3.eth.defaultAccount = oldActiveAccount
        printNewLine()

    def lockETHInEscrow(self, sender, kyberEscrow = None):
        printNewLine()
        if not sender.depositCurrency == "ETH":
            print('Aborting ETH fund deposit.')
            return False

        oldActiveAccount = web3.eth.defaultAccount
        web3.eth.defaultAccount = web3.eth.accounts[sender.getGanacheIndex()]

        sender_balance_before = web3.eth.getBalance(sender.getAddress())
        depositAddress = kyberEscrow.getETHEscrowContractAddress() if kyberEscrow is not None else sender.getETHEscrowContractAddress()

        print('Locking ETH in Escrow...')
        print('Sender is ' + sender.getAddress())
        print('Sender balance before: ' + str(web3.eth.getBalance(sender.getAddress())))

        txn = {
            'nonce': web3.eth.getTransactionCount(sender.getAddress()),
            'from': sender.getAddress(),
            'to': depositAddress,
            'value': web3.toWei(sender.getDepositAmount(), 'ether'),
            'gas': 2000000,
            'gasPrice': 20000000000
        }

        signed_txn = web3.eth.account.signTransaction(txn, sender.getPrivateKey())
        tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

        sender_balance_after = web3.eth.getBalance(sender.getAddress())
        sender.getETHEscrowContract().functions.confirmDeposit().transact()
        
        print('Retrieval hash: ' + web3.toHex(tx_hash))
        print('Sender balance after: ' + str(web3.eth.getBalance(sender.getAddress())))

        web3.eth.defaultAccount = oldActiveAccount
        printNewLine()

    def withdrawETHInEscrow(self, receiver, sender):
        printNewLine()
        if not receiver.expectedCurrency == "ETH":
            print('Aborting ETH fund withdrawal.')
            return False
        
        oldActiveAccount = web3.eth.defaultAccount
        web3.eth.defaultAccount = web3.eth.accounts[receiver.getGanacheIndex()]
        
        print('Withdrawing ETH in Escrow...')
        print('Receiver is ' + receiver.getAddress())
        print('Receiver balance before: ' + str(web3.eth.getBalance(receiver.getAddress())))
        receiver_balance_before = web3.eth.getBalance(receiver.getAddress())
        # Receiver gets puzzle key from the sender through another means in this implementation
        tx_hash_retrieval = sender.getETHEscrowContract().functions.withdraw(receiver.getAddress(), sender.getPuzzleKey()).transact()
        tx_deposit_receipt = web3.eth.waitForTransactionReceipt(tx_hash_retrieval)
        receiver_balance_after = web3.eth.getBalance(receiver.getAddress())
        if ((receiver.getExpectedAmount()*(1+receiver.getTolerance()/100)) > (receiver_balance_after - receiver_balance_before)) and ((receiver.getExpectedAmount()*(1-receiver.getTolerance()/100)) < (receiver_balance_after - receiver_balance_before)):
            print('Received expected amount.')
        print('Retrieval hash: ' + Web3.toHex(tx_hash_retrieval))
        print('Receivers balance after: ' + str(web3.eth.getBalance(receiver.getAddress())))

        web3.eth.defaultAccount = oldActiveAccount
        printNewLine()

def arwenTradeERCtoETH(sender, receiver):
    printNewLine()
    print('\nSender ERC balance before trade: ' + str(ABC.getTokenContract().caller.balanceOf(sender.getAddress())))
    print('Sender ETH balance before trade: ' + str(web3.eth.getBalance(sender.getAddress())))
    print('Reciever ERC balance before trade: ' + str(ABC.getTokenContract().caller.balanceOf(receiver.getAddress())))
    print('Reciever ETH balance before trade: ' + str(web3.eth.getBalance(receiver.getAddress())))
    tradeInstance = ArwenAtomicSwap(sender, receiver)
    tradeInstance.lockERC20InEscrow(sender)
    tradeInstance.lockETHInEscrow(receiver)
    # This is where Alice and Bob ensure each other's escrows are correct and share private key
    tradeInstance.withdrawERC20InEscrow(receiver, sender)
    tradeInstance.withdrawETHInEscrow(sender, receiver)
    print('Sender ERC balance after trade: ' + str(ABC.getTokenContract().caller.balanceOf(sender.getAddress())))
    print('Sender ETH balance after trade: ' + str(web3.eth.getBalance(sender.getAddress())))
    print('Reciever ERC balance after trade: ' + str(ABC.getTokenContract().caller.balanceOf(receiver.getAddress())))
    print('Reciever ETH balance after trade: ' + str(web3.eth.getBalance(receiver.getAddress())) + '\n')
    printNewLine()
    
def arwenTradeETHtoERC(sender, receiver):
    printNewLine()
    print('\nSender ERC balance before trade: ' + str(ABC.getTokenContract().caller.balanceOf(sender.getAddress())))
    print('Sender ETH balance before trade: ' + str(web3.eth.getBalance(sender.getAddress())))
    print('Reciever ERC balance before trade: ' + str(ABC.getTokenContract().caller.balanceOf(receiver.getAddress())))
    print('Reciever ETH balance before trade: ' + str(web3.eth.getBalance(receiver.getAddress())))
    tradeInstance = ArwenAtomicSwap(sender, receiver)
    tradeInstance.lockETHInEscrow(sender)
    tradeInstance.lockERC20InEscrow(receiver)
    # This is where Alice and Bob ensure each other's escrows are correct and share private key
    tradeInstance.withdrawERC20InEscrow(sender, receiver)
    tradeInstance.withdrawETHInEscrow(receiver, sender)
    print('Sender ERC balance after trade: ' + str(ABC.getTokenContract().caller.balanceOf(sender.getAddress())))
    print('Sender ETH balance after trade: ' + str(web3.eth.getBalance(sender.getAddress())))
    print('Reciever ERC balance after trade: ' + str(ABC.getTokenContract().caller.balanceOf(receiver.getAddress())))
    print('Reciever ETH balance after trade: ' + str(web3.eth.getBalance(receiver.getAddress())) + '\n')
    printNewLine()
    
def printNewLine():
    print('\n')

abc_contract_address = Web3.toChecksumAddress('0xad1603bb7bfa29baaae4b7f12a9d6fac6f075d77')
abc_contract = web3.eth.contract(address=abc_contract_address, abi=abc_abi, bytecode=abc_bytecode)

aliceERC20EscrowContractAddress = Web3.toChecksumAddress('0x5f9fa61667411b24cb1ea6cf566217570698bda6')
aliceERC20EscrowContractABI = json.loads('[ { "constant": false, "inputs": [], "name": "confirmDeposit", "outputs": [ { "name": "", "type": "bool" } ], "payable": true, "stateMutability": "payable", "type": "function" }, { "constant": false, "inputs": [], "name": "refund", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "_newTimeLimit", "type": "uint256" } ], "name": "setLargerTimeLimit", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "_to", "type": "address" }, { "name": "_key", "type": "string" } ], "name": "withdraw", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "name": "_seller", "type": "address" }, { "name": "_timeLimit", "type": "uint256" } ], "payable": false, "stateMutability": "nonpayable", "type": "constructor" }, { "constant": true, "inputs": [], "name": "currentState", "outputs": [ { "name": "", "type": "uint8" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "puzzle", "outputs": [ { "name": "", "type": "bytes32" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "seller", "outputs": [ { "name": "", "type": "address" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "timeLimit", "outputs": [ { "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "tokenAddress", "outputs": [ { "name": "", "type": "address" } ], "payable": false, "stateMutability": "view", "type": "function" } ]')
aliceERC20EscrowContract = web3.eth.contract(address=aliceERC20EscrowContractAddress, abi=aliceERC20EscrowContractABI)

aliceETHEscrowContractAddress = Web3.toChecksumAddress('0xefb697d4fe023adcef218893d28339d432337263')
aliceETHEscrowContractABI = json.loads('[ { "constant": false, "inputs": [], "name": "confirmDeposit", "outputs": [ { "name": "", "type": "bool" } ], "payable": true, "stateMutability": "payable", "type": "function" }, { "constant": false, "inputs": [], "name": "refund", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "_newTimeLimit", "type": "uint256" } ], "name": "setLargerTimeLimit", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "_to", "type": "address" }, { "name": "_key", "type": "string" } ], "name": "withdraw", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "name": "_seller", "type": "address" }, { "name": "_timeLimit", "type": "uint256" } ], "payable": false, "stateMutability": "nonpayable", "type": "constructor" }, { "constant": true, "inputs": [], "name": "currentState", "outputs": [ { "name": "", "type": "uint8" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "puzzle", "outputs": [ { "name": "", "type": "bytes32" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "seller", "outputs": [ { "name": "", "type": "address" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "timeLimit", "outputs": [ { "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "tokenAddress", "outputs": [ { "name": "", "type": "address" } ], "payable": false, "stateMutability": "view", "type": "function" } ]')
aliceETHEscrowContract = web3.eth.contract(address=aliceETHEscrowContractAddress, abi=aliceETHEscrowContractABI)

alice = User('0x73661E5b5481b1F9A19F34a330c9D77D1Fc215C1', '85d8c6d8fc255c36f8c2d7e1f5e441c9792d0ecd19e8369f25a9ee6f2dd3e105' ,'bippityBoppityGiveMeTheZoppity', 0, 'ABC', 'ETH', aliceERC20EscrowContractAddress, aliceERC20EscrowContractABI, aliceETHEscrowContractAddress, aliceETHEscrowContractABI, 10, 1, 5, 0.1, 10)


bobERC20EscrowContractAddress = Web3.toChecksumAddress('0x5706ca7e59b5fe2175f28326dc293cb1a316d17b')
bobERC20EscrowContractABI = json.loads('[ { "constant": false, "inputs": [], "name": "confirmDeposit", "outputs": [ { "name": "", "type": "bool" } ], "payable": true, "stateMutability": "payable", "type": "function" }, { "constant": false, "inputs": [], "name": "refund", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "_newTimeLimit", "type": "uint256" } ], "name": "setLargerTimeLimit", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "_to", "type": "address" }, { "name": "_key", "type": "string" } ], "name": "withdraw", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "name": "_seller", "type": "address" }, { "name": "_timeLimit", "type": "uint256" } ], "payable": false, "stateMutability": "nonpayable", "type": "constructor" }, { "constant": true, "inputs": [], "name": "currentState", "outputs": [ { "name": "", "type": "uint8" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "puzzle", "outputs": [ { "name": "", "type": "bytes32" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "seller", "outputs": [ { "name": "", "type": "address" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "timeLimit", "outputs": [ { "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "tokenAddress", "outputs": [ { "name": "", "type": "address" } ], "payable": false, "stateMutability": "view", "type": "function" } ]')
bobERC20EscrowContract = web3.eth.contract(address=bobERC20EscrowContractAddress, abi=bobERC20EscrowContractABI)

bobETHEscrowContractAddress = Web3.toChecksumAddress('0x6cfc17a5eab39b9e3388c2ee446f6ca6f838c0d3')
bobETHEscrowContractABI = json.loads('[ { "constant": true, "inputs": [], "name": "seller", "outputs": [ { "name": "", "type": "address" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "currentState", "outputs": [ { "name": "", "type": "uint8" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "name": "_newTimeLimit", "type": "uint256" } ], "name": "setLargerTimeLimit", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [], "name": "confirmDeposit", "outputs": [ { "name": "", "type": "bool" } ], "payable": true, "stateMutability": "payable", "type": "function" }, { "constant": true, "inputs": [], "name": "puzzle", "outputs": [ { "name": "", "type": "bytes32" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [], "name": "refund", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "_to", "type": "address" }, { "name": "_key", "type": "string" } ], "name": "withdraw", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "tokenAddress", "outputs": [ { "name": "", "type": "address" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "timeLimit", "outputs": [ { "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "inputs": [ { "name": "_tokenAdd", "type": "address" }, { "name": "_seller", "type": "address" }, { "name": "_timeLimit", "type": "uint256" } ], "payable": false, "stateMutability": "nonpayable", "type": "constructor" } ]')
bobETHEscrowContract = web3.eth.contract(address=bobETHEscrowContractAddress, abi=bobETHEscrowContractABI)

bob = User('0x377a6b4Dfbf6215Ff3B4Ef67872445af478483cd', 'a5bccad901b56fe5ecfce860b6f5be8662434e1827a251ac96615802e0e1f05b' ,'itIsAndyAndTheTuna', 1, 'ETH', 'ABC', bobERC20EscrowContractAddress, bobERC20EscrowContractABI, bobETHEscrowContractAddress, bobETHEscrowContractABI, 1, 10, 5, 0.1, 10)


kyberERC20EscrowContractAddress = Web3.toChecksumAddress('0xdc4b81ac627501acdf41af4c0df5e49c1cf101b7')
kyberERC20EscrowContractABI = json.loads('[ { "constant": false, "inputs": [], "name": "confirmDeposit", "outputs": [ { "name": "", "type": "bool" } ], "payable": true, "stateMutability": "payable", "type": "function" }, { "constant": false, "inputs": [], "name": "refund", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "_newTimeLimit", "type": "uint256" } ], "name": "setLargerTimeLimit", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "_to", "type": "address" }, { "name": "_key", "type": "string" } ], "name": "withdraw", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "name": "_seller", "type": "address" }, { "name": "_timeLimit", "type": "uint256" } ], "payable": false, "stateMutability": "nonpayable", "type": "constructor" }, { "constant": true, "inputs": [], "name": "currentState", "outputs": [ { "name": "", "type": "uint8" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "puzzle", "outputs": [ { "name": "", "type": "bytes32" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "seller", "outputs": [ { "name": "", "type": "address" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "timeLimit", "outputs": [ { "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "tokenAddress", "outputs": [ { "name": "", "type": "address" } ], "payable": false, "stateMutability": "view", "type": "function" } ]')
kyberERC20EscrowContract = web3.eth.contract(address=kyberERC20EscrowContractAddress, abi=kyberERC20EscrowContractABI)

kyberETHEscrowContractAddress = Web3.toChecksumAddress('0xa52e18d39c6dbbd9eb25041ef0d7fc7185f0a28c')
kyberETHEscrowContractABI = json.loads('[ { "constant": true, "inputs": [], "name": "seller", "outputs": [ { "name": "", "type": "address" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "currentState", "outputs": [ { "name": "", "type": "uint8" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "name": "_newTimeLimit", "type": "uint256" } ], "name": "setLargerTimeLimit", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [], "name": "confirmDeposit", "outputs": [ { "name": "", "type": "bool" } ], "payable": true, "stateMutability": "payable", "type": "function" }, { "constant": true, "inputs": [], "name": "puzzle", "outputs": [ { "name": "", "type": "bytes32" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [], "name": "refund", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "_to", "type": "address" }, { "name": "_key", "type": "string" } ], "name": "withdraw", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "tokenAddress", "outputs": [ { "name": "", "type": "address" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "timeLimit", "outputs": [ { "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "inputs": [ { "name": "_tokenAdd", "type": "address" }, { "name": "_seller", "type": "address" }, { "name": "_timeLimit", "type": "uint256" } ], "payable": false, "stateMutability": "nonpayable", "type": "constructor" } ]')
kyberETHEscrowContract = web3.eth.contract(address=kyberETHEscrowContractAddress, abi=kyberETHEscrowContractABI)

kyberERC = User('0x621f7c11030872f6F056B6FA5e854c34f56f0f0f', '48eafe71025a7cefae7257c995cf3826c58d226beb0fc44f1ca97bd8b65acacc' ,'beetsBearsBattlestarGalactica', 2, 'ABC', 'ETH', kyberERC20EscrowContractAddress, kyberERC20EscrowContractABI, kyberETHEscrowContractAddress, kyberETHEscrowContractABI, 10, 1, 5, 0.1, 10)

kyberETH = User('0x621f7c11030872f6F056B6FA5e854c34f56f0f0f', '48eafe71025a7cefae7257c995cf3826c58d226beb0fc44f1ca97bd8b65acacc' ,'beetsBearsBattlestarGalactica', 2, 'ETH', 'ABC', kyberERC20EscrowContractAddress, kyberERC20EscrowContractABI, kyberETHEscrowContractAddress, kyberETHEscrowContractABI, 1, 10, 5, 0.1, 10)


reserve1ERC20EscrowContractAddress = Web3.toChecksumAddress('0x0786c0e2ff28b8c9175af6ff99415c42ddea6bad')
reserve1ERC20EscrowContractABI = json.loads('[ { "constant": false, "inputs": [], "name": "confirmDeposit", "outputs": [ { "name": "", "type": "bool" } ], "payable": true, "stateMutability": "payable", "type": "function" }, { "constant": false, "inputs": [], "name": "refund", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "_newTimeLimit", "type": "uint256" } ], "name": "setLargerTimeLimit", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "_to", "type": "address" }, { "name": "_key", "type": "string" } ], "name": "withdraw", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "name": "_seller", "type": "address" }, { "name": "_timeLimit", "type": "uint256" } ], "payable": false, "stateMutability": "nonpayable", "type": "constructor" }, { "constant": true, "inputs": [], "name": "currentState", "outputs": [ { "name": "", "type": "uint8" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "puzzle", "outputs": [ { "name": "", "type": "bytes32" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "seller", "outputs": [ { "name": "", "type": "address" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "timeLimit", "outputs": [ { "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "tokenAddress", "outputs": [ { "name": "", "type": "address" } ], "payable": false, "stateMutability": "view", "type": "function" } ]')
reserve1ERC20EscrowContract = web3.eth.contract(address=reserve1ERC20EscrowContractAddress, abi=reserve1ERC20EscrowContractABI)

reserve1ETHEscrowContractAddress = Web3.toChecksumAddress('0xc27ba61f87b8210327e92298cabf13af1f4ec963')
reserve1ETHEscrowContractABI = json.loads('[ { "constant": true, "inputs": [], "name": "seller", "outputs": [ { "name": "", "type": "address" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "currentState", "outputs": [ { "name": "", "type": "uint8" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "name": "_newTimeLimit", "type": "uint256" } ], "name": "setLargerTimeLimit", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [], "name": "confirmDeposit", "outputs": [ { "name": "", "type": "bool" } ], "payable": true, "stateMutability": "payable", "type": "function" }, { "constant": true, "inputs": [], "name": "puzzle", "outputs": [ { "name": "", "type": "bytes32" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [], "name": "refund", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "_to", "type": "address" }, { "name": "_key", "type": "string" } ], "name": "withdraw", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "tokenAddress", "outputs": [ { "name": "", "type": "address" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "timeLimit", "outputs": [ { "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "inputs": [ { "name": "_tokenAdd", "type": "address" }, { "name": "_seller", "type": "address" }, { "name": "_timeLimit", "type": "uint256" } ], "payable": false, "stateMutability": "nonpayable", "type": "constructor" } ]')
reserve1ETHEscrowContract = web3.eth.contract(address=reserve1ETHEscrowContractAddress, abi=reserve1ETHEscrowContractABI)

reserve1ERC = User('0xFd581A7Db1856E9131FADCdd8fd932C9312d8c5d', '2a98cf8927dcd698a7b82f6caeaa5ba4be7a9fe1cf47cf3a1544d40a98aa0076' ,'iFeelGodInThisChilisTonight', 3, 'ABC', 'ETH', reserve1ERC20EscrowContractAddress, reserve1ERC20EscrowContractABI, reserve1ETHEscrowContractAddress, reserve1ETHEscrowContractABI, 10, 1, 5, 0.1, 10)
reserve1ETH = User('0xFd581A7Db1856E9131FADCdd8fd932C9312d8c5d', '2a98cf8927dcd698a7b82f6caeaa5ba4be7a9fe1cf47cf3a1544d40a98aa0076' ,'iFeelGodInThisChilisTonight', 3, 'ETH', 'ABC', reserve1ERC20EscrowContractAddress, reserve1ERC20EscrowContractABI, reserve1ETHEscrowContractAddress, reserve1ETHEscrowContractABI, 1, 9, 5, 0.1, 10)


reserve2ERC20EscrowContractAddress = Web3.toChecksumAddress('0x0e23f58abff4beea3b8981593cf6114d47134470')
reserve2ERC20EscrowContractABI = json.loads('[ { "constant": false, "inputs": [], "name": "confirmDeposit", "outputs": [ { "name": "", "type": "bool" } ], "payable": true, "stateMutability": "payable", "type": "function" }, { "constant": false, "inputs": [], "name": "refund", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "_newTimeLimit", "type": "uint256" } ], "name": "setLargerTimeLimit", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "_to", "type": "address" }, { "name": "_key", "type": "string" } ], "name": "withdraw", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "name": "_seller", "type": "address" }, { "name": "_timeLimit", "type": "uint256" } ], "payable": false, "stateMutability": "nonpayable", "type": "constructor" }, { "constant": true, "inputs": [], "name": "currentState", "outputs": [ { "name": "", "type": "uint8" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "puzzle", "outputs": [ { "name": "", "type": "bytes32" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "seller", "outputs": [ { "name": "", "type": "address" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "timeLimit", "outputs": [ { "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "tokenAddress", "outputs": [ { "name": "", "type": "address" } ], "payable": false, "stateMutability": "view", "type": "function" } ]')
reserve2ERC20EscrowContract = web3.eth.contract(address=reserve2ERC20EscrowContractAddress, abi=reserve2ERC20EscrowContractABI)

reserve2ETHEscrowContractAddress = Web3.toChecksumAddress('0x87ae5c1467c1250ba24bf8563fec2b1448802340')
reserve2ETHEscrowContractABI = json.loads('[ { "constant": true, "inputs": [], "name": "seller", "outputs": [ { "name": "", "type": "address" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "currentState", "outputs": [ { "name": "", "type": "uint8" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "name": "_newTimeLimit", "type": "uint256" } ], "name": "setLargerTimeLimit", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [], "name": "confirmDeposit", "outputs": [ { "name": "", "type": "bool" } ], "payable": true, "stateMutability": "payable", "type": "function" }, { "constant": true, "inputs": [], "name": "puzzle", "outputs": [ { "name": "", "type": "bytes32" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [], "name": "refund", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "_to", "type": "address" }, { "name": "_key", "type": "string" } ], "name": "withdraw", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [], "name": "tokenAddress", "outputs": [ { "name": "", "type": "address" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "timeLimit", "outputs": [ { "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "inputs": [ { "name": "_tokenAdd", "type": "address" }, { "name": "_seller", "type": "address" }, { "name": "_timeLimit", "type": "uint256" } ], "payable": false, "stateMutability": "nonpayable", "type": "constructor" } ]')
reserve2ETHEscrowContract = web3.eth.contract(address=reserve2ETHEscrowContractAddress, abi=reserve2ETHEscrowContractABI)

reserve2ERC = User('0x9F9b5658b543DCeD9f5a3eAeDd54C0BC4C2F6E17', '0f4ac34a437fd73c89e324c87bd5a447beea4378afbf50624e1a3cfbeec528ad' ,'iDeclareBankruptcy', 4, 'ABC', 'ETH', reserve2ERC20EscrowContractAddress, reserve2ERC20EscrowContractABI, reserve2ETHEscrowContractAddress, reserve2ETHEscrowContractABI, 10, 1, 5, 0.1, 10)
reserve2ETH = User('0x9F9b5658b543DCeD9f5a3eAeDd54C0BC4C2F6E17', '0f4ac34a437fd73c89e324c87bd5a447beea4378afbf50624e1a3cfbeec528ad' ,'iDeclareBankruptcy', 4, 'ETH', 'ABC', reserve2ERC20EscrowContractAddress, reserve2ERC20EscrowContractABI, reserve2ETHEscrowContractAddress, reserve2ETHEscrowContractABI, 1, 11, 5, 0.1, 10)

sender_address = '0x73661E5b5481b1F9A19F34a330c9D77D1Fc215C1'
destination_address = '0x377a6b4Dfbf6215Ff3B4Ef67872445af478483cd'

web3.eth.defaultAccount = web3.eth.accounts[0]

ABC = ERC20Token(abc_contract_address, abc_abi, abc_bytecode)

ERCReserves = [reserve1ERC, reserve2ERC]
ETHReserves = [reserve1ETH, reserve2ETH]

## Put your function calls here
# arwenTradeERCtoETH(alice, bob)
# kyberTradeInstance = KyberExchange(ERCReserves, ETHReserves)
# kyberTradeInstance.executeFullKyberTrade(alice, 'ABC', 10)