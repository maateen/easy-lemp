# Easy-LEMP
EasyLEMP is a Python3 script. EasyLEMP will help you to install LEMP (<b>Nginx, PHP-FPM, MariaDB</b>) on Linux along with <b>phpMyAdmin</b> with just four commands. Currently it only supports <b>Ubuntu Desktop Edition</b>. Support for <b>Ubuntu Server Edition</b> is now under development. Please, try to contribute if you can.

# Version
Easy-LEMP is in <b>beta stage</b>. Please, create an issue with this link: https://github.com/ugcoder/Easy-LEMP/issues/new if you get one.

<i>Alpha version:</i> You can install Nginx, PHP-FPM, MariaDB, phpMyAdmin at once.

<i>Beta Version:</i> Implementing feature request by <b>Tarikur Rahaman Sohel</b>, making the script user interactive. Now you can choose what you wanna install and what not.

# Requirements
1. Python 3

2. Working Internet Connection

# Installation
Press <i>Ctrl+Alt+T</i> to open Terminal in Ubuntu. Then apply the following commands one by one:

```
wget https://github.com/ugcoder/Easy-LEMP/archive/master.zip
```

```
unzip Easy-LEMP-master.zip
```

```
cd Easy-LEMP-master/
```

```
python3 setup.py
```

# Usage
1. **/home/username/public_html** is your **web server root** directory.

2. To access **phpMyAdmin**, just type **http://localhost/phpmyadmin** and press enter. To log in to phpMyAdmin, Use root as username and your MariaDB root password as password.

# Testing
Let's test the LEMP server whether it's working or not.

1. Create a **index.php** file within your web server root directory.

2. Now paste the following code, then save it: 
```
<?php phpinfo(); ?>
```

3. Now open your favorite browser and hit **http://localhost/**. If you can see the **PHP Information** page, then it's all right. Otherwise, create an issue with this link: https://github.com/ugcoder/Easy-LEMP/issues/new
