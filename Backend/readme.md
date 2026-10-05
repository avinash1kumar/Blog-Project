# Blog REST API

A backend REST API for a Blog application built with **FastAPI, MySQL, SQLModel, JWT Authentication, and Pydantic**.

The API provides user authentication, profile management, and complete blog post CRUD operations with user-based authorization.

---

## 🚀 Features

### Authentication & Authorization
- User signup and login
- Password hashing using bcrypt
- JWT-based authentication
- JWT token expiration
- Protected API endpoints
- User identity verification through JWT
- Authorization for post update and deletion
- Users can only update or delete their own posts

### User Management
- Create a new user account
- Login using email and password
- View current user profile
- Update profile information
- Update password securely
- Delete user account
- Automatically delete user's posts when the account is deleted

### Blog Posts
- Create a new blog post
- Retrieve all blog posts
- Retrieve a single blog post
- Update a blog post
- Delete a blog post
- Display the author's name with posts
- Partial updates using PATCH

### API Validation & Documentation
- Request validation using Pydantic
- Response validation using Pydantic response schemas
- Automatic Swagger UI documentation
- HTTP status code and error handling
- Environment variables for sensitive configuration

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend programming language |
| FastAPI | REST API framework |
| MySQL | Relational database |
| SQLModel | ORM and database models |
| Pydantic | Request and response validation |
| JWT | Authentication |
| Passlib / bcrypt | Password hashing |
| Uvicorn | ASGI server |
| python-dotenv | Environment variable management |
| Swagger / OpenAPI | API documentation |

---

## 📁 Project Structure

Backend/
│
├── model/
│   ├── user.py
│   └── posts.py
│
├── schema/
│   ├── signup_user.py
│   ├── login_user.py
│   ├── update_user.py
│   ├── post_data.py
│   └── update_post.py
│
├── response_schema/
│   ├── user_routes_schemas.py
│   └── post_routes_schemas.py
│
├── routes/
│   ├── user_routes.py
│   └── post_routes.py
│
├── utils/
│   └── security.py
│
├── db.py
├── main.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md

