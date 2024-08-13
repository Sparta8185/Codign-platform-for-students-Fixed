# Codign platform for students

This project is a web-based platform that allows students to write, compile, and run C programs directly from their browsers. Additionally, the platform includes a PDF viewer that contains a C language book. 

<img width="1344" alt="Screenshot 2024-08-13 at 22 44 11" src="https://github.com/user-attachments/assets/b086f912-7f03-4561-b349-59a67db39dec">

## Features

- **Code Editor**: An integrated code editor with syntax highlighting. The editor is pre-loaded with a simple "Hello, World!" C program.
- **Input/Output Areas**: Separate areas for entering input and displaying the C program output.
- **PDF Viewer**: Displays a PDF document on the right side of the page.
- **Save Feature**: Allows users to save their code as a .c file, ensuring that their work is preserved and can be accessed later.
- **Open Feature**: Enables users to load previously saved .c files into the code editor, allowing them to continue working on their code from where they left off.

## Requirements

### Python
- **Python 3.x** is required to run the Flask server.

### Python Dependencies
Install the required Python packages using the `requirements.txt` file:

```pip install -r requirements.txt```


### GCC (GNU Compiler Collection)
GCC is required to compile C programs. Check if GCC is installed by running:

```gcc --version```


If GCC is not installed, follow the instructions for your operating system:

- **Ubuntu/Debian**:

```
sudo apt-get update
sudo apt-get install gcc
```

- **macOS** (requires Xcode command line tools):

```xcode-select --install```


- **Windows**:
- Install [MinGW](http://www.mingw.org/) or use the Windows Subsystem for Linux (WSL) to get a Unix-like environment.

### Static Files
- **iyteicon.png**: Icon for the webpage.
- **sample.pdf**: PDF document to be displayed on the right side of the page.

## Project Structure

```
/project-root
    /templates
        main.html         # Main HTML file for the web interface
    /static
        iyteicon.png      # Icon for the webpage
        sample.pdf        # PDF to be displayed on the right side
    app.py                # Flask application code
    requirements.txt      # Python dependencies
```


## Running the Project

1. **Install Python dependencies**:

   ```pip install -r requirements.txt```

2. **Ensure GCC is installed** as described above.

3. **Start the Flask application**:

   ```python app.py```

4. **Access the application** by navigating to ```http://127.0.0.1:5000/``` in your browser.

## Notes

- The platform is designed to run locally, and no login is required for users.
- The initial C program loaded into the editor is a simple "Hello, World!" program.
- The right side of the page displays a PDF document, and the signature "Created by Res. Asst. Okan DÜZYEL, Dept. of Electrical and Electronics Engineering".

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.



