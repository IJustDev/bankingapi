Banking API
***********

Quick Start for DKB
###################

Initializing the API::

    from bankingapi.DKB import Api

    def main():
        dkb = Api()
        dkb.init_api(("username", "banking-pin"))
        balance = dkb.fetch_balance()
        for transaction_page in dkb.fetch_all_transactions():
            for transaction in transaction_page:
                print(transaction)
        dkb.close_browser()
        return balance

    print(main())