from pydantic import BaseModel
from typing import Optional


class Token(BaseModel):
    id: int
    address: str = "0x000"
    name: str = "safemoon"
    symbol: str = "SAFEMOON"
    age: int = 1223432
    decimals: int = 18
    logo: Optional[bytes]


token_ = Token(id=1)
token_.logo = b"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"

print(token_)