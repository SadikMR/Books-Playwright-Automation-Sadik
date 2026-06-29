# Playwright Automation Framework – Books to Scrape

## Project Overview

This project is a UI automation framework built with **Playwright** and **Pytest** to test the functionality of the **Books to Scrape** website.

The framework follows the **Page Object Model (POM)** design pattern to keep the code modular, reusable, and easy to maintain. It covers functional UI testing, data consistency validation, broken link detection, product image validation, reporting, and CI/CD integration using GitHub Actions.

**Target Website:**
https://books.toscrape.com/

---

# Features

* Page Object Model (POM) architecture
* Reusable page classes and utility methods
* Homepage validation
* Book navigation validation
* Book data consistency validation
* Broken link verification
* Product image validation across multiple pages
* Random category and book selection
* Centralized selectors
* Custom logging
* HTML report generation
* Allure result generation
* GitHub Actions CI/CD pipeline
* Screenshot, video, and trace collection on test failure

---

# Tech Stack

* Python 3.12
* Playwright
* Pytest
* pytest-playwright
* pytest-html
* allure-pytest
* Requests
* GitHub Actions

---

# Installation Guide

Clone the repository.

```bash
git clone https://github.com/SadikMR/Books-Playwright-Automation-Sadik.git
cd Books-Playwright-Automation-Sadik
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate it.

**Linux / macOS**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

Install the required packages.

```bash
pip install -r requirements.txt
```

Install Playwright browsers.

```bash
playwright install
```

---

# Environment Setup

Requirements:

* Python 3.12 or later
* Git
* Playwright
* Chromium browser

For Allure HTML reports, install:

* Java Runtime Environment (JRE)
* Allure Command Line

---

## Running Tests

Run the complete test suite.

```bash
pytest
```

Run individual test cases.

### Test Case 1 – Homepage Validation

```bash
pytest tests/test_homepage.py
```

### Test Case 2 – Book Navigation Validation

```bash
pytest tests/test_book_details.py
```

### Test Case 3 – Book Data Consistency Validation

```bash
pytest tests/test_book_consistency.py
```

### Test Case 4 – Broken Link Validation

```bash
pytest tests/test_broken_links.py
```

### Test Case 5 – Product Image Validation

```bash
pytest tests/test_product_images.py
```

Run smoke tests.

```bash
pytest -m smoke
```

Run regression tests.

```bash
pytest -m regression
```

### Running in Headed Mode

The framework runs in **headless mode** by default for CI compatibility.

If you'd like to watch the browser while tests are running, execute:

```bash
pytest --headed
```

To slow down browser actions for easier observation:

```bash
pytest --headed --slowmo=300
```

---

# Project Structure

```text
books-playwright-automation-sadik/
│
├── .github/
│   └── workflows/
│       └── playwright.yml
│
├── pages/
│   ├── base_page.py
│   ├── home_page.py
│   ├── category_page.py
│   └── book_page.py
│
├── tests/
│   ├── test_homepage.py
│   ├── test_book_details.py
│   ├── test_book_consistency.py
│   ├── test_broken_links.py
│   └── test_product_images.py
│
├── utils/
│   ├── constants.py
│   ├── helper.py
│   ├── logger.py
│   ├── navigation.py
│   └── selectors.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

# Test Case Coverage

## Test Case 1 – Homepage Validation

* Verify homepage URL
* Verify page title
* Verify page heading
* Verify Books section
* Verify homepage loads successfully

---

## Test Case 2 – Book Navigation Validation

* Randomly select five categories
* Randomly select five books from each category
* Open each book
* Verify the details page loads
* Verify the H1 title matches the selected book
* Verify book information is displayed

---

## Test Case 3 – Book Data Consistency Validation

* Capture homepage title
* Capture homepage price
* Open the book details page
* Compare homepage and details page titles
* Compare homepage and details page prices

---

## Test Case 4 – Broken Link Validation

* Collect all hyperlinks
* Remove duplicate URLs
* Send HTTP requests
* Verify every URL returns HTTP 200

---

## Test Case 5 – Product Image Validation

* Verify images are visible
* Verify `src` attribute
* Verify `alt` attribute
* Verify image class contains `thumbnail`
* Validate images across multiple pages

---

# Report Generation Guide

## HTML Report

Generate an HTML report after running the tests.

```bash
pytest --html=report.html --self-contained-html
```

Open the generated report in any web browser.

---

## Allure Report

Generate Allure results.

```bash
pytest --alluredir=allure-results
```

Generate the HTML report.

```bash
allure generate allure-results --clean -o allure-report
```

Serve the report locally.

```bash
allure serve allure-results
```

> **Note:** Generating the Allure HTML report locally requires Java and the Allure Command Line to be installed. Even without these tools installed locally, the GitHub Actions workflow can still generate and upload Allure artifacts.

---

# GitHub Actions Setup

A GitHub Actions workflow is included at:

```text
.github/workflows/playwright.yml
```

The workflow automatically:

* Checks out the repository
* Installs Python dependencies
* Installs Playwright browsers
* Runs all tests
* Generates the HTML report
* Generates Allure results
* Builds the Allure HTML report
* Uploads execution artifacts

Uploaded artifacts include:

* HTML Report
* Allure Results
* Allure Report
* Playwright artifacts (screenshots, videos, and traces when available)

---

# Design Decisions

A few design choices were made to keep the framework simple and maintainable:

* Used the **Page Object Model (POM)** to separate page logic from test logic.
* Centralized selectors to make updates easier if the UI changes.
* Created a reusable `BasePage` to avoid duplicated Playwright actions.
* Added helper utilities for shared navigation and random selection.
* Used Playwright's built-in assertions instead of explicit waits whenever possible.
* Added logging to make test execution easier to follow and debug.
* Organized tests so each scenario focuses on a single responsibility.

---

# Known Limitations

* Category and book selection is randomized, so different executions may test different books.
* Internet access is required to run the tests.
* Allure HTML reports require Java and the Allure Command Line.
* Screenshots, videos, and traces are only generated when a test fails, based on the current Playwright configuration.

---
