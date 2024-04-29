"""
This library provides diverse conversions and formatters to assist the main program. 
It offers functions to handle date formatting, converting strings to floats, handling commas in numbers,
updating data structures, and verifying data integrity.
"""
from datetime import date

def brazilian_date_formatter(date: date) -> str:
    """
    Formats a date object into a string with the format 'dd-mm-yyyy'.

    :parameters: date (date): A date object to be formatted.
    :returns: str: The formatted date as a string.
    """

    new_date = date.strftime('%d-%m-%Y')
    return new_date

def date_conversor(value: list[tuple]) -> list[list]:
    """
    Converts date values within a list of tuples to the 'dd-mm-yyyy' format.

    :parameters: value (list[tuple]): A list of tuples containing date values.
    :returns: list[list]: A list of lists with dates formatted as 'dd-mm-yyyy'.
    """

    date_index = 3
    new = [list(i) for i in value]
    for i in new:
        i[date_index] = brazilian_date_formatter(i[date_index])
    return new

def float_conversor(value: list[str]) -> list:
    """
    Converts string representations of floats to actual float values.

    :parameters: value (list[str]): A list containing strings representing float values.
    :returns: list: A list with string float representations converted to actual float values.
    """

    list_index = [4, 5, 6]
    for i in list_index:
        if value[i] is not None:
            value[i] = float(value[i].replace(',', '.'))
    return value

def comma_converter(data:list[list]) -> list[list]:
    """
    Converts decimal points to commas within specified indices in a list of lists.

    :parameters: data (list[list]): A list of lists where decimal points need to be converted to commas.
    :returns: list[list]: The modified list of lists with decimal points converted to commas.
    """
    dot_index = [4,5,6]
    for list_ in data:
        for index in dot_index:
            if list_[index] is not None:
                list_[index] = str(list_[index]).replace('.', ',')
    return data

def update_conversor(data: list[str]) -> list:
    """
    Updates data by converting string representation of a float to a float value.

    :parameters: data (list[str]): A list containing data to be updated.
    :returns: list: A list with the second element converted to a float.
    """
    new = [data[0], float(data[1].replace(',', '.')), data[2]]
    return new

def read_conversor(data: list[tuple]) -> list[list]:
    """
    Chains multiple conversions to prepare data for processing.

    :parameters: data (list[tuple]): A list of tuples containing data to be converted.
    :returns: list[list]: A processed list of lists ready for further processing.
    """
    first_conversion = date_conversor(data)
    second_conversion = comma_converter(first_conversion)
    last_conversion = remove_ids(second_conversion)
    return last_conversion

def remove_ids(data: list[list]):
    """
    Removes the first element (ID) from each inner list.

    :parameters: data (list[list]): A list of lists containing data with IDs.
    :returns: list: A list of lists with the IDs removed.
    """
    new = [i[1:] for i in data]
    return new

def remove_none(data:list):
    """
    Removes any None values from a list.

    :parameters: data (list): A list potentially containing None values.
    :returns: list: A list with None values removed.
    """
    new = [i for i in data if i is not None]
    return new

def verifier(data:list[str]) -> bool:
    """
    Verifies if the first element in the list is in uppercase.

    :parameters: data (list[str]): A list containing strings.
    :returns: bool: True if the first element is in uppercase, False otherwise.
    """
    test = data[0].upper()
    return test.isupper()
