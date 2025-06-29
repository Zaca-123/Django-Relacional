## 🛠️ Django-Relacional

Proyecto académico para el práctico de Bases de Datos (Ingeniería en Sistemas, UTN FRVM).  
Basado en el trabajo del profe [fábrica de pastas](https://github.com/pindutn/fabrica_pastas/tree/main)
 y adaptado para desplegar un entorno Django profesional con Docker, utilizando PostgreSQL y modelos relacionales.

---

## 🚀 Puesta en marcha rápida

### 1. Clona el repositorio
```bash
git clone https://github.com/Zaca-123/Django-Relacional.git
cd Django-Relacional
```

### 2. Genera la estructura del proyecto y levanta el backend
```bash
docker compose run --rm generate
sudo chown $USER:$USER -R .
docker compose up -d backend
```

### 3. Aplica migraciones de la base de datos
```bash
docker compose run --rm manage makemigrations
docker compose run --rm manage migrate
```

### 4. Crea un superusuario para el admin
```bash
docker compose run --rm manage createsuperuser
```

### 5. Carga datos iniciales (fixtures)
```bash
docker compose run --rm manage loaddata initial_data
```

👉 Ahora accede a [http://localhost:8000/admin](http://localhost:8000/admin) y gestiona la app con el usuario creado.

---

## 📝 Estructura del Proyecto

```
Django-Relacional/
│
├── docker-compose.yml
├── Dockerfile
├── .env.db
├── requirements.txt
├── src/
│   ├── app/            # Proyecto Django base
│   └── pastas/         # Aplicación principal
│       ├── models.py
│       ├── admin.py
│       ├── fixtures/
│           └── initial_data.json
├── LICENSE
└── README.md
```

---

## ⚙️ Herramientas utilizadas 
![image](https://github.com/user-attachments/assets/659d4cc4-71c6-44b4-8f4c-a18d4a81f09e) ![image](https://github.com/user-attachments/assets/6bf796e5-6c64-492f-b3ca-8bc69fa3a507) ![image](https://github.com/user-attachments/assets/6f4baccf-f706-4c5e-b996-f79794b1be2d) ![image](https://github.com/user-attachments/assets/f8ff59ed-8bba-4c93-af34-d5379c79fc0c)


## 🛠️ Comandos útiles

- Aplicar migraciones:
  ```bash
  docker compose run manage makemigrations
  docker compose run manage migrate
  ```
- Crear superusuario:
  ```bash
  docker compose run --rm manage createsuperuser
  ```
- Iniciar backend:
  ```bash
  docker compose up -d backend
  ```
- Ver logs:
  ```bash
  docker compose logs -f
  ```
- Cargar datos iniciales:
  ```bash
  docker compose run --rm manage loaddata initial_data
  ```
- Eliminar todo:
  ```bash
  docker compose down -v --remove-orphans --rmi all
  docker system prune -a
  ```
- Corregir permisos:
  ```bash
  sudo chown $USER:$USER -R .
  ```

---

## 🤝 Créditos y Licencia

- Mantenido por: Grupo 12
- Basado en el repositorio: [fábrica de pastas](https://github.com/pindutn/fabrica_pastas/tree/main)

> El código se entrega "tal cual", sin garantías. Si te es útil, considera dar feedback.

---
