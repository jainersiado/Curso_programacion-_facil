import subprocess
import getpass


with open('C:/american_rider.sql', 'w') as out:
    subprocess.Popen(f'mysqldump --user=root --password={getpass.getpass()} --databases american_rider', shell=True, stdout=out)


    # PARA QUE SE PUEDA EJECUTAR DEBE SER EN LA RUTA DE MYSQLDUMP ( C:\Program Files\MySQL\MySQL Workbench 8.0\ )