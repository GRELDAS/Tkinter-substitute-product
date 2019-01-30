# Pur Beurre
This program was designed to work offline offline once the update of the database is done. Get many practical and nutritional information on many consumer products! Pure Butter offers you to discover a practical tool to easily find many substitutions products.

# Install with Ubuntu 18.04 LTS

(If you dont have Python)
sudo apt install python3-venv

1   : Create new virtual environment with venv
1-1 : python3 -m venv venv
1-2 : source venv/bin/activate

You can use pip3 like this :

2   : Install libraries
2-1 : Install mysql (pip3 install mysql)
2-2 : Install mysql-connector (pip3 install mysql-connector)
2-3 : Install SQLAlchemy (pip3 install sqlalchemy)
2-4 : Install requests (pip3 install requests)
2-5 : Install pillow (PIL) (pip3 install pillow)

(!) You can use Oracle, PostgreSQL ... because this program using SQLAlchemy ORM
For more information : https://www.sqlalchemy.org/

3   : Start MySQL Server
3-1 : sudo service mysql start

4   : Start the programm (python3 main.py)

# Main features
- Multiple users
- Updating the customizable database
- Product search by name
- Product search by categories
- Search products substitutes
- Product backup

# Authors
** Guillaume Sadler ** - Python student in OpenClassrooms

Friendship to :
** Timothé Guiched ** - Python mentor without whom nothing would have been possible

# Copyright
This project is licensed under the GNU License
