

# mysql_secure_installation_Ansible



## Features

An **Idempotent** Ansible Module that provides the functions of `mysql_secure_installation`

- Change MySQL Root Password - for a list of hosts i.e `localhost`, `127.0.0.1`, `::1`, .etc.
- Remove Anonymous User
- Disallow Root Login Remotely
- Remove Test Database

💎 The Module is **Idempotent** Means that when you run it again, will not re-execute the commands *If the desired state meets the current state*



---



## Usage



💎 Please take a look 👓 at [sample_playbook.yml](https://github.com/Eslam-Naser/mysql_secure_installation_Ansible/blob/master/sample_playbook.yml), where you will find a full example of Installing MySQL & using `mysql_secure_installation` Ansible Module

* make sure the `MySQL-python` Python Library’s Installation is handled by your Playbook code, An Example Is provided in `sample_playbook.yml`



---

* **To use a custom Ansible Module:**
  *  create a directory called `library` in your `playbook` or your `role`'s  directory

```bash
cd my_playbook_folder
# OR
# cd my_role_folder
mkdir library
cp mysql_secure_installation library/
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
  
  # To see more detailed output
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
    change_root_password: true
    remove_anonymous_user: true
    disallow_root_login_remotely: true
    remove_test_db: true
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





---



* Read the Module’s Documentation

```bash
cd mysql_secure_installation_Ansible
ansible-doc -M library mysql_secure_installation -v
```





