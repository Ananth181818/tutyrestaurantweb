# Tuty Restaurant - Premium Web Application

Welcome to **Tuty Restaurant**, a modern, premium Django-based web application designed for a luxury dining experience, party hall booking, and room reservation services located in Tuticorin (Tuty). 

The application is built with a highly aesthetic responsive UI, utilizing glassmorphism, custom gradients, dynamic CSS micro-animations, and a secure AJAX-driven user authentication system that saves registered users' profiles directly to the database.

---

## 🌟 Key Features

* **Secure Authentication System**: Real AJAX-based login, registration, and logout forms. Authenticated users are saved to the Django database and managed using a custom `UserProfile` database model.
* **Room Booking & Management**: Complete room reservation module supporting Standard, Couple (AC/Non-AC), and Family (AC/Non-AC) rooms. Bookings are stored in the database with automated check-in/check-out date validation.
* **Interactive Digital Menus**: Responsive partial views for exploring Vegetarian and Non-Vegetarian menus.
* **Premium Glassmorphic UI**: High-end styling with an immersive dark theme, responsive navigation dropdowns, hover effects, and slide-in notifications.
* **Django Admin Panel Integration**: Full admin controls to view, search, and manage room bookings and user profile entries.

---

## 🛠️ Technology Stack

* **Backend**: Django 6.0+ (Python)
* **Database**: SQLite (default, easily portable to PostgreSQL/MySQL)
* **Frontend**: HTML5, Vanilla CSS3 (Custom design tokens & responsive layouts), JavaScript (jQuery 3.7.1)
* **Authentication**: Django's default authentication framework integrated with a custom database profile extension (`UserProfile`).

---

## 📂 Project Structure

```text
├── manage.py                   # Django CLI utility
├── db.sqlite3                  # Local SQLite database
├── myenv/                      # Python virtual environment
├── static/                     # Global static assets (CSS, JS, images)
├── templates/                  # Global HTML templates (index, orders, roombook, etc.)
├── tuty_restaurant/            # Main project configuration settings & URLs
└── restaurant/                 # Django App directory
    ├── admin.py                # Admin site registration for models
    ├── models.py               # Database schemas (RoomBooking, UserProfile)
    ├── urls.py                 # App routing paths & API endpoints
    └── views.py                # Business logic for rendering & authentication APIs
```

---

## 🚀 Setup and Installation

Follow these instructions to run the application locally:

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/tutyrestaurantweb.git
cd tutyrestaurantweb
```

### 2. Set Up Virtual Environment
Ensure Python 3.10+ is installed:
```bash
# Create environment
python -m venv myenv

# Activate on Windows
.\myenv\Scripts\activate

# Activate on macOS/Linux
source myenv/bin/activate
```

### 3. Install Django
```bash
pip install django
```

### 4. Run Migrations
Generate and apply the database tables (this will set up authentication tables, room bookings, and user profiles):
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Admin Superuser
To access the Django admin portal, create a superuser account:
```bash
python manage.py createsuperuser
```

### 6. Run the Server
Start Django's local development server:
```bash
python manage.py runserver
```
Open your browser and navigate to `http://127.0.0.1:8000/`.

---

## 🔒 Database Models

The system defines the following key data structures in `restaurant/models.py`:

### 1. `UserProfile`
Extends the default Django `User` model to link authentication accounts with custom profile details.
* `user`: `OneToOneField` linking to the standard Django `User` auth model.
* `full_name`: `CharField` storing the user's full name.
* `email`: `EmailField` (unique) storing the email address.
* `created_at`: `DateTimeField` tracking registration time.

### 2. `RoomBooking`
Stores guest reservation information.
* `guest_name`: Name of the booking guest.
* `guest_phone`: Contact phone number.
* `room_type`: Selected room classification (e.g., Couple Room AC, Family Room Non-AC).
* `price`: Room rate per day.
* `check_in` & `check_out`: Selected dates.
* `booked_at`: Automated booking timestamp.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to open an issue or submit a pull request on the repository.
