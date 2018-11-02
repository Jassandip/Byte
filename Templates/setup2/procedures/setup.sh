#!/usr/bin/env bash 

wget https://www.multichain.com/download/multichain-1.0.6.tar.gz -O /tmp/multichain.tar.gz
tar -xvzf /tmp/multichain.tar.gz 
mv multichain-1.0.6 ../opt
cd ../opt/multichain-1.0.6
mv multichaind multichain-cli multichain-util ../../usr/local/bin
