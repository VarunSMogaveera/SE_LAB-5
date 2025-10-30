1. Which issues were the easiest to fix, and which were the hardest? Why?
The easiest issues to fix were formatting-related ones like renaming functions to snake_case, adding missing docstrings, and removing unused imports.
The hardest ones were handling the bare except statement, correcting the mutable default argument (logs=[] → None), and implementing the “Load or Reset” feature to fix the persistent data issue, since they required structural code changes.
________________________________________
2. Did the static analysis tools report any false positives? If so, describe one example.
Yes. Pylint reported the use of the global variable stock_data as a warning (W0603), but in this small, single-file program, it was necessary and did not cause any functional issue. Therefore, it can be considered a false positive in this context.
________________________________________
3. How would you integrate static analysis tools into your actual software development workflow?
I would integrate tools like pylint, flake8, and bandit both locally and in CI/CD pipelines.
•	Locally: Configure pre-commit hooks to automatically run static analysis before each commit.
•	In CI/CD: Use GitHub Actions to run these tools on every push or pull request, preventing code with security or style violations from being merged.
________________________________________
4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?
After applying fixes, the pylint score improved from 4.8/10 to 9.7/10, and Bandit reported no security vulnerabilities.
The code became more readable and maintainable through consistent naming, docstrings, and safe file handling.
Validation and error handling made it more robust, and removing eval() eliminated a major security risk.
The “Load or Reset” option also improved usability and made test runs consistent.
