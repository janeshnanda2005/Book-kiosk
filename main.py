import requests
import datetime
import csv


# Replace 'YOUR_API_KEY' with your actual Google Books API key
API_KEY = 'AIzaSyARlrYxIKVkTUQLXA796cQjxWZXcx-BHFI'

def main(isbn):
    url = f'https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}&key={API_KEY}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # Check if the book exists in the response
        if 'items' in data:
            book_title = data['items'][0]['volumeInfo']['title']
            return book_title

        else:
            return "No book found with this ISBN."
    else:
        return "Failed to retrieve data."


def write_book():
    with open('dataisbn.csv',mode='a',newline = "") as file:
        while True:
            print("Hello there Drop Your Book in Box!!")
            isbn_book1 = input("Scan Your Book :")
            val_1 = datetime.datetime.now()
            book1 = main(isbn_book1)
            print(f"Book Title: {book1}")
            print("Done!!")
            isbn_book2= input("Scan Your New Book :")
            val_2 = datetime.datetime.now()
            book2 = main(isbn_book2)
            print(f"Book Title: {book2}")
            print("Do visit us again!!")
            writer = csv.writer(file)
            writer.writerow([book1,val_1,book2,val_2])
    file.close()
        
write_book()
