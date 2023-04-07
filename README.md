# Alvin
![logo](https://github.com/amankumawat-567/Alvin/blob/main/banner.png)

## Alvin - Desktop Assistant
Alvin is a desktop assistant that works on CUI with speech recognition. It can perform the following tasks:
* Tell Date and Time
* Set Timers
* Set Reminders
* Launch Applications
* Open Folders
* Search for Files
* Search on Google and YouTube
* Answer Questions using Wikipedia

### How to Use
To use Alvin, you need to say "Alvin" before issuing a command. For example, to ask for the current date and time, say "Alvin, what's the time?" or "Alvin, tell me the date and time".

#### Here are some commands that Alvin can understand:

* "Alvin, what's the time?" or "Alvin, tell me the date and time"
* "Alvin, set a timer for [duration]"
* "Alvin, remind me for [task] at [time]"
* "Alvin, open [folder name] folder" or "Alvin, open [folder name]"
* "Alvin, search for [file or folder name] in [parent folder name]"
* "Alvin, searchfor [query] on Google" or "Alvin, search for [query] on YouTube"
* "Alvin, what is [query]?"

Example Commands
* "Alvin, what's the time?"
* "Alvin, set a timer for 10 minutes"
* "Alvin, remind me for a meeting with client at 3:00 p.m. tommorow"
* "Alvin, open Chrome"
* "Alvin, open Documents folder"
* "Alvin, search for report.pdf in Downloads"
* "Alvin, search for weather in New York on Google"
* "Alvin, what is the capital of France?"

## Introduction:
Alvin is a speech recognition-based command-line interface (CUI) desktop assistant designed to assist users with various tasks. It offers features such as date and time display, reminders, app launching, web searches, folder opening, file searching, and answering questions using Wikipedia. This documentation provides a detailed overview of Alvin's features and functionalities.

## Installation:
To install and use Alvin, you must have Python 3.6 or later installed on your computer. Follow these steps to install and run Alvin:
1. Clone the Alvin Desktop Assistant repository from GitHub.
2. Install the required packages using the command `pip install -r requirements.txt`.
3. Run the assistant using the command `python Alvin.py`.

## Features and Functionality:

### Date and Time:
Alvin can speak the current date and time, including the weekday, month, and year, upon request. You can say "Alvin What's the current date and time?" or "Alvin Tell me the time" to hear the current date and time spoken aloud. If you want to know the weekday, month, or year specifically, you can ask Alvin by saying "Alvin What day is it today?", "Alvin What's the current month?", or "Alvin What's the current year?". Alvin will speak the requested information in a clear and concise manner, making it easy for you to stay on top of your schedule.

### Reminders:
Alvin allows you to create reminders for yourself.It understands natural language commands, making it easy to set reminders. For example, you can say "Alvin, remind me to call John at 3:00 p.m. on 5 march." It also works with flexible date options like "today" and "tomorrow".Alvin will remind you at the specified date and time.
It works like:
1. Speak the following command: "Alvin, remind me or set reminder for [task] at [time] [date]"
2. If you do not provide a date in your command, Alvin will assume that you want the reminder set for today.
3. If you want to set a reminder for a specific date, you can use words like "today," "tomorrow," or you can specify the date in a format such as "12 April."
4. Alvin will confirm your reminder by saying "Okay I'll remind you".

You can edit or delete reminders at any time by tapping on the reminder in the list.
In addition to setting reminders, Alvin can also set timers for you. To set a timer, say "Alvin Set a timer for [number] [unit]". For example, you can say "Set a timer for 10 minutes" or "Set a timer for 1 hour and 30 minutes". Alvin will start the timer and notify you when the time is up.

### App Launcher:
Alvin can launch applications installed on your computer. To launch an application, say "Alvin open [application name]". For instance, you can say "Alvin open Microsoft Word". Alvin will launch the application for you.

### Web Search:
Alvin can perform web searches for you on both Google and YouTube. To perform a search, say "Search for [query] on Google" or "Search for [query] on YouTube". Alvin will open the search results page in your default browser.With these features, you can quickly and easily access the information you need on the web.

### Folder Opener System:
Folder Opener System:
Alvin can help you open both system folders, such as Documents, Downloads, Desktop, Music, etc., and other random folders. To open a system folder, simply say "Alvin Open [folder name]" or "Alvin Open [folder name] folder". For example, you can say "Alvin Open Downloads" or "Alvin Open Documents folder" to open the Downloads or Documents folder, respectively.
To open other folders located in custom paths, you can specify the path by saying "Alvin Open [folder name] folder which is in [parent folder name] folder which is in [grandparent folder name] folder in [directory path] directory". For example, you can say "Alvin Open Projects folder which is in Documents folder which is in User folder in C directory" to navigate to the Projects folder located within the Documents folder, which is located within the User folder in the C directory. Alvin will navigate to the specified directory and open the folder for you. This feature makes it easy to access your files and folders, even if they are nested deep within your file system.

### File Search:
Alvin can help you search for files located on your computer, including files located in system folders like Documents and Downloads. To search for a file in a system folder, simply say "Alvin Search for [file or folder name] in [parent folder name]". For example, you can say "Alvin Search for My Resume in Documents" or "Alvin Search for Vacation Photos in Downloads" to search for files within those folders.
To search for files located in other folders, you can specify the path by saying "Alvin Search for [file or folder name] in [parent folder name] folder which is in [parent folder name] folder which is in [grandparent folder name] folder in [directory path] directory". For example, you can say "Search for Project Report in Clients folder which is in Projects folder which is in Documents folder in C directory" to search for the Project Report file located within the Clients folder, which is located within the Projects folder, which is located within the Documents folder in the C directory. Alvin will search for the file within the specified directory and its subdirectories.

This feature makes it easy to find files, even if they are located in a specific folder or subfolder on your computer.

### Wikipedia Search:
Alvin can help you find answers to your questions using Wikipedia. To ask a question, simply say "Alvin What is [query]?". For example, you can say "Alvin What is the capital of France?" to find out the capital of France. Alvin will search Wikipedia for the answer and provide it to you.
This feature is great for quickly finding information on a wide range of topics. Whether you're curious about historical events, famous people, or scientific concepts, Alvin can provide you with accurate and up-to-date information from one of the world's largest online encyclopedias.

### Conclusion:
Alvin is a powerful and versatile desktop assistant that can help you with various tasks using speech recognition. Its features include date and time display, reminders, app launching, web searches, folder opening, file searching, and Wikipedia search. With Alvin, you can make your daily tasks more accessible and efficient.

## To Run the Project in the Virtual Environment named "env":
1. Open your terminal/command prompt and navigate to the project directory.
1. Activate the virtual environment by running the command `source env/bin/activate` (for Unix-based systems) or `env\Scripts\activate` (for Windows).
1. Install the project dependencies by running the command `pip install -r requirements.txt`. This will install all the necessary libraries and packages required to run the project.
1. Run the main script by executing the command `python Alvin.py`.
1. Alvin will now start running in the command line interface with speech recognition enabled, and you can start interacting with it by giving voice commands.

Note: Before running the project, make sure that you have installed all the required dependencies listed in the `requirements.txt` file. Additionally, ensure that your microphone is properly connected and configured on your system, so that Alvin can accurately recognize your voice commands.

## Contributor's Guide
Thank you for considering contributing to our project! I welcome all contributions, big or small, and appreciate your effort to make this project better.

### Getting Started
Before you start contributing to the project, you need to follow these steps:
1. Fork the repository.
2. Clone the forked repository to your local machine.
3. Create a new branch for your feature or bug fix.
4. Make changes to the code and test your changes locally.
5. Push your changes to your forked repository.
5. Submit a pull request to our repository.

### Guidelines for Contributions
When contributing to the project, please keep the following guidelines in mind:
1. Follow the coding style and conventions used in the project.
2. Write clear and concise commit messages and pull request descriptions.
3. Make sure your code is well-documented and tested.
4. Ensure that your changes do not break any existing functionality.
5. Use meaningful variable and function names.
6. Keep your changes focused and specific to the issue you are addressing.

### Code of Conduct
I expect all contributors to follow our Code of Conduct. Please be respectful and considerate of other contributors and users of the project. Any violation of the Code of Conduct will not be tolerated.

### Reporting Bugs
If you find any bugs or issues in the project, please open an issue in the repository and provide as much detail as possible, including steps to reproduce the issue, error messages, and screenshots if applicable.

### Conclusion
I hope that you find Alvin helpful in your day-to-day tasks. If you have any feedback or suggestions, please feel free to reach out to us.