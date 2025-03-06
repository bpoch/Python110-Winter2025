# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Brian Pochert,03/01/2025, add classes and functions
#   Brian Pochert,03/03/2025, modify exception error messages in IO class
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program --------
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''

FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
menu_choice: str # Hold the choice made by the user.
students: list = []  # a table of student data

# All of these will be used locally
# student_first_name: str = ''  # Holds the first name of a student entered by the user.
# student_last_name: str = ''  # Holds the last name of a student entered by the user.
# course_name: str = ''  # Holds the name of a course entered by the user.
# student_data: dict = {}  # one row of student data
# csv_data: str = ''  # Holds combined string data separated by a comma.
# json_data: str = ''  # Holds combined string data in a json format.
# file = None  # Holds a reference to an opened file.


# Processing the data ---------------------------------------------#
class FileProcessor:
    """
    This is a collection of functions that work with the JSON data file
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        This function will read data from the JSON file
        :param file_name: name of the file to read data from
        :param student_data: list of student data in dictionaries
        :return: list
        """

        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("JSON file must exist before running this script",e)
        except Exception as e:
            IO.output_error_messages("There was a non specific error",e)
        finally:
            if file.closed == False:
               file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        This function will write the data to the JSON file
        :param file_name: Enrollments.json
        :param student_data: New student data add by the program
        :return: None
        """
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
            IO.output_student_courses(student_data=student_data)
        except TypeError as e:
            IO.output_error_messages("Please make sure data is in JSON format",e)
        except Exception as e:
            IO.output_error_messages("There was a non specific error",e)
        finally:
            if file.closed == False:
                file.close()



# Present and Process the data ---------------------------------------#
class IO:
    """
    A group of functions that manage the user input and output
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        this function displays the error messages to the program user
        :param message:
        :param error:
        :return: None
        """
        print(message, end="\n")
        if error is not None:
            print("-----Technical Error Message-----")
            print(error, error.__doc__, type(error), sep="\n")

    @staticmethod
    def output_menu(menu: str):
        """
        this function displays the menu to the program user
        :return: None
        """
        print()
        print(menu)
        print()

    @staticmethod
    def input_menu_choice():
        """
        This function takes the user input to the program
        :return: user inputted menu choice
        """
        choice = "0"
        try:
           choice = input("Enter your menu choice: ")
           if choice not in ("1","2","3","4"):
               raise Exception("Please choose option: 1, 2, 3, or 4")
        except Exception as e:
           IO.output_error_messages(e.__str__())

        return choice

    @staticmethod
    def output_student_courses(student_data : list):
        """
        This function displays the student course list
        :return: display student data
        """
        print("-" * 50)
        for student in student_data:
            print(f'{student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data : list):
        """
        This function takes the student information from the user
        :return: student data
        """
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student = {"FirstName": student_first_name,
                                "LastName": student_last_name,
                                "CourseName": course_name}
            students.append(student)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages("That was not the correct value", e)
        except Exception as e:
            IO.output_error_messages(e.__str__())
        return student_data

# Start of main code body #***********************

students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop

print("-"*40)
print("Program Ended")
print("Thank You")

