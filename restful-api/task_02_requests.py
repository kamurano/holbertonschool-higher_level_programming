#!/usr/bin/python3
import requests

def fetch_and_print_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    posts = response.json()
    print("Status Code: {:d}".format(response.status_code))
    for post in posts:
        print(post['title'])

def fetch_and_save_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    posts = response.json()
    with open('posts.csv', 'w') as file:
        file.write("id,title,body\n")
        for post in posts:
            file.write(f"{post['id']}, {post['title']}, {post['body']}\n")

if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
