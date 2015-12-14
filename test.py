from apt import Cache
from os import environ, getcwd, mkdir, remove, system
def restart_server():
    # This function will restart NginX, MariaDB, PHP5-FPM if installed.
    cache = Cache()
    if cache['nginx'].is_installed:
    	system("sudo service nginx restart")
    	if cache['mariadb-server'].is_installed:
    		system("sudo service mysql restart")
    		if cache['php5-fpm'].is_installed:
    			system("sudo service php5-fpm restart")
    		else:
    			print("PHP isn't installed. So, it hasn't been started.")
    	else:
    		print("MariaDB isn't installed. So, it hasn't been started.")
    elif cache['mysql'].is_installed:
    	system("sudo service mysql restart")
    	if cache['php5-fpm'].is_installed:
    			system("sudo service php5-fpm restart")
    	else:
    		print("PHP isn't installed. So, it hasn't been started.")
    else:
    	system("sudo service php5-fpm restart")

def get_user_choice():
	# This function will hold the user choice
	choice = {}  # A dictionary, will contain user choice
	print("Welcome to Easy_LEMP!")
	print("Please let Easy_LEMP know your choice.")
	choice['nginx'] = input("Do you want Easy_LEMP to install NginX? (y/n): ")
	choice['mariadb'] = input(
		"Do you want Easy_LEMP to install MariaDB? (y/n): ")
	choice['php'] = input("Do you want Easy_LEMP to install PHP? (y/n): ")
	choice['phpmyadmin'] = input(
		"Do you want Easy_LEMP to install phpMyAdmin? (y/n): ")
	return choice

choice = get_user_choice()
print(choice)
restart_server()