from flask import Flask, request, redirect, url_for, render_template
import mysql.connector

app = Flask(__name__)

db_config = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'library_db'
}
def get_db_connection():
    conn = mysql.connector.connect(**db_config)
    return conn



@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO books (title, author, year) VALUES (%s, %s, %s)', (title, author, year))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']
        cursor.execute('UPDATE books SET title=%s, author=%s, year=%s WHERE id=%s', (title, author, year, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    else:
        cursor.execute('SELECT * FROM books WHERE id=%s', (id,))
        book = cursor.fetchone()
        conn.close()
        return render_template('update.html', book=book)

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM books WHERE id=%s', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
