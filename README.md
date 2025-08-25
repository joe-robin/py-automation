# Python Virtual Environment Setup

This project uses a Python virtual environment to manage dependencies locally.

## Getting Started

### Activate the virtual environment:

```bash
source venv/bin/activate
```

### Install dependencies:

```bash
pip install -r requirements.txt
```

### Deactivate the virtual environment:

```bash
deactivate
```

## Adding Dependencies

When you install new packages, update the requirements.txt file:

```bash
pip freeze > requirements.txt
```

## Environment Variables

The project uses a `.env` file to store environment variables. Make sure to:

1. Update the `.env` file with your actual values:

   - `URL`: The target URL for your automation
   - `USERNAME`: Your username
   - `PASSWORD`: Your password

2. Load environment variables in your Python code:

```python
from dotenv import load_dotenv
import os

load_dotenv()

url = os.getenv('URL')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
```

**Note**: Never commit the `.env` file to version control. Add it to your `.gitignore` file.

## Project Structure

```
py-automation/
├── main.py              # Main entry point
├── paths.py             # Route handling and browser management
├── config.py            # Configuration settings
├── modules/
│   ├── login.py         # Login functionality
│   └── attendance.py    # Attendance automation
├── desktop/             # Desktop shortcuts
│   ├── check-in.desktop # Check-in shortcut
│   ├── check-out.desktop # Check-out shortcut
│   └── check-status.desktop # Status check shortcut
├── venv/                # Python virtual environment
├── .env                 # Environment variables
└── requirements.txt     # Python dependencies
```

## Desktop Shortcuts

The project includes desktop shortcuts for easy access to automation functions.

### Available Shortcuts:

- **Check In** (`check-in.desktop`) - Toggle attendance status
- **Check Out** (`check-out.desktop`) - Check out from attendance
- **Check Status** (`check-status.desktop`) - View current attendance status

### Setup Instructions:

1. **Customize Paths**: Update the desktop files with your actual project path:

   ```bash
   # Replace this path in both desktop files:
   /home/joe-icanio/Learning/py-automation

   # With your actual project path, for example:
   /home/yourusername/Projects/py-automation
   ```

2. **Move to Desktop Folder**:

```bash
# Move desktop files to your Desktop for easy access
mv desktop/check-in.desktop ~/Desktop/
mv desktop/check-out.desktop ~/Desktop/
mv desktop/check-status.desktop ~/Desktop/
```

3. **Make Executable**:

```bash
# Make all desktop files executable
chmod +x ~/Desktop/check-in.desktop
chmod +x ~/Desktop/check-out.desktop
chmod +x ~/Desktop/check-status.desktop
```

4. **Verify Installation**:
   - The desktop shortcuts should now appear on your Desktop
   - Double-click any shortcut to run the automation
   - The shortcuts should now be clickable and functional

### Desktop File Customization:

Edit the desktop files to change:

- **Name**: Display name in applications menu
- **Comment**: Description shown on hover
- **Icon**: Path to custom icon (PNG format recommended)
- **Exec**: Command to execute (update paths as needed)

## Usage

### Command Line:

```bash
# Check current status
python main.py status

# Toggle attendance (check-in/check-out)
python main.py check-in
python main.py check-out

# No arguments - toggle current status
python main.py
```

### Desktop Shortcuts:

- Double-click the desktop shortcuts for quick access
- Terminal will open, run the command, and wait for Enter key to close

## Python Version

This environment was created with Python 3.x
