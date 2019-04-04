.. toctree::
   :maxdepth: 2
   dkb-quickstart

**********
BankingAPI
**********

Introduction
############
This banking API made possible through selenium and geckodriver is able to fetch your current balance via simulating a user clicking the actual fields for getting to your balance.
Because initializing the browser clicking the links and so on, it is recommended to fetch your balance or last transactions once per hour and store the results in a database of your choice.
Currently the API provides access to the DKB fetch_balance() and fetch_all_transactions() method. Each of them self explainationary.

Attention!
##########
I do not recommend uploading your script with the credentials to a foreign server. Always be careful when you've got such private information in code!
