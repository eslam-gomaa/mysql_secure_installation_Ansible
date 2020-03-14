

# mysql_secure_installation_Ansible



## Features

An **Idempotent** Ansible Module that provides the functions of `mysql_secure_installation`

- Change MySQL Root Password - for a list of hosts i.e `localhost`, `127.0.0.1`, `::1`, .etc.
- Remove Anonymous User
- Disallow Root Login Remotely
- Remove Test Database



---





## Usage





* **Example** - with a fresh MySQL Installation

```yaml
- name: test mysql_secure_installation
  mysql_secure_installation:
    login_password: password
    new_password: password22
    user: root
    login_host: localhost
    hosts: ['localhost', '127.0.0.1', '::1']
    change_root_password: true
    remove_anonymous_user: true
    disallow_root_login_remotely: true
    remove_test_db: true
  register: secure
```



* **Example** - Change an existing password

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
  register: secure
```





* Read Module Documentation

```bash
cd mysql_secure_installation_Ansible
ansible-doc -M library mysql_secure_installation -v
```





