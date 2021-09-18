import moment from 'moment';


export const LatestPair = ({ info, onClick }) => {



    return (

        <>

            <a type="button" className="list-group-item d-flex gap-3 py-3 border-0 bg-lessdarker text-light" data-bs-toggle="modal" data-bs-target="#pairsModal" onClick={() => onClick(info.pairAddress, info.quoteTokenAddres, info.quoteTokenName, info.quoteTokenSymbol, info.mCap)}>
                {/* <img src="https://github.com/twbs.png" alt="twbs" width="32" height="32" className="rounded-circle flex-shrink-0 my-auto" /> */}

                {info.quoteTokenLogo ? <img src={`data:image/png;base64,${info.quoteTokenLogo}`} width="32" height="32" className="rounded-circle flex-shrink-0 my-auto" /> : <img src="/static/empty-token-bnb.png" width="32" height="32" className="rounded-circle flex-shrink-0 my-auto" />}

                <div className="d-flex gap-2 w-100 justify-content-between">
                    <div>
                        <h6 className="mb-0">{info.quoteTokenSymbol}</h6>
                        <p className="mb-0 opacity-75">{info.quoteTokenName}</p>
                    </div>
                    <div>
                        <h6 className="mb-0 text-end">{parseInt(info.mCap)} <b className="text-warning">฿₦฿</b></h6>
                        <p className="mb-0 opacity-75 text-end fst-italic">{moment.unix(info.quoteTokenAge).utc().fromNow()}</p>
                    </div>
                </div>
            </a>


        </>


    )
}
