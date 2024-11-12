import subprocess

# Lista de archivos a ejecutar
scripts = [
    "CrearTabla_t_students.py",
    "CrearTabla_t_rockies.py",
    "CrearTabla_t_purchasable.py",
    "CrearTabla_t_activities.py",
    "CrearTabla_t_rewards.py",
    "CrearTabla_t_access_tokens.py"
]

# Ejecutar cada script
for script in scripts:
    print(f"Running {script}...")
    try:
        result = subprocess.run(["python", script], capture_output=True, text=True)
        print(result.stdout)  # Mostrar salida estándar
        if result.stderr:
            print(f"Error in {script}:\n{result.stderr}")  # Mostrar error si existe
    except Exception as e:
        print(f"Failed to run {script}: {e}")
