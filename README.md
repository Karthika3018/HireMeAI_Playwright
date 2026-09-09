# HireMeAI Playwright Automation

## Project Overview

This project is a **UI test automation project** developed using **Python, Playwright, and Pytest**.

The project automates different web application scenarios such as login/logout, alerts, file upload/download, new tab handling, checkboxes, dropdowns, and search functionality.

The automation suite is integrated with **GitHub Actions** to execute tests automatically whenever changes are pushed to the `main` branch or a pull request is created.

## Tech Stack

* Python
* Playwright
* Pytest
* Git
* GitHub
* GitHub Actions
* HTML / Web UI Testing

## Automated Test Scenarios

### 1. Homepage Testing

* `test_homepage.py`
* Validates the homepage and expected page behavior.

### 2. Login & Logout Testing

* `test_loginlogout.py`
* Automates the login and logout flow.
* Validates expected elements after login/logout.

### 3. Alert Testing

* `test_alert.py`
* Automates JavaScript alert handling.

### 4. Confirmation Alert Testing

* `test_alertconfirm.py`
* Handles confirmation dialogs and validates the expected behavior.

### 5. Prompt Testing

* `test_prompt.py`
* Automates prompt dialog handling.

### 6. File Upload Testing

* `test_upload.py`
* Automates file upload functionality.

### 7. File Download Testing

* `test_download.py`
* Automates file download functionality.
* Validates the downloaded file name.

### 8. New Tab Testing

* `test_newtab.py`
* Automates opening and validating a new browser tab.

### 9. Checkbox Testing

* `test_w3checkbox.py`
* Automates checkbox selection and validation.

### 10. Dropdown Testing

* `test_w3dropdown.py`
* Automates dropdown selection and validation.

### 11. Search Testing

* `test_wksearch.py`
* Automates search functionality and validates the expected result.

## Project Structure

```text
HireMeAI_Playwright/
│
├── .github/
│   └── workflows/
│       └── playwright.yml
│
├── .gitignore
├── requirements.txt
├── test.txt
│
├── test_alert.py
├── test_alertconfirm.py
├── test_download.py
├── test_homepage.py
├── test_loginlogout.py
├── test_newtab.py
├── test_prompt.py
├── test_upload.py
├── test_w3checkbox.py
├── test_w3dropdown.py
└── test_wksearch.py
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Karthika3018/HireMeAI_Playwright.git
```

Navigate to the project directory:

```bash
cd HireMeAI_Playwright
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

## Running the Tests

Run the complete test suite:

```bash
pytest -v
```

Run an individual test:

```bash
pytest -v test_loginlogout.py
```

## GitHub Actions CI

This project uses **GitHub Actions for Continuous Integration (CI)**.

The workflow automatically:

1. Checks out the source code.
2. Sets up Python.
3. Installs project dependencies.
4. Installs the Playwright browser.
5. Executes the Pytest automation suite.

The workflow runs when:

* Code is pushed to the `main` branch.
* A pull request is created targeting the `main` branch.

## Test Execution Flow

```text
Write Automation Test
        ↓
Run Tests Locally
        ↓
Analyze Pass / Fail
        ↓
Fix Automation Issues
        ↓
Push Code to GitHub
        ↓
GitHub Actions CI
        ↓
Automated Test Execution
        ↓
Analyze CI Results
```

## Current Framework Scope

The current version focuses on:

* Playwright UI automation
* Pytest test execution
* Functional test automation
* Browser interaction
* Dialog/alert handling
* File upload/download
* New tab handling
* Form controls
* Git/GitHub version control
* GitHub Actions CI

## Future Enhancements

The framework can be further enhanced with:

* Page Object Model (POM)
* Pytest Fixtures
* Screenplay Pattern
* Data-Driven Testing
* API Automation
* Test Reporting
* Screenshot capture for failures
* Advanced CI/CD integration

## Author

**Karthika**

QA Automation | Python | Playwright | Pytest
