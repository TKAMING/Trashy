from cs50 import SQL
db = SQL("sqlite:///trashy_user.db")

yellow_can_amount = db.execute("SELECT COUNT(yellow_can) FROM users WHERE yellow_can = yellow_can;")

print(yellow_can_amount)