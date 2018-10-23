#!/usr/bin/env python3

import json

from mapper import Database 

if __name__ == '__main__':
    with Database('master.db') as db:
        db.create_table('users')
        db.add_column('users','username','VARCHAR')
        db.add_column('users','password','VARCHAR')
        print('System agent: Database created.')
