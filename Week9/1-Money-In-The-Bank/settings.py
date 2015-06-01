DB_NAME = "bank.db"
SQL_FILE = "bank.sql"

UPDATE_MESSAGE = """UPDATE clients
SET message = '%s'
WHERE id = '%s'
% (new_message, logged_user.get_id())"""

UPDATE_PASS = """UPDATE clients
SET password = '%s'
WHERE id = '%s'
% (new_pass, logged_user.get_id())"""

INSERT_SQL = """INSERT INTO clients (username, password)
VALUES ('%s', '%s') % (username, password)"""

SELECT_QUERY = """SELECT id, username, balance, message
FROM clients
WHERE username = '%s'
AND password = '%s'
LIMIT 1
% (username, password)"""

DEPOSIT_SQL = """UPDATE clients
SET balance = '%s'
WHERE id = '%s'
% (deposit_sum, logged_user.get_id())"""
