# app.py Sections Overview

This document provides a breakdown of the main sections and functions in `app.py` with their approximate line numbers to facilitate easier navigation and review.

| Section / Function Name           | Description                                      | Line Numbers |
|---------------------------------|--------------------------------------------------|--------------|
| Imports                         | All import statements                            | 1 - 40       |
| Flask App Initialization        | Flask app, DB, Mail, LoginManager setup          | 41 - 80      |
| Data Loading & Saving Functions | Functions to load and save calculation data      | 81 - 105     |
| Weighted Score Mapping Tables   | Data structures for score mappings                | 106 - 162    |
| Score Mapping Functions         | Functions like `map_raw_to_weighted_score`        | 163 - 239    |
| Frequency Calculation Functions | Functions for frequency score calculations        | 240 - 346    |
| User Model                     | SQLAlchemy User model class                        | 347 - 391    |
| Admin Decorator                | `admin_required` decorator function                | 392 - 405    |
| User Loader                   | Flask-Login user loader function                   | 406 - 418    |
| Routes: Landing, Logout       | Landing page and logout routes                      | 419 - 440    |
| User Registration & Login    | Registration and login routes and forms            | 441 - 570    |
| Password Reset               | Password reset request and token routes            | 571 - 590    |
| Intro & Dashboard            | Intro page and user dashboard routes               | 591 - 610    |
| Admin Dashboard             | Admin dashboard route                               | 611 - 630    |
| Profile Editing             | Edit profile (change password) route and form      | 631 - 655    |
| Start & Restart             | Start questionnaire and restart session routes     | 656 - 681    |
| Module Pages (GET & POST)   | Routes for module pages GET and POST                | 682 - 977    |
| Calculation Logic           | Calculation route and related functions             | 978 - 1098   |
| Result Page                | Result display route                                | 1099 - 1133  |
| PDF Generation             | PDF generation route and logic                      | 1134 - 1677 |
| Error Handlers             | 404 and 500 error handlers                          | 1678 - 1684 |
| Admin User Setup           | Admin user environment variable setup              | 1685 - End   |

This overview should help quickly locate and review specific parts of the `app.py` file without needing to scroll through the entire file.