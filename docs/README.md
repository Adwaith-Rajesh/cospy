## Init

The `init` command in simple terms is "`npm init`" but for all languages. It allows the user to quickly create all the stater files and folders necessary to start a project, some these files include, `.gitignore`, `LICENSE`, `setup.py`(Python).. etc.

Currently supported options are listed below.

```commandline
Usage: cos cli [OPTIONS]

  Start a new project in any language

Options:
  -l, --language TEXT   The language used in the project
  -n, --name TEXT       The name of the project
  --license TEXT        The LICENSE to use  [default: mit]
  -d, --directory TEXT  The directory to create all the starter files and
                        folders.  [default: .]
  --env                 Create a virtual env for Python projects
  --no-git              Do not initialize a git repo
  --help                Show this message and exit.   
```

Some values like <b>author name</b> and <b>Author Email</b> which are used some times used the setup files and in some LICENSE file can be set in the [config.py](https://github.com/Adwaith-Rajesh/code-starter/blob/master/cos/config.py) file

Currently supported languages are.
  * Python

___example___

 * Create a python project named ade.
 ```commandline
 cos init -l python -n ade
 ```

 * Create python project named ade without initializing a git repo.
 ```commandline
 cos init -l python -n ade --no-git
 ```

 * Create a python project named ade in directory names `test`
 ```commandline
 cos init -l python -n ade -d test
 ```

 * Create a python project named ade and create a new venv(assuming you have virtualenv installed)
 ```bash
 cos init -l python -n ade --env  # since --no-git is not passed this will also initialize a git repo.
 ```