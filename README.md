
# Task Manager

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Django](https://img.shields.io/badge/Django-5.2.5-green)


A simple, user-friendly web application to manage tasks with full **CRUD functionality**, user authentication, and a clean interface built with **Django** and **Bootstrap**.



## Features or Apps as they call it in Django😅

- **User Authentication:** Login, logout, and signup functionality.  
- **Task Management (CRUD):** Create, read, update, and delete tasks.  
- **Task Ownership:** Each user can only see and manage their own tasks.  
- **Task Completion:** Mark tasks as completed or pending.  
- **Alerts & Feedback:** Success messages for task creation, updates, and deletion.  
- **Sorting & Filtering:** Sort tasks by due date and filter completed/pending tasks.  
- **Responsive UI:** Built with Bootstrap for mobile-friendly design.



## Screenshots

*(Add screenshots or GIFs of your app here to showcase it visually)*



## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/task-manager.git
cd task-manager
````

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the environment:

* **Windows:** `venv\Scripts\activate`
* **Mac/Linux:** `source venv/bin/activate`

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Apply migrations:

```bash
python manage.py migrate
```

6. Run the development server:

```bash
python manage.py runserver
```

7. Visit `http://127.0.0.1:8000/` in your browser.



## Tech Stack

* **Backend:** Django
* **Frontend:** Bootstrap 5, HTML, CSS
* **Database:** SQLite (default, can switch to PostgreSQL)
* **Version Control:** Git & GitHub



## Future Improvements

* Add **due date picker** and deadline reminders.
* Implement **search and filter** functionality.
* Polish UI with **better styling** and animations.
* Deploy online to show a **live demo**.



## License

MIT License.


