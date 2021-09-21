let web3 = null;
let tokenName = "";
let tokenSymbol = "";
let tokenDecimals = 0;
let maxSell = 0;
let maxTXAmount = 0;
let bnbIN = 1000000000000000000;
let maxTxBNB = null;

const urlParams = new URLSearchParams(window.location.search);
let address = urlParams.get("address");
if (address.length < 1) {
  pathname = window.location.pathname;
  if (pathname.startsWith("/token/")) {
    let tokenAddress = pathname.split("/")[pathname.length - 1];
    address = tokenAddress;
  }
}
const screenWidth = screen.width;
let addressToOutput = address;

if (screenWidth < 768) {
  addressToOutput = address.substring(0, 6) + "..." + address.substring(address.length - 4);
}

web3 = new Web3("https://bsc-dataseed.binance.org/");
run(address);

function encodeBasicFunction(web3, funcName) {
  return web3.eth.abi.encodeFunctionCall(
    {
      name: funcName,
      type: "function",
      inputs: [],
    },
    []
  );
}

async function updateTokenInformation(web3, tokenAddress) {
  web3.eth
    .call({
      to: tokenAddress,
      value: 0,
      gas: 150000,
      data: encodeBasicFunction(web3, "name"),
    })
    .then((value) => {
      tokenName = web3.eth.abi.decodeParameter("string", value);
      let x = document.getElementById("token-info");
      if (x != null) {
        x.innerText = tokenName + " (" + tokenSymbol + ")";
      }
    });

  web3.eth
    .call({
      to: tokenAddress,
      value: 0,
      gas: 150000,
      data: encodeBasicFunction(web3, "symbol"),
    })
    .then((value) => {
      tokenSymbol = web3.eth.abi.decodeParameter("string", value);
      let x = document.getElementById("token-info");
      if (x != null) {
        x.innerText = tokenName + " (" + tokenSymbol + ")";
      }
    });
}

async function run(address) {
  x = updateTokenInformation(web3, address);
  await getMaxes();
  if (maxTXAmount != 0 || maxSell != 0) {
    await getDecimals(address);
    await getBNBIn(address);
  }
  await honeypotIs(address);
  await x;
}

async function getDecimals(address) {
  let sig = encodeBasicFunction(web3, "decimals");
  d = {
    to: address,
    from: "0x8894e0a0c962cb723c1976a4421c95949be2d4e3",
    value: 0,
    gas: 15000000,
    data: sig,
  };
  try {
    let val = await web3.eth.call(d);
    tokenDecimals = web3.utils.hexToNumber(val);
  } catch (e) {
    console.log("decimals", e);
  }
}

async function getBNBIn(address) {
  let amountIn = maxTXAmount;
  if (maxSell != 0) {
    amountIn = maxSell;
  }
  let WETH = "0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c";
  let path = [address, WETH];
  let sig = web3.eth.abi.encodeFunctionCall(
    {
      name: "getAmountsOut",
      type: "function",
      inputs: [
        { type: "uint256", name: "amountIn" },
        { type: "address[]", name: "path" },
      ],
      outputs: [{ type: "uint256[]", name: "amounts" }],
    },
    [amountIn, path]
  );

  d = {
    to: "0x10ED43C718714eb63d5aA57B78B54704E256024E",
    from: "0x8894e0a0c962cb723c1976a4421c95949be2d4e3",
    value: 0,
    gas: 15000000,
    data: sig,
  };
  try {
    let val = await web3.eth.call(d);
    let decoded = web3.eth.abi.decodeParameter("uint256[]", val);
    bnbIN = web3.utils.toBN(decoded[1]);
    maxTxBNB = bnbIN;
  } catch (e) {
    console.log(e);
  }
  console.log(bnbIN, amountIn);
}

async function getMaxes() {
  let sig = web3.eth.abi.encodeFunctionSignature({ name: "_maxTxAmount", type: "function", inputs: [] });
  d = {
    to: address,
    from: "0x8894e0a0c962cb723c1976a4421c95949be2d4e3",
    value: 0,
    gas: 15000000,
    data: sig,
  };
  try {
    let val = await web3.eth.call(d);
    maxTXAmount = web3.utils.toBN(val);
    console.log(val, maxTXAmount);
  } catch (e) {
    console.log("_maxTxAmount: ", e);
    // I will nest as much as I want. screw javascript.
    sig = web3.eth.abi.encodeFunctionSignature({ name: "maxSellTransactionAmount", type: "function", inputs: [] });
    d = {
      to: address,
      from: "0x8894e0a0c962cb723c1976a4421c95949be2d4e3",
      value: 0,
      gas: 15000000,
      data: sig,
    };
    try {
      let val2 = await web3.eth.call(d);
      maxSell = web3.utils.toBN(val2);
      console.log(val2, maxSell);
    } catch (e) {}
  }
}

function numberWithCommas(x) {
  return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

async function honeypotIs(address) {
  let encodedAddress = web3.eth.abi.encodeParameter("address", address);
  let contractFuncData = "0xd66383cb";
  let callData = contractFuncData + encodedAddress.substring(2);

  let val = 100000000000000000;
  if (bnbIN < val) {
    val = bnbIN - 1000;
  }
  web3.eth
    .call({
      to: "0x5bf62ec82af715ca7aa365634fab0e8fd7bf92c7",
      from: "0x8894e0a0c962cb723c1976a4421c95949be2d4e3",
      value: val,
      gas: 45000000,
      data: callData,
    })
    .then((val) => {
      let decoded = web3.eth.abi.decodeParameters(["uint256", "uint256", "uint256", "uint256", "uint256", "uint256"], val);
      let buyExpectedOut = web3.utils.toBN(decoded[0]);
      let buyActualOut = web3.utils.toBN(decoded[1]);
      let sellExpectedOut = web3.utils.toBN(decoded[2]);
      let sellActualOut = web3.utils.toBN(decoded[3]);
      let buyGasUsed = web3.utils.toBN(decoded[4]);
      let sellGasUsed = web3.utils.toBN(decoded[5]);
      buy_tax = Math.round(((buyExpectedOut - buyActualOut) / buyExpectedOut) * 100 * 10) / 10;
      sell_tax = Math.round(((sellExpectedOut - sellActualOut) / sellExpectedOut) * 100 * 10) / 10;
      console.log(buy_tax, sell_tax);
      let maxdiv = "";
      if (maxTXAmount != 0 || maxSell != 0) {
        let n = "Max TX";
        let x = maxTXAmount;
        if (maxSell != 0) {
          n = "Max Sell";
          x = maxSell;
        }
        let bnbWorth = "?";
        if (maxTxBNB != null) {
          bnbWorth = Math.round(maxTxBNB / 10 ** 15) / 10 ** 3;
        }
        let tokens = Math.round(x / 10 ** tokenDecimals);
        maxdiv = "<p>" + n + ": " + tokens + " " + tokenSymbol + " (~" + bnbWorth + " BNB)</p>";
      }
      let gasdiv = "<p>Gas used for Buying: " + numberWithCommas(buyGasUsed) + "<br>Gas used for Selling: " + numberWithCommas(sellGasUsed) + "</p>";
      document.getElementById("shitcoin").innerHTML = '<div style="max-width: 100%;" class="ui compact success message"><div class="header">Does not seem like a honeypot.</div><p>This can always change! Do your own due diligence.</p><p>Address: ' + addressToOutput + '</p><p id="token-info">' + tokenName + " (" + tokenSymbol + ")" + "</p>" + maxdiv + gasdiv + "<p>Buy Tax: " + buy_tax + "%<br>Sell Tax: " + sell_tax + "%</p></div>";
    })
    .catch((err) => {
      document.getElementById("shitcoin").innerHTML = '<div style="max-width: 100%;" class="ui compact error message"><div class="header">Yup, honeypot. Run the fuck away.</div><p>Address: ' + addressToOutput + '</p><p id="token-info">' + tokenName + " (" + tokenSymbol + ")" + "</p><br>" + err + "</div>";
    });
  updateTokenInformation(web3, address);
}
