#!/usr/bin/env bash

# Iniitialize parameters
multichain-util create jashanchain

# Create blockchain
multichaind jashanchain -daemon
