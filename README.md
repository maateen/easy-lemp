# Easy-LEMP
EasyLEMP is a Python3 script. EasyLEMP will help you to install LEMP (<b>Nginx, PHP-FPM, MariaDB</b>) on Linux along with <b>phpMyAdmin</b> with just four commands. Currently it only supports <b>Ubuntu Desktop Edition</b>. Support for <b>Ubuntu Server Edition</b> is now under development. Please, try to contribute if you can.

# Requirements
>>> Python 3 

>>> Working Internet Connection

# Installation
<code>wget https://github.com/callmehuyv/EasyLEMP/archive/master.zip</code>

<code>unzip Easy-LEMP-master.zip</code>

<code>cd Easy-LEMP-master/</code>

<code>python3 setup.py</code>

# Usage
>>> <b>/home/username/public_html</b> is your <b>web server root</b> directory.

>>> To access <b>phpMyAdmin</b>, just type <b>http://localhost/phpmyadmin</b> and press enter. To log in to phpMyAdmin, Use root as username and your MariaDB root password as password.

# Testing
Let's test the LEMP whether it's working or not.

>>> Create a <b>index.php</b> file within your web server root directory.

>>> Now paste the following code, then save it:

<code><?php phpinfo(); ?></code>

>>> Now open your favorite browser and hit <b>http://localhost/</b>. If you can see the <b>PHP Information</b> page, then it's all right. Otherwise, create an issue with this link: https://github.com/ugcoder/Easy-LEMP/issues/new