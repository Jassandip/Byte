#What is blockchain? 
    y = f(x)
    hash = heashing_function(str)

genesis block - is the first block mined first in the blockchain

#3 Main Types of CC:
- Cash: Bitcoin
- Fuel: Ether
- Vouchers: Fileocoin

#Reasons why people couldn't install a digital cash
1. The byzantine Generals Problem
2. Double-spending attacks

#Read
- Easyang 
    - the cryptography og bitcoin 
- Bitcoins academic pedegery
- dev ops stuff
- json being a searlized object
- programming from the ground up
- burnaddress  
- bitcoin cryptocurrency technology by anand naryan 
- crytoassets 
- chmod
- multichain.com/developers/getting-started/
- multichain.com/developers/streamed-confidentiality/

#Definition
Big O notation - how an algorithm slows as a the data grows
tar.gz - is a compressed file
10.17.0.7:4257 - an ip-address that starts with 10 means its only accessiable wihtin the server
chmod - change mode


#Questions
1. Do collisions accidentaly happen? 

#Bash Commands
## To set up
    wget https://www.multichain.com/download/multichain-1.0.6.tar.gz -O /tmp/multichain.tar.gz
    tar -xvzf /tmp/multichain.tar.gz 
    mv multichain-1.0.6 ../opt
    cd ../opt/multichain-1.0.6
    mv multichaind multichain-cli multichain-util ../../usr/local/bin

    or 

    scp setup.zip root@{ip-address}:/tmp
    
    ./tmp/setup.sh
    multichaind jashanchain -daemon

- tar -v - verbose
- nano ~/.multichain/chain1/params.dat - shows parameters 
- help - has all the commands and the parameters 
- getinfo - general abstract 
- getblockchainparams - the whole paper
- multichain-cli chain1 - starts interactive mode 
- getpeerinfo - shows your 
- curl x POST "https://api.digitalocean.com/v2/droplets" -d 