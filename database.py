import sqlite3

DB_NAME = "expenses.db"

def get_connection():
    """Creates a connection to our database file"""
    return sqlite3.connect(DB_NAME)

def create_table():
    """Creates the expenses table if it doesn't already exist"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL,
            note TEXT
        )
    """)
    conn.commit()
    conn.close()
def add_expense(amount, category, date, note=""):
    """Adds a new expense record to the database"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO expenses (amount, category, date, note)
        VALUES (?, ?, ?, ?)
    """, (amount, category, date, note))
    conn.commit()
    conn.close()
    print("Expense added successfully!")
def view_expenses():
    """Fetches and returns all expense records"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses ORDER BY date DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows
def update_expense(expense_id, amount, category, date, note=""):
    """Updates an existing expense by its id"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE expenses
        SET amount = ?, category = ?, date = ?, note = ?
        WHERE id = ?
    """, (amount, category, date, note, expense_id))
    conn.commit()
    conn.close()
    print("Expense updated successfully!")

def delete_expense(expense_id):
    """Deletes an expense by its id"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    conn.close()
    print("Expense deleted successfully!")
def total_spend():
    """Returns the total amount spent across all expenses"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]
    conn.close()
    return total if total else 0

def spend_by_category():
    """Returns total spend grouped by category"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT category, SUM(amount)
        FROM expenses
        GROUP BY category
        ORDER BY SUM(amount) DESC
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows

def monthly_summary():
    """Returns total spend grouped by month"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT strftime('%Y-%m', date) AS month, SUM(amount)
        FROM expenses
        GROUP BY month
        ORDER BY month DESC
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows