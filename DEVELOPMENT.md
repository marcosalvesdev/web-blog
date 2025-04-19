# 🛠️ Development Guide

Welcome, developer! This guide will help you set up the project locally using [Poetry](https://python-poetry.org/), the dependency management and packaging tool for Python.

## 📆 Requirements

Before you start, make sure you have the following installed:

- Python 3.10+ (check with `python --version`)
- [Poetry](https://python-poetry.org/docs/#installation)

You can install Poetry by running:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

## 🚀 Getting Started

1. **Clone the repository**

```bash
git clone git@github.com:marcosalvesdev/web-blog.git
cd your-django-blog
```

2. **Install dependencies**

```bash
poetry install
```

3. **Activate the virtual environment**

```bash
poetry shell
```

4. **Apply migrations**

```bash
python manage.py migrate
```

5. **Create a superuser (optional, for admin access)**

```bash
python manage.py createsuperuser
```

6. **Run the development server**

```bash
python manage.py runserver
```

The blog will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🧪 Running Tests

To run tests, use:

```bash
python manage.py test
```

---

## 📝 Useful Commands

- Collect static files: `python manage.py collectstatic`
- Make migrations: `python manage.py makemigrations`
- Access the admin panel: `http://127.0.0.1:8000/admin/`

---

## 🙋 Need Help?

Feel free to open an issue if you run into any trouble. Contributions are welcome!

---

Happy coding! 💻✨