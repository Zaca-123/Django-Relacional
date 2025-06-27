# 🛠️ Django-Relacional

Proyecto académico para la UTN Villa María. La aplicación demuestra cómo integrar **Django** con **PostgreSQL** utilizando **Docker** y contenedores.

---

## 📦 Herramientas
 ![image](https://github.com/user-attachments/assets/dcd99a1a-c00c-48d3-b46b-9455f92c24c9) ![image](https://github.com/user-attachments/assets/f85094c8-c004-49ac-b48e-850d318ad10a) ![image](https://github.com/user-attachments/assets/c8d94dac-8ce0-44b7-bde0-fc10b9f20ff2) ![image](https://github.com/user-attachments/assets/b3552499-8561-4817-ac4f-140735e872e9)

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- Python 3.11 (opcional para desarrollo local sin Docker)
- [PostgreSQL](https://www.postgresql.org/download/)

---

## 🚀 Instalación y ejecución

1. Clonar el repositorio:

```bash
git clone https://github.com/Zaca-123/Django-Relacional.git
cd Django-Relacional
````

2. Levantar los contenedores:
```bash
docker-compose up --build
```

3. Acceder a la aplicación:
```aduino
http://localhost:8000/
```

## 🧪 Migraciones

Para aplicar las migraciones de modelos a la base de datos:

````bash
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
````

## 👤 Acceso al Admin de Django

Crear superusuario:

````bash
docker-compose exec web python manage.py createsuperuser
````
Iniciar sesión:

````bash
http://localhost:8000/admin/
````

## 📂 Estructura del proyecto

Django-Relacional/
├── src/                # Código fuente de Django
├── venv/               # Entorno virtual (opcional)
├── docker-compose.yml  # Configuración de contenedores
├── Dockerfile          # Imagen personalizada de Django
└── requirements.txt    # Dependencias de Python

## 📚 Licencia
Este proyecto fue desarrollado como actividad académica y no cuenta con una licencia específica.
