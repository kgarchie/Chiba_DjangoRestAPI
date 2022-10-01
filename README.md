# ichiba

#### ~slogan

## Getting Started

This API will be hosted soon on some server somewhere and therefore making this unnecessary. <br>
Indulge only to have fun and to learn or to extend the functionality.

### Steps

<ol>
<li><a href="#1">Download and Install Python</a></li>
<li><a href="#2">Set Up Workspace Folder</a></li>
<li><a href="#3">Clone this Repo</a></li>
<li><a href="#4">Set Up a Virtual Environment</a></li>
<li><a href="#5">Set Up Django and Other Dependencies</a></li>
<li><a href="#6">Make Migrations</a></li>
<li><a href="#7">Create a Superuser</a></li>
<li><a href="#8">Run Server</a></li>
<li><a href="#9">Test at LocalHost</a></li>
</ol>

<h3 id="1">Download and Install Python</h3>
You need python as the base interpreter. Download and install it from [Here](https://www.python.org/downloads/)
<h3 id="2">Set Up Workspace Folder</h3>
Create a new folder in a memorable place - I'll call mine `ichiba`<br>
We'll use the desktop for this demo; you should too, should you get lost. <br>
Open the created folder in the terminal; should look something like this <br>
<code>
C:\Users\<username>\Desktop\ichiba>
</code>

<h3 id="3">Clone this Repo</h3>
Type in `git clone https://github.com/kgarchie/ichiba_DjangoRestAPI.git .` to clone this repo into that folder. Note
the `.` at the end

```shell
git clone https://github.com/kgarchie/ichiba_DjangoRestAPI.git
```

<h3 id="4">Set Up a Virtual Environment</h3>
Set up a virtual environment by using the following commands; This will work only if python was added
to [Path](https://datatofish.com/add-python-to-windows-path/).

```shell
python -m venv venv
```

This will create a folder named `venv` in the current folder which is `ichiba`. <br>
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

**Note:** You will need to restart the Terminal(s) for changes to take effect. Re-Open the `ichiba` folder again in
terminal as described <a href="#3">above</a> to continue with this tutorial. <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **You will also need to activate the virtual environment again as shown <a href="#4">Here</a>**

<h3 id="5">Set Up Django and Other Dependencies</h3>
Set up `django` and other dependencies like `django-restframework` using the command below. <br>
Make sure `requirements.txt` is present in `ichiba`.

```shell
pip install -r requirements.txt
```

<h3 id="6">Make Migrations</h3>
Make the migrations - initialises the db

```shell
python manage.py makemigrations
```

Migrate - creates the tables in db

```shell
python manage.py migrate
```

<h3 id="7">Create a Superuser (Optional)</h3>
Create a superuser using the command below

```shell
python manage.py createsuperuser
```

Follow the prompts to create the username, email and password

**Note:** Password input is not actually shown. It will remain blank even when keying it in; it's designed that way to hide
the password.
<h3 id="8">Run Server</h3>
Run the server using the command below
```shell
python manage.py runserver
```

<h3 id="9">Test at LocalHost</h3>
Open your browser at the shown link in the terminal, typically `127.0.0.1:8000`