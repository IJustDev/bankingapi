Banking API
***********

Quick Start for DKB
###################

Initializing the API::

    from bankingapi.DKB import Api

    def main():
        dkb = Api()
        dkb.init_Api(("username", "banking-pin"))
        balance = dkb.fetch_balance()
        return balance

    print(main())