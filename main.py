import requests
import datetime
import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase Admin SDK
cred = credentials.Certificate('C:\Vignesh\main\Book-kioskcred.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://book-kiosk-93f35-default-rtdb.europe-west1.firebasedatabase.app'
})

API_KEY = 'AIzaSyARlrYxIKVkTUQLXA796cQjxWZXcx-BHFI'

def main(isbn):
    url = f'https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}&key={API_KEY}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
       
        if 'items' in data:
            book_title = data['items'][0]['volumeInfo']['title']
            return book_title
 
        else:
            return "No book found with this ISBN."
    else:
        return "Failed to retrieve data."

def write_book():
    counter = 1
    while True:
        print("Hello there Drop Your Book in Box!!")
        isbn_book1 = input("Scan Your Book :")
        book1 = main(isbn_book1)
        
        if book1 in ["No book found with this ISBN.", "Failed to retrieve data."]:
            continue
        
        
        print(f"Book Title: {book1}")
        print("Done!!")
        
        
        isbn_book2 = input("Scan Your New Book :")
        val_1 = datetime.datetime.now().isoformat()
        book2 = main(isbn_book2)
        
        
        print(f"Book Title: {book2}")
        print("Do visit us again!!")
        
        data = {
            'ID': f'{counter}',
            'book_1': f'{book1}',
            'book_2': f'{book2}',
            'date_time': f'{val_1}'
        }
        

        ref = db.reference('books')
        ref.push(data)
        
        counter += 1

write_boo
