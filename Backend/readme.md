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
```
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
```
---

## 🔐 Authentication Flow
- The API uses JWT-based authentication.

### Signup
```
Client
   ↓
POST /auth/signup
   ↓
Validate user data
   ↓
Hash password
   ↓
Store user in MySQL
   ↓
Return user information
```

### Login
```
Client
   ↓
POST /auth/login
   ↓
Verify email and password
   ↓
Create JWT
   ↓
Return access token
```

---

## 🔒 Security

The project implements several basic backend security practices:

- Passwords are hashed before database storage.
- Password hashes are never returned in API responses.
- JWT tokens are used for authentication.
- JWT tokens have an expiration time.
- Protected endpoints require authentication.
- Users cannot modify another user's posts.
- Users cannot delete another user's posts.
- Sensitive configuration is stored using environment variables.
- User input is validated using Pydantic.

---

---

## 📌 API Endpoints

### Authentication & User

| Method | Endpoint | Description | Authentication |
|--------|----------|-------------|----------------|
| POST | `/auth/signup` | Create a new user | ❌ |
| POST | `/auth/login` | Login and receive JWT token | ❌ |
| GET | `/auth/profile` | Get current user profile | ✅ |
| PATCH | `/auth/profile` | Update current user profile | ✅ |
| DELETE | `/auth/profile` | Delete current user account | ✅ |

### Blog Posts

| Method | Endpoint | Description | Authentication |
|--------|----------|-------------|----------------|
| POST | `/posts` | Create a new blog post | ✅ |
| GET | `/posts` | Get all blog posts | ✅ |
| GET | `/posts/{post_id}` | Get a single blog post | ✅ |
| PATCH | `/posts/{post_id}` | Update your own blog post | ✅ |
| DELETE | `/posts/{post_id}` | Delete your own blog post | ✅ |


---

## 📚 API Documentation

FastAPI automatically provides interactive API documentation using Swagger UI.

Run the application and open:

http://127.0.0.1:8000/docs

---

## Testing

The API has been manually tested using FastAPI Swagger UI.

Automated API testing using pytest is planned as a future improvement.

## 🐳 Docker

Dockerization is not currently implemented.

Docker and Docker Compose are planned as future improvements.

---

## 🔮 Future Improvements

- [ ] Automated API testing with pytest
- [ ] Dockerization
- [ ] Database migrations with Alembic
- [ ] Refresh tokens
- [ ] Password reset
- [ ] Email verification
- [ ] Pagination
- [ ] Search and filtering
- [ ] Deployment

---

## 👨‍💻 Author

**Avinash Kumar**

Python Backend Developer
