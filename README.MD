# Selenium with Python practice project

This project contains web automation practice using Python programming and Selenium WebDriver with Pytest.

## Test site for practice

https://practicetestautomation.com/practice-test-login/

## Test cases automated:

### Test case 1: Positive LogIn test

1. Open page
2. Type username student into Username field
3. Type password Password123 into Password field
4. Puch Submit button
5. Verify new page URL contains practicetestautomation.com/logged-in-successfully/
6. Verify new page contains expected text ('Congratulations' or 'successfully logged in')
7. Verify button Log out is displayed on the new page

### Test case 2: Negative username test

1. Open page
2. Type username incorrectUser into Username field
3. Type password Password123 into Password field
4. Puch Submit button
5. Verify error message is displayed
6. Verify error message text is Your username is invalid!

### Test case 3: Negative password test

1. Open page
2. Type username student into Username field
3. Type password incorrectPassword into Password field
4. Puch Submit button
5. Verify error message is displayed
6. Verify error message text is Your password is invalid!

To install dependencies please run pip install -r requirements.txt command