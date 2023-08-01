from flask import Flask, request, jsonify
import json
""" import sqlite3 """
import pymysql
from dotenv import load_dotenv



# Carga las variables de entorno desde el archivo .env
load_dotenv()
app = Flask(__name__)

## DAR LA RUTA COMPLETA ASI NO PERESENTA PROBLEMAS EN EJECUTAR 
""" with open("src/Books.json")as json_file:
    data = json.load(json_file)

books_list = data["books"] """


def db_connection():
    conn = None
    try:
        conn = pymysql.connect(  host="localhost",
        database='my_database',
        user='my_user',
        password='my-secret-password',
        charset='utf8mb4'
    )
    except pymysql.error as e:
        print(e)
    return conn



@app.route('/')
def index():
    return "Heloo World"

@app.route('/<name>')
def print_name(name:str):
    return 'Welcome, {}'.format(name)


@app.route("/books", methods= ["GET", "POST"])
def books():
    

    conn = db_connection()
    cursor = conn.cursor()



    if request.method =="GET":
      cursor.execute("SELECT * FROM book")

      books =[
          dict ( id = row[0], language=row[1], author= row[2], title=row[3] )
          for row in cursor.fetchall()
      ]
      if books is not None:
          return jsonify(books)

      """   if len(books_list) > 0:
            return jsonify(books_list)
        else:
            "Nothing Found", 404
     """
      

    if request.method == "POST":
        new_author = request.form["author"]
        new_lang = request.form["language"]
        new_title = request.form["title"]
        """   id_book = books_list[-1]["id"]+1 """
        sql = """INSERT INTO book (author, language, title)
                 VALUES (%s, %s, %s)"""
        cursor.execute(sql, (new_author, new_lang, new_title))
        conn.commit()
        return f"Book with the id: { cursor.lastrowid } created seccesfully", 201

        """     new_obj = {
        "id": id_book,
        "author": new_author,
        "language":new_lang,
        "title": new_titlle
       } """
    """     books_list.append(new_obj) """



@app.route('/book/<int:id>', methods=["GET","PUT","DELETE"])
def single_book(id:int):
    """ if request.method =="GET":
        for book in books_list:
            if book['id'] ==id:
                return jsonify(book)
            pass
    """

    conn = db_connection()
    cursor = conn.cursor()
    book = None
    if request.method == "GET":
        cursor.execute("SELECT * FROM book WHERE id=%s", (id,))
        rows = cursor.fetchall()
        for r in rows:
            book = r
        if book is not None:
            return jsonify(book), 200
        else:
            return "Something wrong", 404
        
    if request.method == "PUT":
        sql = """UPDATE book
                SET title=%s,
                    author=%s,
                    language=%s
                WHERE id=%s """

        author = request.form["author"]
        language = request.form["language"]
        title = request.form["title"]
        updated_book = {
            "id": id,
            "author": author,
            "language": language,
            "title": title,
        }
        cursor.execute(sql, (author, language, title, id))
        conn.commit()
        return jsonify(updated_book)


    if request.method == "DELETE":
        sql = """ DELETE FROM book WHERE id=%s """
        cursor.execute(sql, (id,))
        conn.commit()
        return "The book with id: {} has been ddeleted.".format(id), 200
    

"""     if request.method =="PUT":
        for book in books_list:
            if book['id'] ==id:
                book["author"]  = request.form["author"]
                book["language"] = request.form["language"]
                book["title"] = request.form["title"]

                update_book ={
                    "id": id,
                    "author":    book["author"],
                    "language":book["language"],
                    "title": book["title"]
                }
                return jsonify(update_book) """
              
"""     if request.method =="DELETE":
        for index, book in enumerate(books_list):
            if book["id"] == id:
                books_list.pop(index)
                return jsonify(books_list)
            
 """


if __name__== '__main__':
    app.run(debug=True)


    """ CREAR VARIABLES DE ENTORNO

        BASH
        export FLASK_APP=src/app.py
        export FLASK_DEBUG=1

        EJECUTAR
        flask run

      
    """