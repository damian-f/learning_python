#!/usr/bin/python

#this is a simple and non-secure password manager!

#dictionary to store passwords

PASSWORDS = {"EMAIL" : "password123",
			"BLOG": "password456",
			"APP" : "password789"}

import sys, pyperclip

if len(sys.argv) < 2:
    print("Password manager usage: python password_manager.py [account] --copies a password for a selected account")
    sys.exit()

account = sys.argv[1] #the first command line argument is the program name, the second is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("Password for ' + account + ' has been copied into the clipboard")
else:
    print("The provided account doesn't exist in the base")
