from google.cloud import storage
import joblib
import gcsfs


#///////////// CONEXION CON GCP /////////////

# Crea una instancia del cliente de almacenamiento
storage_client = storage.Client() 

# Especifica el nombre de tu bucket
bucket_name = 'modelo_ml'

# Especifica el nombre del archivo en el bucket
file_name = 'all_models.joblib'

# Obtiene una referencia al bucket
bucket = storage_client.get_bucket(bucket_name)

# Construye la URL del archivo en el bucket
file_url = f"gs://{bucket_name}/{file_name}"

# Crea un objeto gcsfs para leer el archivo directamente desde el bucket
fs = gcsfs.GCSFileSystem(project='optimum-reactor-414719')

# Lee el archivo utilizando pandas
with fs.open(file_url) as f:
    models_by_branch = joblib.load(f)
    
#///////////// FIN CONEXION CON GCP /////////////