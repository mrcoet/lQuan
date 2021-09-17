import string


def okay_name_emoji(name: str):
    OKAYLIST = [num_ for num_ in range(65, 91)] + [num_ for num_ in range(97, 123)] + [32]
    name_list = [ord(char_) for char_ in name]
    if set(name_list).difference(OKAYLIST):
        return False
    return True


def okay_name_word(name: str):
    alphabet_string = string.ascii_lowercase
    bad_words = [char_ * 3 for char_ in alphabet_string] + ["test", "fuck", "contract"]
    for bad_word in bad_words:
        if bad_word.lower() in name.lower():
            return False
    return True


def okay_name(name: str):
    okay_name_emoji_ = okay_name_emoji(name)
    if not okay_name_emoji_:
        return False
    okay_name_word_ = okay_name_word(name)
    if not okay_name_word_:
        return False
    return True


if __name__ == "__main__":
    from web3 import Web3
    import json

    bscNode = "wss://bsc-ws-node.nariox.org:443"
    w3 = Web3(Web3.WebsocketProvider(bscNode))

    if w3.isConnected():
        print("[INFO] Web3 Seccessfuly connected")

    tokenABI = json.loads(
        '[ { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "owner", "type": "address" }, { "indexed": true, "internalType": "address", "name": "spender", "type": "address" }, { "indexed": false, "internalType": "uint256", "name": "value", "type": "uint256" } ], "name": "Approval", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "from", "type": "address" }, { "indexed": true, "internalType": "address", "name": "to", "type": "address" }, { "indexed": false, "internalType": "uint256", "name": "value", "type": "uint256" } ], "name": "Transfer", "type": "event" }, { "constant": true, "inputs": [ { "internalType": "address", "name": "_owner", "type": "address" }, { "internalType": "address", "name": "spender", "type": "address" } ], "name": "allowance", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "internalType": "address", "name": "spender", "type": "address" }, { "internalType": "uint256", "name": "amount", "type": "uint256" } ], "name": "approve", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [ { "internalType": "address", "name": "account", "type": "address" } ], "name": "balanceOf", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "decimals", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "getOwner", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "name", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "symbol", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "totalSupply", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "internalType": "address", "name": "recipient", "type": "address" }, { "internalType": "uint256", "name": "amount", "type": "uint256" } ], "name": "transfer", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "internalType": "address", "name": "sender", "type": "address" }, { "internalType": "address", "name": "recipient", "type": "address" }, { "internalType": "uint256", "name": "amount", "type": "uint256" } ], "name": "transferFrom", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" } ]'
    )
    tokenAddress = w3.toChecksumAddress("0x933d3caca4031cf9268e6bd550ea8628c28c10bc")
    tokenContract = w3.eth.contract(address=tokenAddress, abi=tokenABI)
    tokenName = tokenContract.functions.name().call()
    tokensymbol = tokenContract.functions.symbol().call()

    if okay_name(tokenName):
        print(f"TokenName: {tokenName} : is Okay.")
    if okay_name(tokensymbol):
        print(f"TokenSymbol: {tokensymbol}: is Okay.")
    else:
        print(f"TokenSymbol: {tokensymbol}: is **NOT** Okay.")
