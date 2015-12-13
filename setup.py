from os import environ, getcwd, mkdir, remove ,system
from lsb_release import get_lsb_information

class NginX():
	"""This class will define several methods which will interact with NginX."""
	
	def add_key(self):
		#This method will add NginX signing key to the apt program keyring.
		system("wget http://nginx.org/keys/nginx_signing.key")
		system("sudo apt-key add nginx_signing.key")

	def add_repo(self):
		#This method will add stable NginX ubuntu repo to /etc/apt/sources.list file.
		codename = get_codename()
		system("sudo add-apt-repository \"deb http://nginx.org/packages/ubuntu/ "+codename+" nginx\"")

	def install_nginx(self):
		#This method will install the latest stable version of NginX available to the added repo.
		system("sudo apt-get install nginx nginx-common nginx-full")

class MariaDB():
	"""This class will define several methods which will interact with MariaDB"""

	def add_key(self):
		#This method will add MariaDB v10.1 public key to the apt program keyring.
		system("sudo apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xcbcb082a1bb943db")

	def add_repo(self):
		#This method will add MariaDB v10.1 ubuntu repo to /etc/apt/sources.list file.
		codename = get_codename()
		system("sudo add-apt-repository \"deb [arch=amd64,i386] http://mirror.jmu.edu/pub/mariadb/repo/10.1/ubuntu "+codename+" main\"")

	def install_mariadb(self):
		#This method will install MariaDB v10.1.
		system("sudo apt-get install mariadb-server")

class PHP():
	"""This class will define several methods which will interact with PHP."""
	
	def add_repo(self):
		#This method will add PHP5 ubuntu repo with public key to /etc/apt/sources.list file.
		codename = get_codename()
		system("sudo add-apt-repository ppa:ondrej/php5-5.6")

	def install_php(self):
		#This method will install the latest stable version of PHP available to the added repo.
		system("sudo apt-get install php5 php5-fpm php5-mysql")


def get_codename():
	#This function will get the codename of running Ubuntu
	info = get_lsb_information()
	
	return info ['CODENAME']

def update_package_lists():
	#This function will downloads the package lists from the repositories and "updates" them to get information on the newest versions of packages and their dependencies.
	system("sudo apt-get update")

def main():
	#Defining the main function regarding Easy_LEMP
	system("sudo apt-get install software-properties-common")
	home_directory = environ['HOME']
	current_working_directory = getcwd()
	#Tyring to create a /home/username/public_html folder.
	try:
		mkdir(home_directory+"/public_html")
	except FileExistsError:
		print("The file \'"+home_directory+"/public_html\' already exists.")

	#Installing NginX, MariaDB, PHP with regarding Class and methods
	nginx = NginX()
	mariadb = MariaDB()
	php = PHP()
	nginx.add_key()
	nginx.add_repo()
	mariadb.add_key()
	mariadb.add_repo()
	php.add_repo()
	update_package_lists()
	nginx.install_nginx()
	mariadb.install_mariadb()
	php.install_php()

	#Editing /etc/nginx/nginx.conf file.
	system("sudo rm -f /etc/nginx/nginx.conf")
	system("sudo cp "+current_working_directory+"/nginx/nginx.conf /etc/nginx/nginx.conf")

	#Editing /etc/nginx/sites-available/default file.
	system("sudo rm -f /etc/nginx/sites-available/default")
	system("cp "+current_working_directory+"/nginx/default "+current_working_directory+"/nginx/default.txt")
	with open(current_working_directory+"/nginx/default.txt","r") as file:
		contents = file.read()
	with open(current_working_directory+"/nginx/default.txt","w") as file:
		if "/home/username" in contents:
			final_contents = contents.replace("/home/username",home_directory)
		else:
			final_contents = contents
		file.write(final_contents)
	system("sudo mv "+current_working_directory+"/nginx/default.txt /etc/nginx/sites-available/default")

	#Editing /etc/php5/fpm/php.ini file.
	system("sudo rm -f /etc/php5/fpm/php.ini")
	system("sudo cp "+current_working_directory+"/php/php.ini /etc/php5/fpm/php.ini")

	#Editing /etc/php5/fpm/pool.d/www.conf file.
	system("sudo rm -f /etc/php5/fpm/pool.d/www.conf")
	system("sudo cp "+current_working_directory+"/php/www.conf /etc/php5/fpm/pool.d/www.conf")

	#Configuring MariaDB
	system("sudo mysql_secure_installation")

	#Installing phpMyAdmin
	system("sudo apt-get install phpmyadmin")
	system("sudo ln -s /usr/share/phpmyadmin/ "+home_directory+"/public_html")

	#Restarting NginX, MariaDB, PHP
	system("sudo service nginx restart")
	system("sudo service mysql restart")
	system("sudo service php5-fpm restart")

if __name__ == "__main__":
	main()