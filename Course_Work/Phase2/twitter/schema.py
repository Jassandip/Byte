#!/usr/bin/env python3

from mapper import Database 

if __name__ == '__main__':
    with Database('master.db') as db:
        db.create_table('users')
        db.add_column('users','username','VARCHAR')
        db.add_column('users','password','VARCHAR')
        db.create_table('tweets')
        db.add_column('tweets','username','VARCHAR')
        db.add_column('tweets','tweet','VARCHAR')
        db.add_column('tweets','date','VARCHAR')
        db.create_table('friends')
        db.add_column('friends','username','VARCHAR')
        db.add_column('friends','friends','VARCHAR')
        print('System agent: Database created.')
