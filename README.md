# Task Overview
The HR management backend API is designed with FastAPI, utilizing asynchronous SQLAlchemy for database operations and an APIRouter-based modular structure. After a refactor for async compatibility and improved route grouping, the /employees/{employee_id} GET endpoint began returning HTTP 500 errors when the app is run in Docker. Logs indicate unhandled coroutines and serialization problems are preventing normal behavior.

# Guidance
- Focus on understanding FastAPI's async SQLAlchemy usage and response serialization patterns.
- Pay special attention to how database coroutines are awaited and how ORM objects are returned from endpoints.
- Check that response serialization with Pydantic models is strictly followed.
- Limit your changes to the problematic endpoint only, updating supporting code only if needed to ensure correct async and serialization behavior.

# Objectives
- Diagnose the root cause causing HTTP 500 errors and traceback messages mentioning async coroutine or serialization issues.
- Update the /employees/{employee_id} endpoint so it properly awaits DB access and serializes output using Pydantic models.
- Ensure that requesting /employees/{employee_id} returns HTTP 200 and a valid JSON response with the expected employee data.
- Avoid making unnecessary changes outside of resolving the issue at hand.

# How to Verify
- Start the full environment using the provided scripts and Docker setup.
- Query the /employees/{employee_id} endpoint for an employee present in the database.
- Confirm the response returns HTTP 200 with correct JSON data, and that logs do not show coroutine or JSON serialization errors for this endpoint.