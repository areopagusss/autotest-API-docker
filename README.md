<<<<<<< HEAD
# Autotest-API-Docker

<p align="center">
  <img src=".images/bees_for_git.png" alt="Telegram Admin Bot Logo">
</p>

## About
This project is a set of automated tests to verify the functionality of API endpoints. The tests are implemented in Python using the requests library for interacting with the API and the pytest framework for organizing and running autotests.
## Install and Run
**1. Create and activate a virtual environment:**
   
   - python3 -m venv env  # Linux  macOS
   - python -m venv venv  # Windows


   - source env/bin/activate  # Linux  macOS
   - source venv/Scripts/activate  # Windows
   
**2. Install dependencies from a file requirements.txt:**
   - python3 -m pip install --upgrade pip
   - pip install -r requirements.txt

**3. To run all autotests, run the following command:**
   
   - pytest
   

## API Description
The API that autotests interact with is located at the following URL: https://jsonplaceholder.typicode.com /. The following API methods are being tested as part of the project:

Each of these methods can accept userId, id, title, and body parameters.
- **GET /posts:** Getting a list of posts.
- **POST /posts:** Creating a new post.
- **DELETE /posts/{id}:** Delete a post by ID.

---
This test works great and performs all its functions.
=======
"# Autotest-API-Docker" 
>>>>>>> origin/main