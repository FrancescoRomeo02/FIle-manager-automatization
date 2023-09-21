# Description

This program enables continuous monitoring of one or more folders and manages the files within them, specifically sorting added files in the observed folder(s) into various subfolders.

## Important

### Required Libraries for Execution:

To run the program, you need to install the following Python libraries:<br>

- `dotenv`: Install with `pip3 install python-dotenv` [link](https://pypi.org/project/python-dotenv/)<br>
- `watchdog`: Install with `pip3 install watchdog` [link](https://pypi.org/project/watchdog/)

### Path of Files to Manage:

To execute the program, create a `.env` file and initialize the variables as follows:<br>

- `PATH_TO_SCAN`: Path to be scanned <br>
- `PATH_IMAGE`: Path to the image folder <br>
- `PATH_VIDEO`: Path to the video folder <br>
- `PATH_DOCUMENTS`: Path to the documents folder <br>
- `PATH_COMPRESSED`: Path to the compressed files folder <br>
- `PATH_EXECUTABLES`: Path to the executables folder <br>
- `PATH_NOT_RECOGNIZED`: Path to the unrecognized files folder <br>

If you prefer not to write it manually, you can download a preconfigured `.env` file from this [link](https://github.com/FrancescoRomeo02/File-manager-automatization/blob/main/demo.env).

#### Examples
- `PATH_TO_SCAN = "/Users/name/Downloads"`
- `PATH_DOCUMENTS = "/Users/name/Documents"`

### Automatic Execution

For automatic execution, create a link to the `.vbs` file within the folder: <br>
`C:\Users\'USER NAME'\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`

## What I learned

- **File Handling**: Gained hands-on experience in manipulating files using Python, utilizing functions to read, write, and move files.
- **Path Manipulation**: Acquired knowledge of constructing and managing file paths, ensuring cross-platform compatibility with methods like `os.path.join()`.
- **Directory Interaction**: Explored directory operations, such as creating, deleting, and navigating directories, using functions from the `os` module.
- **Error Handling**: Developed an understanding of handling potential errors, enhancing the script's robustness and reliability.
- **Operating System Interaction**: Deepened comprehension of Python's interaction with the underlying operating system for effective file and folder management.
- **Documentation**: Creating clear and concise documentation, such as this README file, helps users understand the purpose and usage of the script.

## Contact Me
Feel free to get in touch via:
- 📧 Email: romeo.francesco.2002@gmail.com
- 💼 LinkedIn: [Francesco Romeo](https://www.linkedin.com/in/FrancescoRomeo02)
