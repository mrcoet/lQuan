from typing import Optional


async def get_source_code(data):
    try:
        source_code = data["result"][0]["SourceCode"]
        return source_code
    except Exception as e:
        print("=" * 50)
        print("Error in --> pairModal --> miniAudit --> get_source_code")
        print("-" * 50)
        print(e)
        print("=" * 50)
        return False


async def using_router_v2(source_code: Optional[str]):
    if not source_code:
        return False
    router_addrss = "0xe56842Ed550Ff2794F010738554db45E60730371"
    if router_addrss.lower() in str(source_code).lower():
        return True
    else:
        return False


async def telegram_in_code(source_code: Optional[str]):
    if not source_code:
        return False
    if "telegram" in str(source_code).lower() or "t.me" in str(source_code).lower():
        return True
    return False


async def twitter_in_code(source_code: Optional[str]):
    if not source_code:
        return False
    if "twitter" in str(source_code).lower():
        return True
    return False


async def website_in_code(source_code: Optional[str]):
    if not source_code:
        return False
    if "website" in str(source_code).lower():
        return True
    return False


async def bad_in_code(path: str, source_code: Optional[str]):
    if not source_code:
        return False
    codeExceptionFile = open(path)
    lines = codeExceptionFile.readlines()
    warnings = []
    for line in lines:
        if line.strip().lower() in str(source_code).lower():
            warnings.append(line.strip())
    if len(warnings) > 0:
        out_ = {"warning": True, "warnings": warnings}
        return out_
    return {"warning": False, "warnings": []}
