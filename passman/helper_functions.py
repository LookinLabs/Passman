import sqlite3
import tkinter as tk

def toggle_password(entry, button):

    if entry["show"] == "*":

        entry["show"] = ""

        button.config(text="Hide")

    else:

        entry["show"] = "*"

        button.config(text="Show")



class PasswordValidation:

    def __is_correct_length(self, password: str) -> bool:
        """
        Check if the password's length is within the valid range.

        The password should have a length between 8 and 64 symbols.
        :param password: Password to be checked
        :return: True if the password's length is within the valid range, False otherwise
        """
        password_length = len(password)

        return password_length >= 8 and password_length <= 64


    def __includes_uppercase(self, password: str) -> bool:
        """
        Check if the password contains at least one uppercase letter.

        :param password: Password to be checked
        :return: True if the password contains at least one uppercase letter, False otherwise
        """
        for symbol in password:

            if symbol.isupper():

                return True

        return False


    def __includes_lowercase(self, password: str) -> bool:
        """
        Check if the password contains at least one lowercase letter.

        :param password: Password to be checked
        :return: True if the password contains at least one lowercase letter, False otherwise
        """
        for symbol in password:

            if symbol.islower():

                return True

        return False


    def __includes_special(self, password: str) -> bool:
        """
        Check if the password contains at least one special character (whitespace is also considered a special character).

        :param password: Password to be checked
        :return: True if the password contains at least one special character, False otherwise
        """
        for symbol in password:

            if not symbol.isalnum():

                return True

        return False


    def __includes_number(self, password: str) -> bool:
        """
        Check if the password contains at least one numeric digit.

        :param password: Password to be checked
        :return: True if the password contains at least one numeric digit, False otherwise
        """
        for symbol in password:

            if symbol.isdigit():

                return True

        return False


    def __is_different_from_old_password(self, old_pass: str, new_pass: str) -> bool:
        """
        Check if the new password is different enough from the old password.

        The overlap between the new password and old password should be less than 50%.
        The check for overlap is case-insensitive.
        The overlap is also checked for the reversed version of the new password.

        :param old_pass: The old password
        :param new_pass: The new password
        :return: True if the new password is different enough, False otherwise
        """
        new_pass_lowercase = new_pass.lower()

        new_password_length = len(new_pass_lowercase)

        half_of_old_password = len(old_pass) // 2

        for index in range(new_password_length - half_of_old_password + 1):

            end_index = index + half_of_old_password

            substring = new_pass_lowercase[index:end_index]

            if substring in old_pass or substring[::-1] in old_pass:

                return False

        return True


    def __is_name_in_password(self, password: str, name: str) -> bool:
        """
        The name received as input may contain whitespace to separate the first and last name, neither of which should be
        present in the password.
        If the name contains a hyphen (such as Mari-Liis), neither part of the name should be present in the password.
        The name should not be in the password even if the casing of it is different in the password.
        Reversed format of the name is also not allowed in the password

        :param password: The password to be validated
        :param name: The full name of the account owner
        :return: True if the name is present in the password, False otherwise
        """
        HYPHEN = "-"

        SPACE = " "

        password_lowercase = password.lower()

        name_lowercase = name.lower()

        name_without_hyphens = name_lowercase.replace(HYPHEN, SPACE)

        name_value = name_without_hyphens.split(SPACE)

        for part in name_value:

            if part in password_lowercase or part[::-1] in password_lowercase:

                return True

        return False


    def __is_birthday_in_password(self, password: str, birthdate: str) -> bool:
        """
        Check if the password contains the birthday of the account owner.

        The day, month or year in the birthdate cannot be present in the password. For the birth year, the last two digits
        of the birth year separately is also not allowed.

        For the day, month or last 2 digits of the year, the reversed number is allowed but for the full 4-digit year is
        not allowed in the reverse format.

        The date is always in the format "dd.mm.yyyy", where
        dd is 2-digit day (01, 02, .. 31)
        mm is 2-digit month (01, 02, .. 12)
        yyyy is 4-digit year (0001, 0002, ..., 2022, 2023, ..., 3000, ...)

        You don't have to validate the date.

        :param password: The password to be validated
        :param birthdate: Birthday of the account owner, format is dd.mm.yyyy
        :return: True if the birthday is present in the password, False otherwise
        """
        birthday_data = birthdate.split(".")

        full_year = birthday_data[-1]

        if full_year[::-1] in password:

            return True

        for number in birthday_data:

            if number[-2:] in password:

                return True

        return False


    def __is_password_valid(self, new_password: str, old_password: str, name: str, birthdate: str) -> bool:
        """
        Check whether the given password is valid.

        This function combines several checks to determine if the provided password is valid.
        It checks the length, presence of uppercase and lowercase letters, inclusion of at least one number,
        inclusion of at least one special character, absence of the user's name and birthdate in the password.
        Call the functions you wrote before within this one to complete the validation.

        :param new_password: The password to be checked
        :param old_password: the previous password of this account
        :param name: The user's full name
        :param birthdate: The user's birthdate
        :return: True if the password is valid, False otherwise.
        """
        length = self.__is_correct_length(new_password)

        uppercase = self.__includes_uppercase(new_password)

        lowercase = self.__includes_lowercase(new_password)

        special = self.__includes_special(new_password)

        number = self.__includes_number(new_password)

        difference = self.__is_different_from_old_password(old_password, new_password)

        name_in_password = self.__is_name_in_password(new_password, name)

        birthday = self.__is_birthday_in_password(new_password, birthdate)

        validators = (length, uppercase, lowercase, special, number, difference)

        falsy_validators = (name_in_password, birthday)

        return all(validators) and not all(falsy_validators)
