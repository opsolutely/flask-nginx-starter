# flask-nginx-starter
 A starter repo for a flask + nginx Docker container

Setting up local installations on a Mac
=========================
1.  You'll need a keys.sh file in the local_files directory.
2.  PostgresApp needs to be installed on your computer
3.  brew install postgres
4.  brew install bcrypt
5.  brew install openssl
6.  If you don't have python virtualenvs setup, follow the instructions here (starting at installing virtualenv): https://newcoder.io/pyladiessf
7.  mkvirtualenv deploy
8.  pip install -r ./local_files/requirements.txt

Creating a Local Database
=========================
1.  To create a local database, type: psql -h localhost
2.  CREATE DATABASE [db_name];

Running the app locally
=========================
1.  Run: ./run_local.sh
2.  Go to localhost:7070 to see your home page!
3.  Application logs can be accessed with: tail -f ./application.log
