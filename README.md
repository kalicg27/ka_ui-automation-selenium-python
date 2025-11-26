# UI Automation Framework (Python + Selenium + POM)

This repository contains a scalable UI automation framework built with **Python**, **Selenium WebDriver**, **Pytest**, and the **Page Object Model (POM)** design pattern.

It is part of my QA / Technical Software Test Engineer portfolio and demonstrates how I structure maintainable, production-ready UI tests.

---

## Tech Stack

- Python
- Selenium WebDriver
- Pytest
- Pytest-HTML (HTML reporting)
- WebDriver Manager
- YAML-based configuration
- GitHub Actions (CI)

---

## Application Under Test

The framework automates tests against the public demo application:

- `https://www.saucedemo.com/`

Main flows covered:

- Login (valid / invalid / locked-out user)
- Adding items to cart
- Removing items from cart
- Full checkout flow (end-to-end)

---

## Architecture

```text
config/         # YAML configuration (base URL, browser, timeouts)
core/           # Driver factory & config loader
pages/          # Page Object Model classes
tests/          # Pytest test suites
utils/          # Common utilities (waits, helpers)
.github/        # CI pipeline (GitHub Actions)
