# 🍀 Installing Virtual Environment in Older and Newer Versions of Python

# Creating a virtual environment allows you to manage your projects with specific and separate dependencies. Here’s how to install a virtual environment in both older and newer versions of Python.

# 🍀 Newer Versions of Python (Python 3.3 and Above)

# In newer versions of Python, the `venv` module is available by default, and you can use it to create virtual environments.

# 🔎 Installation Steps:
# 1. Open the Terminal** (Command Prompt or Terminal).
# 2. Create a Virtual Environment:
   
#    python -m venv myenv
   
#    Here, `myenv` is the name of your virtual environment folder. You can choose any name you prefer.

# 3. Activate the Virtual Environment:
#    - On Windows:
#      myenv\Scripts\activate


# 4. Deactivate the Virtual Environment:
#    deactivate
   

# 🍀 Older Versions of Python (Before 3.3)

# In older versions of Python, you need to use the `virtualenv` library.

# 🔎 Installation Steps:
# 1. Install virtualenv:
#    If virtualenv is not already installed, you can install it using pip:
#    pip install virtualenv
   

# 2. Create a Virtual Environment:
   
#    virtualenv myenv
   

# 3. Activate the Virtual Environment:
#    - On Windows:
#      myenv\Scripts\activate
   

# 4. Deactivate the Virtual Environment:
#    deactivate

# 🍀 To install a virtual environment on a specific version of Python, use the following command:

# py -3.10 -m venv myenv

# 🍀 Use the following method to install the package in a virtual environment:

# pip install package_name
