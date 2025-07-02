# 📘 Django Signals Assessment

This repository contains Python and Django code examples demonstrating the behavior of Django signals in three core areas: execution flow, thread handling, and database transaction safety.

---

## 🧪 Environment

- Python 3.x
- Django 3.x or 4.x
- Tested locally using Django shell and standalone test scripts

---

## ✅ Question 1: By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

> **Answer:** By default, Django signals are executed synchronously — meaning they block the main thread and execute immediately before the current function completes.
This means the main thread waits for the signal to complete before continuing.

### 🔬 Proof of Concept:
- Added a `time.sleep(5)` delay inside a `post_save` signal
- Measured execution time in a script using `time.time()`

### 📂 File:
- `test_signal_sync.py`

### ✅ Result:
```
Signal started
Signal finished
Time taken for create(): 5.02 seconds
```

➡️ **Conclusion:** 
•	The Book.objects.create() call waits until the signal finishes.
•	The time.sleep(5) in the signal handler blocks the execution.
•	This proves that Django signals are synchronous by default.


---

## ✅ Question 2: Do django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

> **Answer:** Yes, signals run in the **same thread** as the code that triggered them.

### 🔬 Proof of Concept:
- Used `threading.current_thread().name` in both:
  - Caller script
  - Signal handler

### 📂 File:
- `test_signal_thread.py`

### ✅ Result:
```
Caller running in thread: MainThread
Signal running in thread: MainThread
```

➡️ **Conclusion:** This shows both the calling code and the signal handler execute in the **same thread**.

---

## ✅ Question 3: By default do django signals run in the same database transaction as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

> **Answer:** Yes — Django signals run inside the same transaction by default.

### 🔬 Proof of Concept:
- Wrapped `Student.objects.create()` inside `transaction.atomic()`
- `post_save` signal attempted to create a note in a `Attendence_Sheet` model
- We then raised an exception to roll back the transaction.
- Checked if note was saved

### 📂 File:
- `test_signal_transaction.py`

### ✅ Result:
```
Transaction rolled back
Signal effect rolled back.(proof that signal shares transanction)
```

➡️ **Conclusion:** If the transaction is rolled back, signal effects are also rolled back → they share the same transaction


---

## 🗂️ Directory Structure

```
ASSESSMENT/
├── env/                            # Virtual environment (ignored via .gitignore)
├── django_assessment/             # Django project package (settings, urls, etc.)
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── test_1/                         # Django app for Question 1 (Signal sync test)
├── test_2/                         # Django app for Question 2 (Signal thread test)
├── test_3/                         # Django app for Question 3 (Signal transaction test)
├── db.sqlite3                      # SQLite database file
├── manage.py                       # Django's CLI utility
├── test_signal_sync.py            # Standalone test script for Question 1
├── test_signal_thread.py          # Standalone test script for Question 2
├── test_signal_transaction.py     # Standalone test script for Question 3
├── rectangle_task.py              # Custom iterable Rectangle class implementation
├── requirements.txt               # Python package dependencies
├── .gitignore                     # To exclude env/, __pycache__, etc.
└── README.md                      # Project overview and explanation



```

---



## 🚀 Run Locally

## 🛠️ Clone This Repository

```bash
git clone https://github.com/trish0912/django-task.git
cd django-task
```
1.Create virtual environment
```
python -m venv env

```
Activate virtual environment
On Windows:
```
env\Scripts\activate

```

On macOS/Linux:
```
source env/bin/activate

```

2. Install Django  
```
pip install -r requirements.txt

```
3. Run the test files from the project root:
```bash
python test_signal_sync.py
python test_signal_thread.py
python test_signal_transaction.py
```
Topic: Custom Classes in Python

Description: You are tasked with creating a Rectangle class with the following requirements:

An instance of the Rectangle class requires length:int and width:int to be initialized.
We can iterate over an instance of the Rectangle class 
When an instance of the Rectangle class is iterated over, we first get its length in the format: {'length': <VALUE_OF_LENGTH>} followed by the width {width: <VALUE_OF_WIDTH>}

## Rectangle Class Task

This task demonstrates use of Python OOP and custom iteration.

Create a Rectangle class with:

Two required attributes: length and width (both integers).

The class must be iterable.

When iterated, the object should yield:

{'length': <value>}

followed by {'width': <value>}

The class is defined in rectangle_task.py and includes:

__init__() to store the attributes.

__iter__() to enable iteration by yielding two dictionaries — one for length, one for width.

Results:
```
{'length': 10}
{'width': 5}
```

See: `rectangle_task.py`
