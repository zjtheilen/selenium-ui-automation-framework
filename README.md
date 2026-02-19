# Selenium UI Automation Framework

A lightweight Selenium automation framework using **pytest** to test [`the-internet.herokuapp.com`](https://the-internet.herokuapp.com/) sample pages. Includes basic helpers, page objects, and cross-page test examples.

---

## Table of Contents

- [Project Structure](#project-structure)  
- [Setup](#setup)  
- [Running Tests](#running-tests)  
- [Helpers](#helpers)  
- [Page Objects](#page-objects)  
- [Future Improvements](#future-improvements)  

---

## Project Structure

```bash
.
├── conftest.py                  # Pytest fixtures (browser setup/teardown)
├── utils/
│   └── driver_factory.py        # Driver creation and page load helpers
├── tests/
│   ├── helpers.py               # Common actions (login, toggle_checkbox, wait helpers)
│   ├── pages/
│   │   ├── base_page.py         # BasePage class with wait utilities
│   │   ├── checkboxes_page.py   # Checkboxes page object
│   │   └── login_page.py        # Login page object
│   ├── test_checkboxes.py       # Checkbox tests
│   ├── test_homepage.py         # Homepage test
│   └── test_login.py            # Login test
└── README.md
```

---

## Setup

```bash
# Clone the repository
git clone https://github.com/zjtheilen/selenium-ui-automation-framework.git
cd selenium-ui-automation-framework

# Create a virtual environment (optional but recommended)
python -m venv testenv
source testenv/Scripts/activate  # Windows
# or
source testenv/bin/activate      # macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

---

## Running Tests

```bash
# Run all tests
pytest

# Run a specific test
pytest tests/test_login.py

# Use verbose mode for more output
pytest -v
```

---

## Helpers

```python
# login(driver, username, password)
#   Logs into the login page and waits for Secure Area

# toggle_checkbox(driver, index)
#   Toggles a checkbox by index and returns its current state

# wait_for_element(driver, locator)
#   Waits until an element is present

# wait_for_clickable(driver, locator)
#   Waits until an element is clickable
```

---

## Page Objects

Implemented using **Page Object Model (POM) principles**:

```python
# BasePage – Provides wait_for_element and wait_for_clickable
# LoginPage – Encapsulates login page actions (load(), login())
# CheckboxesPage – Encapsulates checkbox page actions (load(), toggle_checkbox())
```

Will extend this pattern for other pages to keep tests clean and maintainable.

---

## Future Improvements

```bash
# Add README badges (pytest, coverage, Python version)
# Implement full POM for all pages
# Add configuration file for URLs, credentials, and timeouts
# Integrate CI/CD (GitHub Actions) for automated test runs
# Add screenshots on test failure and HTML reports
```
