async def check_contract_version(data: dict):
    try:
        version = data["result"][0]["CompilerVersion"]
        version = version[0 : version.index("+")]
        return version
    except Exception as e:
        print("=" * 50)
        print("Error in --> pairModal --> contractVersion --> check_contract_version")
        print("-" * 50)
        print(e)
        print("=" * 50)
        return None
