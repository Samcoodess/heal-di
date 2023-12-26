# Accounts Module

## Overview

The `accounts` module manages user accounts within the Healdi application. This module handles user registration, authentication, and profile management.

## Features
- **User Groups:** ✅
  - The system supports two main user groups:
    - Doctors
    - Patients
- **User Registration:**  ✅
  - New users can create accounts with a valid email address and password.

- **Authentication:** ✅
  - Secure user authentication process for access to Healdi features.
 
- **Profile Management:** ✅
  - Users can edit their profiles, including personal information and preferences.

- **Password Recovery:**
  - Users can recover their accounts by resetting passwords via email.

## Directory Structure

The `accounts` module follows a standard Django app directory structure:



## How to Use

### 1. Installation

```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
