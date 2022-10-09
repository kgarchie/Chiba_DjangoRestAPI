# Chiba

## Getting Started

This API will be hosted soon on some server somewhere and therefore making this unnecessary.  
Indulge only to have fun and to learn or to extend the functionality.

### Steps

1. [Download and Install Python](#download-and-install-python)
1. [Set Up Workspace Folder](#set-up-workspace-folder)
1. [Clone this Repo](#clone-this-repo)
1. [Set Up a Virtual Environment](#set-up-a-virtual-environment)
1. [Set Up Django and Other Dependencies](#set-up-django-and-other-dependencies)
1. [Make Migrations](#make-migrations)
1. [Create a Superuser](#create-a-superuser-optional)
1. [Run Server](#run-server)
1. [Test at LocalHost](#test-at-localhost)


### Download and Install Python
You need python as the base interpreter. Download and install it from [Here](https://www.python.org/downloads/)

### Set Up Workspace Folder
Create a new folder in a memorable place - I'll call mine `Chiba`  
We'll use the desktop for this demo; you should too, should you get lost.  
Open the created folder in the terminal; should look something like this  
```
C:\Users\<username>\Desktop\Chiba>
```

### Clone this Repo
Type in `git clone https://github.com/kgarchie/Chiba_DjangoRestAPI.git .` to clone this repo into that folder. Note
the `.` at the end

```shell
git clone https://github.com/kgarchie/Chiba_DjangoRestAPI.git
```

### Set Up a Virtual Environment
Set up a virtual environment by using the following commands; This will work only if python was added
to [Path](https://datatofish.com/add-python-to-windows-path/).

```shell
python -m venv venv
```

This will create a folder named `venv` in the current folder which is `Chiba`.   
Activate the virtual environment so that we can install `django`

```shell
venv/Scripts/acivate
```

Note the `S` is capitalized and `Scipts` is in plural.

Some users may get an error. Something along the lines of `Runnig Scripts is not allowed on this sytem`.
To fix this error:-

- Open a new Terminal as Administrator
- Type in ```Set-Execution policy RemoteSigned``` and then `y` to accept the changes.
- (Optional) Read more
  about [Set-Execution Policy](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy?view=powershell-7.2)

**Note:** You will need to restart the Terminal(s) for changes to take effect. Re-Open the `Chiba` folder again in
terminal as described [above](#set-up-workspace-folder) to continue with this tutorial.  
**You will also need to activate the virtual environment again as shown [Here](#set-up-a-virtual-environment)**

### Set Up Django and Other Dependencies
Set up `django` and other dependencies like `django-restframework` using the command below.  
Make sure `requirements.txt` is present in `Chiba`.

```shell
pip install -r requirements.txt
```

### Make Migrations
Make the migrations - initialises the db

```shell
python manage.py makemigrations
```

Migrate - creates the tables in db

```shell
python manage.py migrate
```

### Create a Superuser (Optional)
Create a superuser using the command below

```shell
python manage.py createsuperuser
```

Follow the prompts to create the username, email and password

**Note:** Password input is not actually shown. It will remain blank even when keying it in; it's designed that way to hide
the password.
### Run Server
Run the server using the command below
```shell
python manage.py runserver
```

### Test at LocalHost
Open your browser at the shown link in the terminal, typically `127.0.0.1:8000`