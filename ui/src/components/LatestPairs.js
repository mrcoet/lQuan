import { useState, useEffect, useCallback } from "react";
import { LatestPair } from "./LatestPair";
import { LatestPairModal } from "./LatestPairModal";

export const LatestPairs = () => {
    const [pairs, setPairs] = useState([]);

    const [page, setPage] = useState(1);

    const [search, setSearch] = useState(0);

    const [pairAddress, setPairAddress] = useState("");

    const [pairInfo, setPairInfo] = useState()

    const [pairInfoSwitch, setPairInfoSwitch] = useState(0)

    const [tokenName, setTokenName] = useState("")

    const [tokenSymbol, setTokenSymbol] = useState("")


    useEffect(() => {
        setPairs([]);
        const getPairs = async () => {
            const pairsFromServer = await fetchPairs();
            setPairs(pairsFromServer);
        };
        console.log("useEffect Enter");
        getPairs();
    }, [page]);

    //fetch pairs
    const fetchPairs = async () => {
        console.log(`fetchPairs - page ${page}`);
        console.log(`http://localhost:8000/latestpairs/${page - 1}`);
        const res = await fetch(`http://localhost:8000/latestpairs/${page - 1}`);
        const data = await res.json();
        return data;
    };

    const updateModal = (pair_address, token_name, token_symbol) => {
        setTokenName(token_name)
        setTokenSymbol(token_symbol)
        setPairAddress(pair_address)
        setPairInfoSwitch(1)

    };

    useEffect(() => {
        const getPairInfo = async () => {
            const pairInfoFromServer = await fetchPairsInfo()
            setPairInfo(pairInfoFromServer)
        }
        if (pairInfoSwitch == 1) {
            setPairInfo()
            setPairInfoSwitch(0)
            getPairInfo()

        }

    }, [pairAddress])

    const fetchPairsInfo = async () => {
        const res = await fetch(`http://localhost:8000/modal/${pairAddress}`)
        const data = await res.json()
        console.log(data)
        return data
    }

    return (
        <main>
            <div className="mb-4 ps-3">
                <h3>
                    Latest PancakeSwap Pairs
                    <a href="https://bscscan.com/address/0xca143ce32fe78f1f7019d7d551a6402fc5350c73" target="_blank" className="fs-6 link-primarier align-top text-decoration-none">
                        {" "}
                        factory
                    </a>
                </h3>
            </div>

            <div className="list-group mt-2 mx-auto py-4 rounded-12 bg-lessdarker position-relative">
                <span className="position-absolute top-0 start-97 translate-middle badge rounded-pill bg-page"> {page}</span>

                <div className="d-flex flex-row bg-lessdarker px-2 mb-2 justify-content-between">
                    <div className="d-flex align-items-end">
                        <div className="input-group">
                            <div className="input-group-prepend">
                                <button className="btn-page input-group-text fs-4 py-0" id="basic-addon1" onClick={() => setPage(search)}>
                                    ⇲
                                </button>
                            </div>
                            <input type="text" className="bg-darker text-secondary border-0 form-control" placeholder="page number" onChange={(e) => setSearch(e.target.value)} />
                            <button class="btn-page fs-4 py-0 ms-2">
                                <i className="bi bi-arrow-repeat" onClick={() => setPage(1)}></i>
                            </button>
                        </div>
                    </div>
                    <div>
                        <button type="button" className="btn-page">
                            <i className="bi-arrow-left-circle fs-3" onClick={() => setPage(parseInt(page) - 1)}></i>
                        </button>
                        <button type="button" className="btn-page">
                            <i className="bi-arrow-right-circle fs-3" onClick={() => setPage(parseInt(page) + 1)}></i>
                        </button>
                    </div>
                </div>
                <LatestPairModal pairInfo={pairInfo} tokenName={tokenName} tokenSymbol={tokenSymbol} />
                {pairs.map((pair) => (
                    <LatestPair key={pair.id} info={pair} onClick={(pair_address, token_name, token_symbol) => updateModal(pair_address, token_name, token_symbol)} />
                ))}
            </div>
        </main>
    );
};
