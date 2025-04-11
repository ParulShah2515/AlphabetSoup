# AlphabetSoup
This Python script counts how many times the word "PENNYMAC" can be formed using the letters from a given string, which is passed as input. The script works by counting the occurrences of each letter required to form the word "PENNYMAC" and compares those counts to the available letters in the input string.

## Requirements

- Python 3.x
### Check Python Version

  To check if Python is installed and verify the version, open your terminal or command prompt and run the following command:<br>
  
![image](https://github.com/user-attachments/assets/3d31ebd5-a38c-4148-aa34-4105bd28e421)



Alternatively, if you're using python3, you can use:


![image](https://github.com/user-attachments/assets/930821f3-6d06-474a-9233-bea36de45c05)

If you see output like Python 3.x.x, then Python 3 is already installed on your system.

### Install Python
If Python is not installed, you can download and install it from the official Python website:
- [Download Python](https://www.python.org/downloads/) 

## Installation


1. There is no need to install any additional libraries, as the script only uses Python's built-in collections module.
2. Clone this repository or download the script to your local machine.

## Run 
1. Open the terminal and Navigate to the directory where you cloned the repository. 
2. Run the below command. 

![image](https://github.com/user-attachments/assets/ff709790-3d8a-4ee9-a3be-3db5e345c1fc)


## OUTPUT
![image](https://github.com/user-attachments/assets/93847452-6faa-47d1-9de8-4dad33e4ffa3)
> [!NOTE]
> If you want to change the input for the alphabet bowl, you need to manually update the value of the alphabet_soup variable in the Python script.


## Code Walkthrough
### Function: count_pennymac_occurrences
1. Target word: The target word is "PENNYMAC".
2. Counting occurrences: The function counts how many times each character in the target word appears in the input string.
3. Finding minimum occurrences: For each character in "PENNYMAC", the function calculates the maximum number of times that character can be used from the available letters. The minimum of these values determines the maximum number of times the whole word "PENNYMAC" can be formed.

### Dependencies
1. collections.Counter: This built-in module is used to count the frequency of characters in both the target word and the input string.


### Enhancements
> [!IMPORTANT]
> Instead of hardcoding the alphabet bowl value inside the Python script, we can modify the script to accept the input as a parameter at runtime using sys.argv, allowing the user to provide the input directly when executing the script.

