# AI Coding Agent Guidelines & Core Rules

## 1. Code Quality & Standards
- Write clean, modular, and secure code.
- Always include explicit type hints and documentation strings for core functions.
- Avoid hardcoding sensitive credentials; strictly rely on environment variables (`.env` or GitHub Secrets).

## 2. Error Handling & Testing
- Every automated patch or utility script must include exception handling (`try-except`) with descriptive failure logs.
- Never output destructive code commands or alter critical system files outside the designated workspace sandbox.

## 3. Git Operations Protocol
- Maintain clear and standardized commit messages following conventional formats (e.g., `feat:`, `fix:`, `refactor:`).
- Automatically verify code syntax locally before pushing branches or triggering pull requests.
