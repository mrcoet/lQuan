from web3 import Web3
import requests
import json


bscNode = "wss://bsc-ws-node.nariox.org:443"
w3 = Web3(Web3.WebsocketProvider(bscNode))
if w3.isConnected():
    print("[Info] Web3 successfully connected")


tokenAddress = w3.toChecksumAddress("0xe56842Ed550Ff2794F010738554db45E60730371")
pancakeSwapRouterAddress = w3.toChecksumAddress("0x10ED43C718714eb63d5aA57B78B54704E256024E")


contractCodeGetRequestURL = "https://api.bscscan.com/api?module=contract&action=getsourcecode&address=" + tokenAddress
contractCodeRequest = requests.get(contractCodeGetRequestURL)
tokenContractCode = contractCodeRequest.json()

source_code = tokenContractCode["result"][0]["SourceCode"]


if str(tokenContractCode["result"][0]["ABI"]) == "Contract source code not verified":  # ---> Contract Verified
    print("[FAIL] contract source code isn't verified.")

if str(pancakeSwapRouterAddress) not in str(source_code):  # ----> Don't use Router V2
    print("[FAIL] Contract doesn't use valid PancakeSwap v2 router.")


if "telegram" in str(source_code).lower():  # ---> has Telegram
    print("has telegram")

if "website" in str(source_code).lower():  # ---> Has websit
    print("has website")

if "twitter" in str(source_code).lower():  # ---> has twitter
    print("has twitter")


def check_telegram(source_code: str):  # get telegram link
    def many_or_one_sourcecode(source_code: str):
        try:
            source_code_dict = json.loads(source_code)
            source_code_keys = list(source_code_dict.keys())
            source_code_final = str(source_code_dict[source_code_keys[0]]["content"])
            return source_code_final
        except:
            return str(source_code)

    if "t.me" in str(source_code):
        source_code = many_or_one_sourcecode(source_code)
        for line_ in source_code.splitlines():
            if "t.me" in line_:
                line = line_.strip()
                tele_index = line.index("t.me")
                out_ = "https://" + line[tele_index:]
                return out_
    else:
        return False


def bad_in_code(path: str, source_code: str):  # check bad functions and words
    codeExceptionFile = open(path)
    lines = codeExceptionFile.readlines()
    for codeException in lines:
        if codeException.strip().lower() in source_code.lower():
            print("bad: ", codeException)
            return True
    return False


print(bad_in_code("./contract/badInCode.txt", source_code))
