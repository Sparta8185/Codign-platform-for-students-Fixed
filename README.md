# Codign-platform-for-students

This project is a web-based platform designed to allow students to write, compile, and run C programs directly from their browser. The platform is built using Flask for the backend, with a frontend code editor powered by CodeMirror. Additionally, the platform includes a PDF viewer and a user management interface for lab sessions.


<img width="1348" alt="Screenshot 2024-08-13 at 09 28 37" src="https://github.com/user-attachments/assets/ae62f0e8-e9e4-4e00-9b1a-52e6e4569aea">


## Features

- **Code Editor**: An integrated code editor with syntax highlighting, using CodeMirror. The editor is pre-loaded with a simple "Hello, World!" C program.
- **Input/Output Areas**: Separate areas for entering input and displaying the output of the C program.
- **PDF Viewer**: Displays a PDF document on the right side of the page, with an aligned signature at the bottom right.
- **User Management**: Admin interface to manage users, track their connection status, and control lab sessions.

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



