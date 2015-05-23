import sqlite3
from prettytable import PrettyTable


db = sqlite3.connect("company.db")
db.row_factory = sqlite3.Row
cursor = db.cursor()

print("Available commands:\nlist_employees\n\
monthly_spending\nyearly_spending\nadd_employee\n\
delete_employee <employee_id>\nupdate_employee <employee_id>")
command = input("command> :")


def list_employees():
    table = PrettyTable(["id", "name", "position"])
    info = cursor.execute("SELECT id, name, position FROM company")
    for row in info:
        table.add_row([row["id"], row["name"], row["position"]])
    print(table)


def monthly_spending():
    info = cursor.execute("SELECT monthly_salary FROM company")
    salary = sum([row["monthly_salary"] for row in info])
    print("Monthly spending of company: {}$".format(salary))


def yearly_spending():
    info = cursor.execute("SELECT monthly_salary, yearly_bonus FROM company")
    total = sum(
        [12 * row["monthly_salary"] + row["yearly_bonus"] for row in info])
    print(total)


def add_employee():
    name = input("name> ")
    salary = int(input("monthly_salary> "))
    bonus = int(input("yearly_bonus> "))
    position = input("position> ")
    cursor.execute("""INSERT INTO company(name, monthly_salary, yearly_bonus, position)
    VALUES(?,?,?,?)""", (name, salary, bonus, position))
    db.commit()


def delete_employee(num):
    cursor.execute("DELETE FROM company WHERE id = ?", (num))
    db.commit()


def update_employee(num):
    name = input("name> ")
    salary = int(input("monthly_salary> "))
    bonus = int(input("yearly_bonus> "))
    position = input("position> ")
    cursor.execute("""UPDATE company SET name = ?,
                                       monthly_salary = ?,
                                       yearly_bonus = ?,
                                       position = ?
                    WHERE id = ?""", (name, salary, bonus, position, num))
    db.commit()

commands = {
           "list_employees": list_employees,
           "monthly_spending": monthly_spending,
           "yearly_spending": yearly_spending,
           "add_employee": add_employee,
           "delete_employee": delete_employee,
           "update_employee": update_employee
           }


def main():
    user_command = command.split()[0]
    try:
        user_id = command.split()[1]
        commands[user_command](user_id)
        print("I deleted")
    except:
        commands[user_command]()

if __name__ == '__main__':
    main()
