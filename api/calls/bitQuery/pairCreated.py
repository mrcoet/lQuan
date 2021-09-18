from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport

from keys import bitquery_key


async def get_latest_pairs(limit: int, page: int):
    headers = {"X-API-KEY": bitquery_key, "Content-Type": "application/json"}

    transport = AIOHTTPTransport(url="https://graphql.bitquery.io", headers=headers)

    # Using `async with` on the client will start a connection on the transport
    # and provide a `session` variable to execute queries on this connection
    async with Client(transport=transport, fetch_schema_from_transport=True) as session:

        # Execute single query
        query = gql(
            """
            query ($network: EthereumNetwork!, $limit: Int!, $offset: Int!, $from: ISO8601DateTime, $till: ISO8601DateTime) {
                ethereum(network: $network) {
                    smartContractEvents(options: {desc: "block.height", limit: $limit, offset: $offset}, date: {since: $from, till: $till}, smartContractAddress: {is: "0xcA143Ce32Fe78f1f7019d7d551a6402fC5350c73"}, smartContractEvent: {is : "PairCreated"}) {
                        block {
                            height
                        }
                        arguments{
                            argument,
                            argumentType,
                            index,
                            value
                        }
                    }
                }
            }
        """
        )
        params = {"network": "bsc", "limit": limit, "offset": int(page * limit), "from": None, "till": None}
        result = await session.execute(query, variable_values=params)
        events_ = result["ethereum"]["smartContractEvents"]
        pairs_list = []
        for event_ in events_:
            args_dict = {}
            args = event_["arguments"]
            block = event_["block"]
            args_dict["blockNumber"] = block["height"]
            args_dict[args[0]["argument"]] = args[0]["value"]
            args_dict[args[1]["argument"]] = args[1]["value"]
            args_dict[args[2]["argument"]] = args[2]["value"]
            pairs_list.append(args_dict)
        return pairs_list
