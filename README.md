# 📚 Books REST API: CRUD Operations & Authentication

## 🌟 Description
Welcome to the **Books REST API**! 📖 This API lets you manage books with ease. Non-authenticated users can browse and search the book list, while authenticated users can create, read, update, and delete their own books. It also supports pagination for smooth data handling. 🚀

## ✨ Features
- 🛠️ Built with Django, Python, and Django REST Framework
- 🔒 Secure JWT-based authentication using `djangorestframework_simplejwt`
- 📝 Full CRUD operations for authenticated users
- 🔍 Search functionality for discovering books
- 📄 Pagination for efficient book listings

## 🛠️ Tech Stack
- 🐍 Python
- 🌐 Django
- ⚙️ Django REST Framework
- 🔐 Django REST Framework SimpleJWT

## 🚀 Installation Instructions
Get started in a few simple steps:

1. **Clone the repository** to your local machine.
2. Ensure **Python** is installed (version 3.8+ recommended).
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up the database and apply migrations:
   ```bash
   python manage.py migrate
   ```
5. Launch the development server:
   ```bash
   python manage.py runserver
   ```

## 📖 Usage Examples
Explore the API with these endpoints (base URL: `http://localhost:8000/api/v1/`):

- **📋 List & Create Books**:
  - `GET /books`: View all books (open to everyone).
  - `POST /books`: Add a new book (authenticated users only).
- **📕 Book Details**:
  - `GET /books/1/`: Get details of book with ID=1.
- **✍️ Update a Book**:
  - `PUT /books/1/update`: Update book with ID=1 (authenticated users only).
- **🗑️ Delete a Book**:
  - `DELETE /books/1/delete`: Delete book with ID=1 (authenticated users only).
- **🔎 Search Books**:
  - `GET /books/?search=hello`: Find books containing "hello".
- **📑 Pagination**:
  - `GET /books/?limit=10&offset=2`: Fetch 10 books, starting from the 3rd record.

## 📜 License
This project has no license specified.