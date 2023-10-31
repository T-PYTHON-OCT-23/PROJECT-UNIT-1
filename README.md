# PROJECT-UNIT-1


## Based on what you’ve learned until now , create a project of your choosing (impress us with your imagination) . This project must at least satisfy the following minimum requirements :

- Must be interactive on CLI.
- Use lists or dictionaries or tuples. 
- Use loops.
- Use functions that return an output . 
- Use a Lambda function.
- Use at least 1 Class.
- Use some form of Error Handling .
- Organize Your Code into modules & (or packages)

# Property Management System

This project is a Property Management System that allows users to manage properties and their details. It provides various functionalities such as viewing properties, adding properties, updating properties, deleting properties, searching properties, calculating total rents paid, and identifying properties that have not paid.

## Files

The project consists of the following files:

- `property_manager_class.py`: Contains the `PropertyManager` class, which handles the management of properties.
- `property_data_class.py`: Contains the `PropertyData` class, which defines the structure and properties of a property.
- `main.py`: Contains the main program logic and user interface.
- `Property_data.json`: A JSON file used to store property data.

## Dependencies

The project relies on the following external libraries and modules:

- `tabulate`: Used for creating formatted tables for displaying property information.
- `art`: Used for generating ASCII art text.
- `colorama`: Used for adding colors to the console output.
- `datetime`: Used for working with dates and times.
- `random`: Used for generating random numbers.

## Functionality

The Property Management System provides the following functionality:

1. View Properties: Displays a list of all properties.
2. Add Property: Allows the user to add a new property and its details.
3. Update Property: Enables the user to update the details of an existing property.
4. Delete Property: Allows the user to delete a property from the system.
5. Search Properties: Allows the user to search for properties based on certain criteria.
6. Total Rents Paid: Calculates and displays the total rents paid for all properties.
7. The Properties That Have Not Paid: Identifies and displays the properties that have not paid their rent.
8. Exit: Exits the program.

The program utilizes a menu-based user interface, where the user can input their choice to perform the desired action.

## Usage

To use the Property Management System, execute the `main.py` file. The program will present a menu with options numbered from 1 to 8. Enter the corresponding number to select an option and perform the desired action. Follow the prompts and provide the necessary input when required.

The program utilizes the `PropertyManager` and `PropertyData` classes to manage and store property information. The `Property_data.json` file is used to persist property data between program runs.

Please ensure that the required dependencies are installed before running the program.

## Note

This README.md file provides an overview of the project and its functionalities. For more detailed information and implementation details, refer to the source code files: `property_manager_class.py`, `property_data_class.py`, and `main.py`
