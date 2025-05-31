# crm-client-manager
Full-stack CRM web application for managing client data with authentication, filtering and statistics.

📂 Paso 1: Abre la carpeta del proyecto
Desde VS Code:

Ve a Archivo > Abrir carpeta.

Abre: C:\Users\34672\Desktop\PORTFOLIO\Full-stack CRM

🐍 Paso 2: Activa el entorno virtual
Abre la terminal (Ctrl + ñ) y ejecuta:

powershell
Copiar
Editar
.\venv\Scripts\Activate.ps1
🛑 Si te da error de permisos, ejecuta una sola vez en tu vida este comando como administrador de PowerShell:

powershell
Copiar
Editar
Set-ExecutionPolicy RemoteSigned
🧪 Paso 3: Mueve a la carpeta backend
bash
Copiar
Editar
cd backend
🚀 Paso 4: Arranca el servidor
bash
Copiar
Editar
uvicorn app.main:app --reload
📍 Accede a la API en:
http://127.0.0.1:8000/docs