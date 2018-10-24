#!/usr/bin/env bash

# Environment variables
BLOCKCHAIN_NAME=$(cat ./reference/black/blockchain_name.txt) 


# Iniitialize parameters
multichain-util create $BLOCKCHAIN_NAME

# Create blockchain
multichaind $BLOCKCHAIN_NAME -daemon


