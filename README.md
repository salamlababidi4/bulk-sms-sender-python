# Bulk SMS Sender in Python
This Python project simulates a simple bulk SMS sending system using predefined customer data. It includes functions to retrieve phone numbers, send individual messages, and handle bulk messaging while managing errors gracefully.

### Features
1. **Phone Number Retrieval**: `get_phone_number(person)` fetches the phone number of a specified customer from a predefined list.
2. **Send SMS**: `send_sms(number)` sends a simulated SMS message and confirms the action.
3. **Bulk SMS Sending**: `send_bulk_sms(names)` sends messages to a list of customers, handling errors for customers not in the database.

### Purpose
This project showcases:
- Error handling using `try` and `except` blocks.
- Working with lists and indexes.
- Implementing reusable functions for modular code.

### Example Usage
Input a list of names, and the program will send messages to customers found in the database while notifying if any names are missing.
