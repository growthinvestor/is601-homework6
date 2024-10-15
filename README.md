# IS-601 Homework 6
# Performed Testing Using logging, env and logging handling
# Cleared all errors and fixed issues

# Logging in Terminal

(myenv) ajaswal@AJ:~/projects/homework6$ python main.py
2024-10-14 21:10:00,530 - DEBUG - Program started.
2024-10-14 21:10:00,530 - DEBUG - Program started.

Options:
1. Add
2. Subtract
3. Multiply (using plugin)
4. Divide (using plugin)
5. Modulus
6. Exponentiate
7. Exit
Choose an option (1-7): 2
Enter the first number: 3
Enter the second number: 1
2024-10-14 21:10:05,164 - DEBUG - SubtractCommand initialized with a=3.0 and b=1.0
2024-10-14 21:10:05,164 - DEBUG - Executing SubtractCommand
2024-10-14 21:10:05,164 - INFO - Calculated 3.0 minus 1.0, result: 2.0
2024-10-14 21:10:05,164 - INFO - Result of the operation: 2
2024-10-14 21:10:05,164 - INFO - Result of the operation: 2
Result: 2

Options:
1. Add
2. Subtract
3. Multiply (using plugin)
4. Divide (using plugin)
5. Modulus
6. Exponentiate
7. Exit
Choose an option (1-7): 3
Enter the first number: 4
Enter the second number: 2
2024-10-14 21:10:07,908 - INFO - Result of the operation: 8
2024-10-14 21:10:07,908 - INFO - Result of the operation: 8
Result: 8

# Logging saved under logs --> app.log

2024-10-14 20:26:55,748 - ERROR - Invalid number input.
2024-10-14 20:35:16,160 - INFO - Result of the operation: 0
2024-10-14 20:35:20,351 - WARNING - Invalid choice: 345
2024-10-14 20:35:22,023 - INFO - Result of the operation: -1
2024-10-14 20:35:23,007 - WARNING - Invalid choice: 32
2024-10-14 20:35:23,808 - INFO - Result of the operation: 1
2024-10-14 20:35:24,623 - INFO - Result of the operation: 1
2024-10-14 20:35:25,759 - WARNING - Invalid choice: 
2024-10-14 20:35:26,559 - INFO - Result of the operation: -1
2024-10-14 20:35:27,863 - INFO - Result of the operation: 0
2024-10-14 20:35:28,633 - INFO - Result of the operation: 9
2024-10-14 20:35:30,752 - INFO - Result of the operation: 105
2024-10-14 20:35:32,240 - INFO - Result of the operation: 3
2024-10-14 20:37:40,298 - INFO - Result of the operation: 0
2024-10-14 20:37:45,338 - INFO - Result of the operation: 9
2024-10-14 20:40:57,598 - INFO - User chose to exit the program.
2024-10-14 21:10:00,530 - DEBUG - Program started.
2024-10-14 21:10:05,164 - INFO - Result of the operation: 2
2024-10-14 21:10:07,908 - INFO - Result of the operation: 8
2024-10-14 21:10:14,572 - INFO - Result of the operation: 2
2024-10-14 21:11:29,262 - INFO - Result of the operation: 1
2024-10-14 21:11:37,909 - ERROR - Invalid number input.
2024-10-14 21:11:46,422 - INFO - Result of the operation: 5
2024-10-14 21:12:03,902 - INFO - User chose to exit the program.
