from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport


async def latest_pairs(limit: int, page: int):
    headers = {"Content-Type": "application/json"}
    transport = AIOHTTPTransport(url="https://bsc.streamingfast.io/subgraphs/name/pancakeswap/exchange-v2", headers=headers)
    async with Client(transport=transport, fetch_schema_from_transport=True) as session:
        query = gql(
            """
         query ($limit: Int!, $skip: Int!) {
            pairs(first: $limit, skip: $skip,  orderBy: block, orderDirection: desc) {
                id
                token0 {
                    id
                    name
                    symbol
                    derivedUSD
                }
                token1 {
                    id
                    name
                    symbol
                    derivedUSD
                }
                reserve0
                reserve1
                block
                
            }
            }

         """
        )
        params = {"limit": limit, "skip": int(page * limit)}
        result = await session.execute(query, variable_values=params)
        return result["pairs"]
