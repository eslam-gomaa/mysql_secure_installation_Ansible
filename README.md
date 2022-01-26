

# mysql_secure_installation_Ansible


<br>

<br>

# ✋ Wait a second !

This module has been refactored to get rid of the dependencies issue across distributions, And it's much simpler now.


### Updates

- [x] use `pymysql` lib instead of `MySQLdb 👎`
- [x] Enable authentication with unix_socket
- [x] Add an option to disable unix_socket
- [x] make the output more understandable
- [x] run different commands based on different MySQL versions (Due to changes in newer MySQL versions)


### To do,

- [ ] Update the module doc
- [ ] Test with more distributions
- [ ] Validate that `disable_unix_socket` works well in MySQl version >= 1.4

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


## Dependencies

This is NOT something to worry about, It is something to make sure it's meet if you faced an error

1. **mysqladmin** command (already installed with MySQL/Mariadb)  -- Needed to get information such as `unix_socket` location & MySQL version
2. **python-pymysql** which can be easily installed using the pkg manager e.g: apt, yum
   * The only caveat is that this package name may differ between distributions e.g: `python3-pymysql` or `python36-pymysql` (Trying to cover all the possible differences in the example provided)


## Usage


💎 A full sample is provided at [sample-playbook.yml](https://github.com/eslam-gomaa/mysql_secure_installation_Ansible/blob/master/sample-playbook.yml) which installs & secures MySQL --  Workes on the [tested distributions](https://github.com/eslam-gomaa/mysql_secure_installation_Ansible#test) below

```bash
# Modify the hosts
ansible-playbook sample-playbook.yml
```



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

## Test

Below, is a list of the tested distributions

💎 I'll be more than happy when you let me know if you faced an error ! 

| Distribution                         | Test result          |  Comment |
| ------------------------------ | --------------------------   |----------|
| Centos 6                       |            ⏱️                |          |
| Centos 7                       |![](https://jenkins.demo.devops-caffe.com/jenkins/buildStatus/icon?job=mysql_secure_installation_Ansible%2Fmaster&config=centos_7)|          |
| Centos 8                       |![](https://jenkins.demo.devops-caffe.com/jenkins/buildStatus/icon?job=mysql_secure_installation_Ansible%2Fmaster&config=centos_8)|          |
| fedora-34                      |![](https://jenkins.demo.devops-caffe.com/jenkins/buildStatus/icon?job=mysql_secure_installation_Ansible%2Fmaster&config=fedora34)|          |
| Debian 10 (buster)             |![](https://jenkins.demo.devops-caffe.com/jenkins/buildStatus/icon?job=mysql_secure_installation_Ansible%2Fmaster&config=debian10)|          |
| Ubuntu 16.04                   |![](https://jenkins.demo.devops-caffe.com/jenkins/buildStatus/icon?job=mysql_secure_installation_Ansible%2Fmaster&config=ubuntu_16_04)| had to upgrade Ansible to a newer version (Related to example syntax NOT the module)|
| Ubuntu 18.04                   |![](https://jenkins.demo.devops-caffe.com/jenkins/buildStatus/icon?job=mysql_secure_installation_Ansible%2Fmaster&config=ubuntu_18_04)|          |
| Ubuntu 20.04                   |![](https://jenkins.demo.devops-caffe.com/jenkins/buildStatus/icon?job=mysql_secure_installation_Ansible%2Fmaster&config=ubuntu_18_04)|          |

---

<br>

## Updates / News

as of Mariadb v10.4+ we can not use `update mysql.user` > Currently that affects `disable_unix_socket` option for Mariadb versions above 10.4 (need some investigation & will update the module)

**Error produced**
> ERROR 1356 (HY000): View 'mysql.user' references invalid table(s) or column(s) or function(s) or definer/invoker of view lack rights to use them

* https://stackoverflow.com/a/64841540

---

<br>

## Input

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
| `disable_unix_socket`          | Disable login with unix_socket                               | False         | Boolean |



---



## Debug Output


* **Note:**  The Module throws a `Warning` instead of an `Error` if the both the `login_password` &  `new_password` are incorrect

#### Sample output

![image](https://user-images.githubusercontent.com/33789516/123868353-dda1f080-d92f-11eb-9402-acac14be4474.png)

![image](https://user-images.githubusercontent.com/33789516/123868361-e0044a80-d92f-11eb-91c4-991e76c08aaf.png)




---
.

## Known issues

```bash
No package matching 'python*-pymysql' is available
```

If you face this, don't worry it's **NOT an issue**, the problem is that `python-pymysql` might has a different name on the distro you're using

You'll probably face this if you are using a non [tested](https://github.com/eslam-gomaa/mysql_secure_installation_Ansible#test) distribution


![image](https://user-images.githubusercontent.com/33789516/123947208-6bb5bf80-d9a0-11eb-98b1-9e7b89afe2de.png)

### Fix

Just Update `pymysql` package name with the correct name in the playbook


![image](https://user-images.githubusercontent.com/33789516/123947630-e088f980-d9a0-11eb-9d4a-b300fd9a22cd.png)


### Extra mile
 
It is much appreciated ♥️ if you share package name on your tested distribution either with opening an issue or a pull request.


---


#### Read the Module’s Documentation

```bash
cd playbook_directory
# OR
cd role_directory
ansible-doc -M library mysql_secure_installation -v
```

---

.

### Please leave a ⭐ if you found it useful

.

Thank you

Maintainer: [Eslam Gomaa](https://www.linkedin.com/in/eslam-gomaa/)

