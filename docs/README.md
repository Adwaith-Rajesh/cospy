## Init

The `init` command in simple terms is "`npm init`" but for all languages. It allows the user to quickly create all the stater files and folders necessary to start a project, some these files include, `.gitignore`, `LICENSE`, `setup.py`(Python).. etc.

Currently supported options are listed below.

```commandline
Usage: cos init [OPTIONS]

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

 * Create a python project named ade in directory named `test`
 ```commandline
 cos init -l python -n ade -d test
 ```

 * Create a python project named ade and create a new venv(assuming you have virtualenv installed)
 ```bash
 cos init -l python -n ade --env  # since --no-git is not passed this will also initialize a git repo.
 ```


 ## Clean
 The `clean` command is used to sort files in a directory based on their MIME type or extension.

 Currently supported options are listed below

 ```commandline
 Usage: cos clean [OPTIONS]

  Clean / Sort directory

Options:
  -d, --directory TEXT          The directory to clean  [default: .]
  -ct, --clean-type [ext|type]  ext: Group files by extension       
                                type: Group files by type  [default: ext]
  --help                        Show this message and exit.
 ```

 ___example___

 * Clean the current directory based on extensions
 ```commandline
 cos clean -ct ext  # by default -d is "."
 ```

 ## Tasks
 An easier way to manage tasks without leaving your terminal

 Currently supported options are listed below

 ```commandline
 Usage: cos tasks [OPTIONS] COMMAND [ARGS]...

  Manage programming tasks more easily

Options:
  -g, --group TEXT   The group to make changes to.
  -a, --add TEXT     add a new task.
  -r, --remove TEXT  remove a task.
  -d, --done TEXT    mark task as done.
  --help             Show this message and exit.

Commands:
  delete  Delete a task group
  ls      List all the groups or task in a group cos tasks ls...
  new     Create new task group

 ```

 ___examples___

* Create a new task group.
  <br>
  <br>
  A task group as the name suggest is a way to group your task into different categories. Each task group can be named after the project that you are working on or anything else.
  <br>
  A task group can be made using the following command.
  ```bash
  cos tasks new <group-name>
  ```

* Delete a task group.
  ```bash
  cos tasks delete <group-name>
  ```

* List all the task group or all tasks in a group
  * To list all the groups.
    ```bash
    cos tasks ls
    ```
  * To list all the tasks in a group.
    ```bash
    cos tasks ls <group-name>
    ```
* Adding, Removing, Marking tasks.
<br>
<br>
In each group a task can be added, removed or marked as Done.

  * Add a new task to the group.
    <br>
    When a new task is made an id will be generated to the task, which will be printed to the console.
    ```bash
    cos tasks -g <group-name> -a <task-description>
    ```

  * Remove a task from the group.
    ```bash
    cos tasks -g <group-name> -r <task-id>
    ```
  * Mark task as done.
    ```bash
    cos venv -g <group-name> -d <task-id>
    ```

## Venv

### For windows only
<br>

Venv is a simple and easy python virtual env manager.

Currently supported options are listed below.
```commandline
Usage: cos cli [OPTIONS] COMMAND [ARGS]...

  Manage all your Python venv in a single place.

Options:
  --help  Show this message and exit.

Commands:
  ls   List all the venv created by 'cos venv'
  new  Create a new virtualenv
  rm   Remove a virtual env
```

___examples___

* Create a new venv.

  By default the venv are created in the directory specified in the `COS_VENV_DIR` path variable. If not it will be saved in `%USERPROFILE%\cos_venvs"`. To create a new venv run the following command.

  ```bash
  cos venv new <venv-name>
  ```

* Remove a venv

  Remove a venv made by `cospy`
   ```bash
   cos venv rm <venv-name>
  ```

* List all the venv.

  To list all the venv created by `cospy`. Run the following command.
  ```bash
  cos venv ls
  ```
* Activate venv

  To activate a venv created by `cospy`. Run the following command.

  ```bash
  cosenv <venv-name>
  ```
