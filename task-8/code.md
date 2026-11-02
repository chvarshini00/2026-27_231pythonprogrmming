# Password Policy Validation Engine

## 1. Problem Statement

Develop a Python program to validate passwords based on a set of security policies. The program should evaluate multiple sample password strings against minimum length, character-category, repetition, and prohibited-substring rules.

The program must perform the following operations:

1. Check whether the password satisfies the minimum length requirement of 8 characters.
2. Verify that the password contains at least:
   - One uppercase letter.
   - One lowercase letter.
   - One digit.
   - One special character.
3. Check whether the password contains consecutive repeated characters.
4. Check whether the password contains prohibited substrings such as `password`, `admin`, and `123456`.
5. Display whether each password is valid or invalid.
6. Explain every failed validation condition.
7. Process multiple passwords and display their validation results.

## 2. Algorithm

1. Start the program.
2. Define the minimum password length as 8.
3. Define the prohibited substrings:
   - password
   - admin
   - 123456
4. Read the number of passwords to validate.
5. Repeat for each password:
   - Read the password.
   - Initialize an empty list to store errors.
6. Check whether the password length is at least 8.
7. Check whether it contains an uppercase letter.
8. Check whether it contains a lowercase letter.
9. Check whether it contains a digit.
10. Check whether it contains a special character.
11. Check whether it contains consecutive repeated characters.
12. Check whether it contains any prohibited substring (case-insensitive).
13. Add an appropriate error message for every failed condition.
14. If the error list is empty, display VALID PASSWORD.
15. Otherwise, display INVALID PASSWORD and all failure reasons.
16. Repeat until all passwords are processed.
17. Stop the program.


## 5. Sample Input

```
======= PASSWORD POLICY VALIDATION ENGINE =======

Enter number of passwords to validate: 4

Enter Password 1:
Abc@1234

Enter Password 2:
abc123

Enter Password 3:
Admin@1234

Enter Password 4:
Strong@Pass9
```

## 6. Sample Output

```
======= PASSWORD POLICY VALIDATION ENGINE =======

Password 1: Abc@1234

Password Validation Result:
VALID PASSWORD
All security rules are satisfied.

---------------------------------------------

Password 2: abc123

Password Validation Result:
INVALID PASSWORD

Failed Conditions:
- Password must contain at least 8 characters.
- Password must contain at least one uppercase letter.
- Password must contain at least one special character.

---------------------------------------------

Password 3: Admin@1234

Password Validation Result:
INVALID PASSWORD

Failed Conditions:
- Password contains prohibited substring: admin

---------------------------------------------

Password 4: Strong@Pass9

Password Validation Result:
VALID PASSWORD
All security rules are satisfied.

---------------------------------------------

Password validation completed.
```

## 7. Explanation of Validation Rules

| Validation rule      | Condition                           | Failure message            |
| -------------------- | ----------------------------------- | -------------------------- |
| Minimum length       | At least 8 characters               | Password is too short      |
| Uppercase            | At least one A–Z letter             | Uppercase letter missing   |
| Lowercase            | At least one a–z letter             | Lowercase letter missing   |
| Digit                | At least one number                 | Digit missing              |
| Special character    | At least one symbol                 | Special character missing  |
| Repetition           | No consecutive identical characters | Repeated characters found  |
| Prohibited substring | Must not contain restricted words   | Prohibited substring found |

Example:

For the password `Admin@1234`:

- Length requirement: Passed.
- Uppercase requirement: Passed.
- Lowercase requirement: Passed.
- Digit requirement: Passed.
- Special character requirement: Passed.
- Repetition requirement: Passed.
- Prohibited substring requirement: Failed because it contains `admin`.

Therefore, the password is invalid.

## 8. Mermaid Flowchart Code
``` mermaid

flowchart TD
    A([Start]) --> B[Define password policy rules]
    B --> C[/Enter number of passwords/]
    C --> D[/Enter password/]
    D --> E[Initialize error list]

    E --> F{Length at least 8?}
    F -- No --> G[Add minimum length error]
    F -- Yes --> H{Contains uppercase?}
    G --> H

    H -- No --> I[Add uppercase error]
    H -- Yes --> J{Contains lowercase?}
    I --> J

    J -- No --> K[Add lowercase error]
    J -- Yes --> L{Contains digit?}
    K --> L

    L -- No --> M[Add digit error]
    L -- Yes --> N{Contains special character?}
    M --> N

    N -- No --> O[Add special character error]
    N -- Yes --> P{Contains consecutive repeated characters?}
    O --> P

    P -- Yes --> Q[Add repetition error]
    P -- No --> R{Contains prohibited substring?}
    Q --> R

    R -- Yes --> S[Add prohibited substring error]
    R -- No --> T{Error list empty?}
    S --> T

    T -- Yes --> U[Display VALID PASSWORD]
    T -- No --> V[Display INVALID PASSWORD and failure reasons]

    U --> W{More passwords?}
    V --> W

    W -- Yes --> D
    W -- No --> X[Display completion message]
    X --> Y([Stop])
mermaid



```


## 9. Result

The Python program successfully validates multiple passwords against minimum length, uppercase, lowercase, digit, special character, consecutive repetition, and prohibited-substring rules. It displays whether each password is valid or invalid and explains all the failed conditions.

