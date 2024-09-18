from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator

class Employee(models.Model):
    # Name: Validate that it's not too short
    name = models.CharField(max_length=200, validators=[RegexValidator(r'^[a-zA-Z ]+$', 'Name must contain only letters and spaces')])

    # Address: No specific validation needed here as it's free text
    address = models.CharField(
        max_length=300,
        validators=[RegexValidator(r'^[a-zA-Z0-9 ,.-]+$', 'Address must contain only letters, numbers, spaces, and the characters , . -')]
    )

    # Phone number: Validate that it contains only digits and has a length between 7 to 15 digits
    phone_number = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(r'^[\d\s\-\+]+$', 'Phone number must contain only digits, spaces, dashes, or a plus sign'),
            RegexValidator(r'^.{7,15}$', 'Phone number must be between 7 and 15 characters')
        ],
        unique=True
    )


    # Salary: Ensure that salary is a positive value
    salary = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(0.01, 'Salary must be a positive number')]
    )

    # Designation: Ensure it's a string with only letters and spaces
    designation = models.CharField(
        max_length=100, 
        validators=[RegexValidator(r'^[a-zA-Z ]+$', 'Designation must contain only letters and spaces')]
    )

    # Description: No specific validation needed here as it's free text
    description = models.TextField()

    def __str__(self):
        return self.name
