
# 🗳️ Online Voting System

A secure and user-friendly web app where users can register, vote, and view real-time election results using charts.

> 🔗 [Live on GitHub](https://github.com/Abhi-Rewale/online-voting-system)

---

## 📌 Features

- ✅ Login & Register using email
- ✅ Admin creates elections and candidates
- ✅ Voters can vote only once per election
- ✅ Live results with interactive chart
- ✅ Admin can view results from admin panel
- ✅ Users can see their vote history
- ✅ Beautiful Bootstrap UI with image support

---

## 🧑‍💻 Technologies Used

- **Python** + **Django**
- **MySQL**
- **Bootstrap 5**
- **Chart.js** (for visual results)

---

## 📸 Screenshots

> *(Add screenshots in your GitHub repo later: login, vote page, chart view, admin panel)*

---

## 🛠️ Setup Instructions

### 🔧 Prerequisites

- Python 3.x
- MySQL
- Git (optional but recommended)

---

### ⚙️ Installation Steps

1. **Clone the repo:**

```bash
git clone https://github.com/Abhi-Rewale/online-voting-system.git
cd online-voting-system
```

2. **Create virtual environment:**

```bash
python -m venv env
env\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Setup MySQL database:**

Create a MySQL database, then update `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'voting_db',
        'USER': 'root',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

5. **Apply migrations and create superuser:**

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

6. **Run the development server:**

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/`

---

## 👨‍⚖️ Admin Credentials

- Log in at `/admin/` to manage elections, candidates, and view results.

---

## 📂 Folder Structure

```
├── accounts/
├── election/
├── templates/
│   ├── accounts/
│   └── election/
├── static/
├── media/
├── manage.py
├── README.md
```

---

## 🙋‍♂️ Author

**Abhishek Rewale**  
GitHub: [@Abhi-Rewale](https://github.com/Abhi-Rewale)
