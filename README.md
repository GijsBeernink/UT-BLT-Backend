# BLT_Backend
Blockchain and Distriuted Ledger Technologies Project

### API Keys

Get API keys for the following services:
* [BitcoinAbuse](https://www.bitcoinabuse.com/api-docs) to get reported addresses
* [Blockchain.com](https://www.blockchain.com/api) to get the data from the bitcoin blockchain

Store these API keys in the `local.py` file.

### Running

To run the application simply enter the address and depth to search in the `main.py` file.
Keep in mind that searching for new addresses can take a while since we query the Blockchain.com
 API endpoints and don't want to get blocked. To see fast results use the following as the
  resulting addresses are already requested from the API endpoint:
 
```
ADDRESS = '1LYz7EgAF8PU6bSN8GDecnz9Gg814fs81W'

DEPTH = 2
```

To see the results open the `Frontend.html` page and wait until it is loaded. Note that due to an issue with Remote Content Policy, Google Chrome does currently *not* work!
