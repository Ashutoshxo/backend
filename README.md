# 🧠 Django REST Backend — Todo App

This is the **backend** of a full-stack Todo Application built with **Django** and **Django REST Framework (DRF)**.  
It provides secure REST APIs used by the **Flutter frontend** for all CRUD operations.

---

## 🚀 Tech Stack
- **Python 3.x**
- **Django 5.x**
- **Django REST Framework (DRF)**
- **SQLite / MySQL** (easily switchable)
- **CORS Headers** for Flutter connection

---

## 🧩 Features
✅ RESTful APIs for all CRUD operations  
✅ Create, Read, Update, Delete todos  
✅ Filter todos by status (All / Pending / Done)  
✅ JSON responses optimized for Flutter app  
✅ Django admin panel for managing data  
✅ Ready for JWT or token authentication  
✅ CORS enabled for mobile frontend access  



---

## 🧠 API Endpoints

| Method | Endpoint               | Description               |
|--------|------------------------|---------------------------|
| GET    | `/api/todos/`          | Get all todos             |
| POST   | `/api/todos/`          | Create a new todo         |
| GET    | `/api/todos/<id>/`     | Get single todo details   |
| PUT    | `/api/todos/<id>/`     | Update a todo             |
| DELETE | `/api/todos/<id>/`     | Delete a todo             |

Example request:
```bash
POST /api/todos/
{
  "title": "Buy groceries",
  "description": "Milk, Bread, Eggs",
  "due_date": "2025-11-05",
  "completed": false
🔗 Flutter Frontend

The frontend for this project is built with Flutter.
Check it out here: https://github.com/Ashutoshxo/frontend

## 🗂️ Project Structure
