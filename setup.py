from os import environ, remove ,system
from lsb_release import get_lsb_information
from shutil import copy

class NginX():
	"""This class will define several methods which will interact with NginX."""
	
	def add_key():
		#This method will add NginX signing key to the apt program keyring.
		os.system("wget http://nginx.org/keys/nginx_signing.key")
		return os.system("sudo apt-key add nginx_signing.key")

	def add_repo():
		#This method will add stable NginX ubuntu repo to /etc/apt/sources.list file.
		codename = get_codename()
		os.system("sudo add-apt-repository \"deb http://nginx.org/packages/ubuntu/",codename,"nginx\"")

	def install_nginx():
		#This method will install the latest stable version of NginX available to the added repo.
		os.system("sudo apt-get install nginx")

class MariaDB():
	"""This class will define several methods which will interact with MariaDB"""

	def add_key():
		#This method will add MariaDB v10.1 public key to the apt program keyring.
		os.system("sudo apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xcbcb082a1bb943db")

	def add_repo():
		#This method will add MariaDB v10.1 ubuntu repo to /etc/apt/sources.list file.
		codename = get_codename()
		os.system("sudo add-apt-repository \"deb [arch=amd64,i386] http://mirror.jmu.edu/pub/mariadb/repo/10.1/ubuntu",codename,"main\"")

	def install_mariadb():
		#This method will install MariaDB v10.1.
		os.system("sudo apt-get install mariadb-server mariadb-client")

class PHP():
	"""This class will define several methods which will interact with PHP."""
	
	def add_repo():
		#This method will add PHP5 ubuntu repo with public key to /etc/apt/sources.list file.
		codename = get_codename()
		os.system("sudo add-apt-repository ppa:ondrej/php5-5.6")

	def install_php():
		#This method will install the latest stable version of PHP available to the added repo.
		os.system("sudo apt-get install php5 php5-fpm php5-mysql")


def get_codename():
	#This function will get the codename of running Ubuntu
	info = lsb_release.get_lsb_information()
	return info ['CODENAME']

def update_package_lists():
	#This function will downloads the package lists from the repositories and "updates" them to get information on the newest versions of packages and their dependencies.
	os.system("sudo apt-get update")

def main():
	#Defining the main function regarding Easy_LEMP
	os.system("sudo apt-get install software-properties-common")
	home_directory = os.environ['HOME']
	os.mkdir(home_directory+"/public_html")

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
	os.remove("/etc/nginx/nginx.conf")
	shutil.copy("/nginx/nginx.conf","/etc/nginx/nginx.conf")

	#Editing /etc/nginx/sites-available/default file.
	os.remove("/etc/nginx/sites-available/default")
	shutil.copy("/nginx/default","/etc/nginx/sites-available/default")
	with open("/nginx/default","rw") as file:
		contents = file.read()
		final_contents = contents.replace("/home/username",home_directory)
		file.write(final_contents)

	#Editing /etc/php5/fpm/php.ini file.
	os.remove("/etc/php5/fpm/php.ini")
	shutil.copy("/php/php.ini","/etc/php5/fpm/php.ini")

	#Editing /etc/php5/fpm/pool.d/www.conf file.
	os.remove("/etc/php5/fpm/pool.d/www.conf")
	shutil.copy("/php/www.conf","/etc/php5/fpm/pool.d/www.conf")

	#Configuring MariaDB
	os.system("sudo mysql_secure_installation")

	#Installing phpMyAdmin
	os.system("sudo apt-get install phpmyadmin")
	os.system("sudo ln -s /usr/share/phpmyadmin/ "+home_directory+"/public_html")

	#Restarting NginX, MariaDB, PHP
	os.system("sudo service nginx restart")
	os.system("sudo service mysql restart")
	os.system("sudo service php5-fpm restart")

if __name__ == "__main__":
	main()