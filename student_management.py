from flask import Flask, request, redirect, url_for, render_template_string
import sqlite3

app = Flask(__name__)

# ---------------- Database Setup ----------------
def init_db():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            enrollment TEXT NOT NULL,
            name TEXT NOT NULL,
            age INTEGER,
            course TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# ---------------- Home Page ----------------
@app.route('/')
def home():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    conn.close()

    html = '''
    <html>
    <head>
        <title>Student Management System</title>
    </head>
    <body>
        <h2>Add Student</h2>
        <form method="POST" action="/add">
            Enrollment No: <input type="text" name="enrollment" required><br><br>
            Name: <input type="text" name="name" required><br><br>
            Age: <input type="number" name="age" required><br><br>
            Course: <input type="text" name="course" required><br><br>
            <input type="submit" value="Add Student">
        </form>

        <h2>Student List</h2>
        <table border="1" cellpadding="10">
            <tr>
                <th>ID</th>
                <th>Enrollment No</th>
                <th>Name</th>
                <th>Age</th>
                <th>Course</th>
                <th>Action</th>
            </tr>
            {% for student in students %}
            <tr>
                <td>{{ student[0] }}</td>
                <td>{{ student[1] }}</td>
                <td>{{ student[2] }}</td>
                <td>{{ student[3] }}</td>
                <td>{{ student[4] }}</td>
                <td>
                    <a href="/delete/{{ student[0] }}">Delete</a>
                </td>
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    '''

    return render_template_string(html, students=students)

# ---------------- Add Student ----------------
@app.route('/add', methods=['POST'])
def add_student():
    enrollment = request.form['enrollment']
    name = request.form['name']
    age = request.form['age']
    course = request.form['course']

    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO students (enrollment, name, age, course)age, course) VALUES (?, ?, ?)',
                   (name, age, course))
    conn.commit()
    conn.close()

    return redirect(url_for('home'))

# ---------------- Delete Student ----------------
@app.route('/delete/<int:id>')
def delete_student(id):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM students WHERE id = ?', (id,))
    conn.commit()
    conn.close()

    return redirect(url_for('home'))

# ---------------- Run App ----------------
if __name__ == '__main__':
    app.run(debug=True)
