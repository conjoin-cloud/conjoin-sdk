from __future__ import annotations

import os

from conjoin_cloud import Conjoin


def main() -> None:
    api_key = os.environ["CONJOIN_API_KEY"]
    app_id = os.environ["CONJOIN_AUTH_APP_ID"]

    with Conjoin(api_key=api_key, auth_app_id=app_id) as client:
        page = client.auth.accounts.list()

        for account in page.data:
            print(account.account_id)


if __name__ == "__main__":
    main()
