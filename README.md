

# mysql_secure_installation_Ansible

# ✋ Wait a second !

This module has been refactored to get rid of the dependencies issue across distributions, And it's much simpler now.


### Updates

- [x] use `pymysql` lib instead of `MySQLdb 👎`
- [x] Enable authentication with unix_socket
  * Logic:
    * If socket is found, try to login with socket
       * If not able to login with socket, login with user/password
- [x] Add an option to disable unix_socket
- [x] make the output more understandable


### To do,

- [ ] Update the module doc
- [ ] Test with more distributions



---



## Features

An **Idempotent** Ansible Module that provides the functions of `mysql_secure_installation`

- Change MySQL Root Password - for a list of hosts i.e `localhost`, `127.0.0.1`, `::1`, .etc.
- Remove Anonymous User
- Disallow Root Login Remotely
- Remove Test Database
- disable unix_socket

💎 The Module is **Idempotent** Means that when you run it again, will not re-execute the commands *If the desired state meets the current state*



---



## Usage



💎 Please take a look 👓 at [sample-playbook.yml](https://github.com/eslam-gomaa/mysql_secure_installation_Ansible/blob/master/sample-playbook.yml), where you will find a full example of Installing MySQL & using `mysql_secure_installation` Ansible Module

> Make sure the `MySQL-python` Python Library’s Installation is handled by your Playbook code, An Example Is provided in `sample_playbook.yml`



---

* **To use a custom Ansible Module:**
  *  create a directory called `library` in your `playbook` or your `role`'s  directory

```bash
cd my_playbook_folder
# OR
# cd my_role_folder
mkdir library
cp mysql_secure_installation.py library/
```



---



* **Example** - with a fresh MySQL Installation

```yaml
- name: test mysql_secure_installation
  mysql_secure_installation:
    login_password: ''
    new_password: password22
    user: root
    login_host: localhost
    hosts: ['localhost', '127.0.0.1', '::1']
    change_root_password: true
    remove_anonymous_user: true
    disallow_root_login_remotely: true
    remove_test_db: true
  register: mysql_secure
  
# To see detailed output
- debug:
    var: mysql_secure
```



* **Example** - Change an existing `root` password

```yaml
- name: test mysql_secure_installation
  mysql_secure_installation:
    login_password: password22
    new_password: password23
    user: root
    login_host: localhost
    hosts: ['localhost', '127.0.0.1', '::1']
```



---



## Input 👓

| :Param                         | :Description                                                 | :Default      | :Type   |
| ------------------------------ | ------------------------------------------------------------ | ------------- | ------- |
| `login_password`               | Root's password to login to MySQL                            |               | String  |
| `new_password`                 | New desired Root password                                    |               | String  |
| `user`                         | MySQL user                                                   | root          | String  |
| `login_host`                   | host to connect to                                           | localhost     | String  |
| `hosts`                        | List of hosts for the provided user i.e `['localhost', '127.0.0.1', '::1']`, `Note:` all will have the same new password | [‘localhost’] | List    |
| `change_root_password`         |                                                              | True          | Boolean |
| `remove_anonymous_user`        |                                                              | True          | Boolean |
| `disallow_root_login_remotely` |                                                              | False         | Boolean |
| `remove_test_db`               |                                                              | True          | Boolean |
| `disable_unix_socket`          | Disable login with unix_socket                               | False          | Boolean |



---



## Debug Output



* If the `login_password` is correct, will change it to the `new_password`
* if the `new_password` is correct, then the *desired state* is met

* **Note:**  The Module throws a `Warning` instead of an `Error` if the both the `login_password` &  `new_password` are incorrect

| Code | Meaning   | Description                                                  |
| ---- | --------- | ------------------------------------------------------------ |
| 0    | `Success` | When repeat –> `meet the desired state`                      |
| 1    | `Fail`    | **`change_root_pwd`** - will output `1` if failed to change the password of at least 1 host, for more info check `hosts_success` & `hosts_failed` |



---



#### Read the Module’s Documentation

```bash
cd playbook_directory
# OR
cd role_directory
ansible-doc -M library mysql_secure_installation -v
```



Thank you

[Eslam Gomaa](https://www.linkedin.com/in/eslam-gomaa/)

