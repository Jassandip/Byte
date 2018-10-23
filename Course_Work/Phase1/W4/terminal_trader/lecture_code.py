def buy():

def check_balance(self,user_id):
    cursor.execute=("""SELECT balance 
    FROM users 
    WHERE user_id=={}
    ;""".format(user_id)
    balance = self.cursor.fetchone()
    return balance[0]

def signup(self,_username,_password):
    self.cursor.execute(
        """"INSERT INTO users(
            username,
            password,
            balance
        ) VALUES(
            {username},
            {password},
            {balance}
        );""".format(
            username=_username,
            password=_password,
            balance=10000.
        )
    )
def