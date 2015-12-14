# Easy-LEMP
EasyLEMP is a Python3 script. EasyLEMP will help you to install LEMP (<b>Nginx, PHP-FPM, MariaDB</b>) on Linux along with <b>phpMyAdmin</b> with just four commands. Currently it only supports <b>Ubuntu Desktop Edition</b>. Support for <b>Ubuntu Server Edition</b> is now under development. Please, try to contribute if you can.

# Version
Easy-LEMP is in <b>beta stage</b>. Please, create an issue with this link: https://github.com/ugcoder/Easy-LEMP/issues/new if you get one.
>>>Alpha version: You can install Nginx, PHP-FPM, MariaDB, phpMyAdmin at once.
>>>Beta Version: Implementing feature request by <b>Tarikur Rahaman Sohel</b>, making the script user interactive. Now you wan choose what you wanna install and what not.

# Requirements
1. Python 3

2. Working Internet Connection

# Installation
Press <i>Ctrl+Alt+T</i> to open Terminal in Ubuntu. Then apply the following commands one by one:

<code>wget https://github.com/callmehuyv/EasyLEMP/archive/master.zip</code>

<code>unzip Easy-LEMP-master.zip</code>

<code>cd Easy-LEMP-master/</code>

<code>python3 setup.py</code>

# Usage
1. <b>/home/username/public_html</b> is your <b>web server root</b> directory.

2. To access <b>phpMyAdmin</b>, just type <b>http://localhost/phpmyadmin</b> and press enter. To log in to phpMyAdmin, Use root as username and your MariaDB root password as password.

# Testing
Let's test the LEMP server whether it's working or not.

1. Create a <b>index.php</b> file within your web server root directory.

2. Now paste the following code, then save it: <code><?php phpinfo(); ?></code>

3. Now open your favorite browser and hit <b>http://localhost/</b>. If you can see the <b>PHP Information</b> page, then it's all right. Otherwise, create an issue with this link: https://github.com/ugcoder/Easy-LEMP/issues/new