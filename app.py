from flask import Flask, request, redirect, url_for, render_template
import mysql.connector

app = Flask(__name__)

db_config = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'library_db'
}

