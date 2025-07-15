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

## Python Version

This environment was created with Python 3.x
