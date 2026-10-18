import pymysql

# Corregido de install_as_mysql a install_as_MySQLdb
pymysql.install_as_MySQLdb()

from django.db.backends.mysql.base import DatabaseWrapper

# Omitir la comprobación estricta de la versión de MariaDB (para aceptar 10.4.32)
def check_database_version_supported(self):
    pass

DatabaseWrapper.check_database_version_supported = check_database_version_supported