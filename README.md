# 🛒 PhiMart – eCommerce API

PhiMart is a fully functional eCommerce REST API built with Django and Django REST Framework (DRF). It provides endpoints for managing products, categories, orders, carts, and users, and supports secure authentication using JWT with **Djoser**. A Swagger UI is also integrated for API documentation using **drf\_yasg**.

---

## 🚀 Features

* 🔐 **JWT Authentication** using Djoser
* 📦 **Product Management** (CRUD)
* 🗂️ **Category Management**
* 🛍️ **Shopping Cart System**
* 📑 **Order Placement & History**
* 👤 **User Registration & Profile**
* 📘 **Swagger Documentation** with drf\_yasg

---

## 🛠️ Tech Stack

* **Python 3**
* **Django 4+**
* **Django REST Framework**
* **Djoser** – JWT Auth
* **drf\_yasg** – Swagger/OpenAPI docs
* **PostgreSQL** – Database
* **SimpleJWT** – Token-based authentication

---

## 📂 Project Structure

```
PHIMART/
├── manage.py
├── phimart/               # Project settings
│   └── settings.py
├── api/                   # Core app with views, models, serializers, urls
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
├── requirements.txt
├── README.md
```

---

## 📦 Installation

1. **Clone the repo**

   ```bash
   git clone https://github.com/yourusername/phimart.git
   cd phimart
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**

   ```bash
   python manage.py runserver
   ```

---

## 🔐 Authentication

JWT authentication is handled using **Djoser**. Key endpoints include:

* `POST /auth/jwt/create/` – Obtain access and refresh tokens
* `POST /auth/jwt/refresh/` – Refresh token
* `POST /auth/jwt/verify/` – Verify token
* `POST /auth/users/` – Register new user
* `GET /auth/users/me/` – Get current user

---

## 🔗 API Endpoints Overview

| Resource   | Endpoint           | Methods                |
| ---------- | ------------------ | ---------------------- |
| Products   | `/api/v1/products/`   | GET, POST, PUT, DELETE |
| Categories | `/api/v1/categories/` | GET, POST, PUT, DELETE |
| Carts      | `/api/v1/carts/`      | GET, POST, DELETE      |
| Orders     | `/api/v1/orders/`     | GET, POST              |
| Users/Auth | `/auth/`              | JWT Login, Register    |

---

## 📘 API Docs

Swagger UI is available at:

```
http://localhost:8000/swagger/
```

Redoc UI is also available:

```
http://localhost:8000/redoc/
```

---

## ✅ Todo / Future Enhancements

* [ ] Payment Integration (e.g. Stripe/SSLCommerz)
* [ ] Email Verification
* [ ] Admin Dashboard

---

## 🧑‍💻 Author

**Md Mehedi Hasan**
Bangladeshi software developer & web enthusiast
📧 [mdmehedihasanroby@gmail.com](mailto:mdmehedihasanroby@gmail.com)
📍 Currently in Malaysia

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
