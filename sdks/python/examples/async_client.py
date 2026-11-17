from __future__ import annotations

import asyncio
import os

from conjoin_cloud import AsyncConjoin


async def main() -> None:
    api_key = os.environ["CONJOIN_API_KEY"]
    app_id = os.environ["CONJOIN_AUTH_APP_ID"]

    async with AsyncConjoin(api_key=api_key, auth_app_id=app_id) as client:
        page = await client.auth.accounts.list()

        async for account in page.iter_all():
            print(account.account_id)


if __name__ == "__main__":
    asyncio.run(main())
