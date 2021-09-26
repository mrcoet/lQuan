import moment from "moment"

export const LatestPairModal = ({ pairInfo, tokenName, tokenSymbol }) => {




    return (

        <>

            <div className="modal fade" id="pairsModal" tabindex="-1" aria-labelledby="pairsModalLabel" aria-hidden="true">
                <div className="modal-dialog modal-dialog-centered">
                    <div className="modal-content bg-darker rounded-12">
                        {
                            pairInfo ? (
                                <>
                                    {/* ++++++++++++ Header ++++++++++++ */}
                                    <div className="modal-header border-0 mt-3">
                                        <div className="d-flex flex-column mx-auto align-items-center" style={{ paddingLeft: "36px" }}>
                                            <a style={{ textDecoration: "none" }} className="modal-title text-light" target="_blank" href={`https://bscscan.com/token/${pairInfo.tokenAddress}`}><h5 className="modal-title" id="exampleModalLabel">{pairInfo.tokenName}</h5></a>
                                            <div className="d-flex align-items-center">
                                                <span className="p-1">{pairInfo.tokenSymbol} </span>
                                                <img className="p-1" src="/static/USDollar.svg" alt="ok" width="25px" height="25px" />
                                                <span className="p-1">{pairInfo.tokenPrice}</span>
                                            </div>
                                        </div>

                                        <button type="button" className="btn-page align-top" data-bs-dismiss="modal" aria-label="Close"
                                            style={{ marginTop: "-30px" }}><i className="bi bi-x fs-3 align-top"></i></button>
                                    </div>
                                    {/* ++++++++++++ Header ++++++++++++ */}

                                    <div className="modal-body d-flex flex-column">
                                        {/* ++++++++++++ Contract ++++++++++++ */}
                                        {pairInfo.contractVersion ? (
                                            <div className="d-flex align-items-center p-1">
                                                <img className="p-1" src="/static/Ok.svg" alt="ok" width="25px" height="25px" />
                                                <div className="p-1"><span className="opacity-25 pe-2">version</span>
                                                    <a style={{ textDecoration: "none" }} target="_blank" href={`https://bscscan.com/address/${pairInfo.tokenAddress}#code`}><span className="text-success">{pairInfo.contractVersion}</span></a>
                                                </div>
                                            </div>) : (<div className="d-flex align-items-center p-1">
                                                <img className="p-1" src="/static/Delete.svg" alt="not" width="25px" height="25px" />
                                                <div className="p-1"><span className="opacity-25 pe-2">version</span>
                                                    <a style={{ textDecoration: "none" }} target="_blank" href={`https://bscscan.com/address/${pairInfo.tokenAddress}#code`}><span className="text-danger">No Contract</span></a>
                                                </div>
                                            </div>)}
                                        {/* ++++++++++++ Contract ++++++++++++ */}

                                        {/* ++++++++++++ Honeypot ++++++++++++ */}

                                        <div className="d-flex align-items-center p-1">
                                            {(pairInfo.honeypot == "SWAP_FAILED") ?
                                                (<>
                                                    <img className="p-1" src="/static/Delete.svg" alt="ok" width="25px" height="25px" />
                                                    <div className="p-1"><span className="opacity-25 pe-2">honeypot</span>
                                                        <a style={{ textDecoration: "none" }} target="_blank" href={`https://honeypot.is/?address=${pairInfo.tokenAddress}`}><span className="text-danger">{pairInfo.honeypot}</span></a>
                                                    </div>
                                                </>)
                                                : (pairInfo.honeypot == "OK") ?
                                                    (
                                                        <>
                                                            <img className="p-1" src="/static/Ok.svg" alt="ok" width="25px" height="25px" />
                                                            <div className="p-1"><span className="opacity-25 pe-2">honeypot</span>
                                                                <a style={{ textDecoration: "none" }} target="_blank" href={`https://honeypot.is/?address=${pairInfo.tokenAddress}`}><span className="text-success">{pairInfo.honeypot}</span></a>
                                                            </div>
                                                        </>
                                                    )
                                                    :
                                                    (
                                                        <>
                                                            <img className="p-1" src="/static/Warning.svg" alt="ok" width="25px" height="25px" />
                                                            <div className="p-1"><span className="opacity-25 pe-2">honeypot</span>
                                                                <a style={{ textDecoration: "none" }} target="_blank" href={`https://honeypot.is/?address=${pairInfo.tokenAddress}`}><span className="text-warning">{pairInfo.honeypot}</span></a>
                                                            </div>
                                                        </>
                                                    )

                                            }

                                        </div>
                                        {/* ++++++++++++ Honeypot ++++++++++++ */}

                                        {/* ++++++++++++ Funny Name ++++++++++++ */}
                                        {pairInfo.funnyName ? (
                                            <div className="d-flex align-items-center p-1">
                                                <img className="p-1" src="/static/Delete.svg" alt="ok" width="25px" height="25px" />
                                                <div className="p-1"><span className="opacity-25 pe-2">offical</span>
                                                    <span className="text-danger">funny name/symbol detected.</span>
                                                </div>
                                            </div>) : (
                                            <div className="d-flex align-items-center p-1">
                                                <img className="p-1" src="/static/Ok.svg" alt="ok" width="25px" height="25px" />
                                                <div className="p-1"><span className="opacity-25 pe-2">offical</span>
                                                    <span className="text-success">no funny name/symbol detected.</span>
                                                </div>
                                            </div>)}
                                        {/* ++++++++++++ Funny Name ++++++++++++ */}

                                        {/* ++++++++++++ Token Owner ++++++++++++ */}
                                        <div className="d-flex align-items-center p-1">
                                            <img className="p-1" src="/static/Key.svg" alt="ok" width="25px" height="25px" />
                                            <div className="p-1 align-middle"><span className="opacity-25 pe-2">owner</span>
                                                <span style={{ fontSize: "12px" }}>{pairInfo.tokenOwner}</span>
                                            </div>
                                        </div>
                                        {/* ++++++++++++ Token Owner ++++++++++++ */}

                                        {/* ++++++++++++ Token Age ++++++++++++ */}
                                        <div className="d-flex align-items-center p-1">
                                            <img className="p-1" src="/static/Birthday.svg" alt="ok" width="25px" height="25px" />
                                            <div className="p-1 align-middle"><span className="opacity-25 pe-2">Deployed since</span>
                                                <span>{moment.unix(pairInfo.tokenAge).utc().fromNow()}</span>
                                            </div>
                                        </div>
                                        {/* ++++++++++++ Token Age ++++++++++++ */}

                                        {/* ++++++++++++ Token Holders ++++++++++++ */}
                                        <div className="d-flex align-items-center p-1">
                                            <img className="p-1" src="/static/People.svg" alt="ok" width="25px" height="25px" />
                                            <div className="p-1 align-middle"><span className="opacity-25 pe-2">Holders</span>
                                                <span style={{ fontSize: "12px" }}>{pairInfo.tokenHolders}</span>
                                            </div>
                                        </div>
                                        {/* ++++++++++++ Token Holders ++++++++++++ */}


                                        {/* ++++++++++++ Pair Liquidity ++++++++++++ */}
                                        <div className="d-flex flex-column  p-1">
                                            <div className="d-flex align-items-center">
                                                <img className="p-1" src="/static/Safe.svg" alt="ok" width="25px" height="25px" />
                                                <div className="p-1 align-middle"><span className="opacity-25 pe-2">Liquidity</span>
                                                    <a target="_blank" href={`https://bscscan.com/token/${pairInfo.pairAddress}#balances`} ><span className="text-warning">{pairInfo.mCap} BNB</span></a>
                                                </div>
                                            </div>
                                            <div className="d-flex">
                                                <div className="me-3" style={{ borderLeft: "2px solid #14B6B9", marginLeft: "12px", }}>

                                                </div>
                                                <div>
                                                    <div className="p-1 align-middle">
                                                        <span>{pairInfo.lockers.burn}%</span><span className="opacity-25 ps-3">Burn</span>
                                                    </div>
                                                    <div className="p-1 align-middle">
                                                        <span>{pairInfo.lockers.deepLocker}%</span><span className="opacity-25 ps-3">DeepLocker</span>
                                                    </div>
                                                    <div className="p-1 align-middle">
                                                        <span>{pairInfo.lockers.unicrypt}%</span><span className="opacity-25 ps-3">UnicryptLocker</span>
                                                    </div>
                                                    <div className="p-1 align-middle">
                                                        <span>{pairInfo.lockers.cakeMainStaking}%</span><span className="opacity-25 ps-3">Cake main staking</span>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        {/* ++++++++++++ Pair Liquidity ++++++++++++ */}

                                        {/* ++++++++++++ Source Code analysis ++++++++++++ */}
                                        <div className="d-flex flex-column  p-1">
                                            <div className="d-flex align-items-center">
                                                <img className="p-1" src="/static/Ethereum.svg" alt="ok" width="25px" height="25px" />
                                                <div className="p-1 align-middle"><span style={{ color: "#7986CB" }}>source code analysis</span>
                                                </div>
                                            </div>
                                            <div className="d-flex">
                                                <div className="me-3" style={{ borderLeft: "2px solid  #7986CB", marginLeft: "12px" }}>
                                                </div>
                                                <div>


                                                    {pairInfo.badMethods ? (<>
                                                        <div className="d-flex align-items-center">
                                                            <img className="p-1" src="/static/Ok.svg" alt="ok" width="25px" height="25px" />
                                                            <div className="p-1 align-middle"><span className="opacity-25 pe-2">Social media in code</span>
                                                                {pairInfo.socialMedia.telegram && <img className="p-1" src="/static/Telegram App.svg" alt="ok" width="25px" height="25px" />}
                                                                {pairInfo.socialMedia.twitter && <img className="p-1" src="/static/Twitter.svg" alt="ok" width="25px" height="25px" />}
                                                                {pairInfo.socialMedia.website && <img className="p-1" src="/static/Brave.svg" alt="ok" width="25px" height="25px" />}
                                                            </div>
                                                        </div>
                                                        {pairInfo.badMethods.warning ? (<><div className="d-flex align-items-center">
                                                            <img className="p-1" src="/static/Delete.svg" alt="not" width="25px" height="25px" />
                                                            <div className="p-1 align-middle"><span className="opacity-25 pe-2">Foudn bad methods</span>
                                                            </div>
                                                        </div>
                                                            <div className="d-flex">
                                                                <div className="" style={{ borderLeft: "2px solid  rgb(224 79 95)", marginLeft: "12px" }}></div>
                                                                <div className="d-flex flex-column">
                                                                    <ul style={{ listStyleType: "none", paddingLeft: "20px" }}>
                                                                        {pairInfo.badMethods.warnings.map((bad) => <li style={{ fontSize: "10px" }}>{bad}</li>)}

                                                                    </ul>
                                                                </div>
                                                            </div></>
                                                        ) : (<div className="d-flex align-items-center">
                                                            <img className="p-1" src="/static/Ok.svg" alt="not" width="25px" height="25px" />
                                                            <div className="p-1 align-middle"><span className="opacity-25 pe-2">No Bad Methods</span>
                                                            </div>
                                                        </div>)}


                                                    </>) : (<div className="d-flex align-items-center">
                                                        <img className="p-1" src="/static/Delete.svg" alt="not" width="25px" height="25px" />
                                                        <div className="p-1 align-middle"><span className="opacity-25 pe-2">contract not verfied</span>
                                                        </div>
                                                    </div>)}



                                                </div>
                                            </div>
                                        </div>
                                        {/* ++++++++++++ Source Code analysis ++++++++++++ */}


                                    </div>

                                    <div className="modal-footer border-0 mb-3 px-5">
                                        <div className="d-flex justify-content-center justify-content-evenly w-100">
                                            <a target="_blank" href={`https://tokensniffer.com/token/${pairInfo.tokenAddress}`}><img src="/static/tokensniffer.svg" alt="ok" width="25px" height="25px" /></a>
                                            <a target="_blank" href={`https://poocoin.app/tokens/${pairInfo.tokenAddress}`}><img src="/static/poocoin.svg" alt="ok" width="25px" height="25px" /></a>
                                            <a target="_blank" href={`https://www.google.com/search?q="${pairInfo.tokenName}"`}><img src="/static/google.svg" alt="ok" width="25px" height="25px" /></a>
                                            <a target="_blank" href={`https://www.reddit.com/search/?q="${pairInfo.tokenAddress}"`}><img src="/static/reddit.svg" alt="ok" width="25px" height="25px" /></a>
                                            <a target="_blank" href={`https://twitter.com/search?q="${pairInfo.tokenName}"`}><img src="/static/twitter1.svg" alt="ok" width="25px" height="25px" /></a>
                                            <a target="_blank" href={`https://twitter.com/search?q="${pairInfo.tokenAddress}"`}><img src="/static/twitter2.svg" alt="ok" width="25px" height="25px" /></a>
                                            <a target="_blank" href={`https://www.bscheck.eu/${pairInfo.tokenAddress}`}><img src="/static/bscan.svg" alt="ok" width="25px" height="25px" /></a>
                                            <a target="_blank" href={`https://www.dextools.io/app/bsc/pair-explorer/${pairInfo.tokenAddress}`}><img src="/static/dextools.svg" alt="ok" width="25px" height="25px" /></a>
                                            <a target="_blank" href={`https://dex.guru/token/${pairInfo.tokenAddress}-bsc`}><img src="/static/dexguru.svg" alt="ok" width="25px" height="25px" /></a>
                                        </div>
                                    </div>


                                </>
                            ) : (
                                <>
                                    <div className="modal-header border-0 mt-3">
                                        <div className="d-flex flex-column mx-auto align-items-center" style={{ paddingLeft: "36px" }}>
                                            <h5 className="modal-title" id="exampleModalLabel">{tokenName}</h5>
                                            <div className="d-flex align-items-center">
                                                <span className="p-1">{tokenSymbol} </span>
                                            </div>
                                        </div>

                                        <button type="button" className="btn-page align-top" data-bs-dismiss="modal" aria-label="Close"
                                            style={{ marginTop: "-30px" }}><i className="bi bi-x fs-3 align-top"></i></button>
                                    </div>
                                    <div className="modal-header border-0 mt-3">
                                        <div className="d-flex flex-column mx-auto align-items-center p-4">
                                            <img src="/static/rings.svg" alt="waiting" width="50px" height="50px" />
                                        </div>
                                    </div>
                                </>

                            )
                        }
                    </div>
                </div>
            </div>
        </>
    )
}
