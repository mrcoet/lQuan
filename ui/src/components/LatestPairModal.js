import { useState, useEffect } from "react"

export const LatestPairModal = ({ tokenName, tokenSymbol }) => {
    return (
        <>
            <div class="modal fade" id="pairsModal" tabindex="-1" aria-labelledby="pairsModalLabel" aria-hidden="true">
                <div class="modal-dialog modal-dialog-centered">
                    <div class="modal-content bg-darker rounded-12">
                        <div class="modal-header border-0">
                            <h5 class="modal-title mx-auto" id="exampleModalLabel">{tokenName}</h5>
                            <h6 class="mx-auto">{tokenSymbol}</h6>
                            <button type="button" class="btn-page" data-bs-dismiss="modal" aria-label="Close"><i class="bi bi-x fs-3"></i></button>
                        </div>
                        <div class="modal-body d-flex flex-column align-items-center"></div>
                    </div>
                </div>
            </div>
        </>
    )
}
