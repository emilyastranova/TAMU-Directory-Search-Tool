# TAMU Directory Search Tool

This tool allows a user to lookup a student or staff member in the TAMU Directory through the terminal. If results are found, it can also search those results for a specific email (or a portion of an email). Due to TAMU's query logic, you cannot just search by email, there must be a list of users retrieved by name first

## Installation

Install the required Python 3 libraries

```bash
pip3 install -r requirements.txt
```

## Usage

Terminal argument usage:

```bash
python3 search.py john doe
```

Interactive usage:

```bash
python3 search.py
```

This will give you the following prompt:

```lang-none
Enter search term: john doe
```

Output:

```lang-none
1 results found
Checking for emails...

Name: Doe, John
Email: johndoe@tamu.edu
Link: https://directory.tamu.edu/people/XXXXXXXX/?branch=people&cn=john+doe
```

If results are found, there will be a prompt to filter down by email address:

```lang-none
Search results for a specific email? (y/N):
```

Selecting "y" will prompt for an email and display only the results containing that text in the email address

## Contributing

This project uses the GPLv3 license.
I'm sure this could use some work, feel free to change it

## Credit

Original author: [Tyler Harrison](https://github.com/tyleraharrison)
