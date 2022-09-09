# Sprint8

Instalacion del Virtual Environment

  - python -m venv env
  - env/Scripts/activate

Instalar requirements

  - pip install -r requirements.txt

Iniciar el servidor

  -cd sprint7
  -python manage.py runserver


USUARIOS OCUPADOS
Para probar el registro de nuevos usuarios, no utilizar los siguientes clientes, ya que fueron usados durante el desarrollo.
customer_id = 5, 6, 13, 21, 24, 40

EMPLEADOS OCUPADOS
employee_id = 1, 2, 3, 4, 7


Una vez logeado con el empleado/cliente, dirigirse a /api/
  
   Accesibles para el cliente:
   -api/client_data = informacion del cliente logeado
   -api/account_data = informacion de la cuenta del cliente logeado
   -api/client_loans = informacion de los prestamos solicitados del cliente logeado
   
   Accesibles para empleados:
   -api/loans_by_branch/<id> = informacion de los prestamos otorgados por la sucursal <id>
   -api/all_loans = informacion de todos los prestamos por cliente. Se puede eliminar, updatear y agregar nuevos
  
   Endpoint:
   -api/branchs/ = endpoint con la lista de todas las sucursales y sus nombres
