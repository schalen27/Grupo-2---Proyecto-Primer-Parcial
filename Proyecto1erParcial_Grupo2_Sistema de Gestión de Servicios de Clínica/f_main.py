# Grupo 2 - Sistema de Gestión de Servicios de Clínica
#Integrantes:
# 1. Bermeo Cevallos Jorge Alejandro
# 2. Caceres Medina Bolivar Santiago
# 3. Chalen Ochoa Shuska Akyra
# 4. Rivera Valdiviezo Ashley Daniela
# 5. Silva Parrales Jipson Alexander

from d_paciente import Paciente
from b_consulta_general import ConsultaGeneral
from c_examen_laboratorio import ExamenLaboratorio
from e_gestor_clinica import GestorClinica

#Crear pacientes
paciente1 = Paciente(
    cedula= '0963587421',
    nombre= 'Jorge Bermeo',
    edad= 26,
    telefono= '097 977 9089',
    genero= 'Masculino'
)

paciente2 = Paciente(
    cedula='0926512365',
    nombre= 'Bolivar Cáceres',
    edad= 20,
    telefono= '098 912 6772',
    genero= 'Masculino'
)

paciente3 = Paciente(
    cedula='0952850105',
    nombre= 'Akyra Chalen',
    edad= 21,
    telefono= '098 254 9195',
    genero= 'Femenino'
)

paciente4 = Paciente(
    cedula= '0912584762',
    nombre= 'Ashley Rivera',
    edad= 21,
    telefono= '093 947 6177',
    genero= 'Femenino'
)

paciente5 = Paciente(
    cedula= '0937682514',
    nombre= 'Jipson Silva',
    edad= 20,
    telefono= '099 774 8130',
    genero= 'Masculino'
)

# Crear consultas generales
consulta1 = ConsultaGeneral(
    codigo='C001',
    nombre_servicio='Consulta Médica',
    costo_base= 30,
    paciente= paciente1,
    especialidad='Cardiología',
    duracion= 45,
    nivel_urgencia= 'Alta'
)

consulta2 = ConsultaGeneral(
    codigo= 'C002',
    nombre_servicio= 'Consulta Médica',
    costo_base= 25,
    paciente= paciente2,
    especialidad= 'Traumatología',
    duracion= 30,
    nivel_urgencia= 'Baja'
)
# Crear exámenes de laboratorio
examen1 = ExamenLaboratorio(
    codigo= 'E001',
    nombre_servicio= 'Examen de Laboratorio',
    costo_base= 20,
    paciente= paciente3,
    tipo_analisis= 'Sangre',
    requiere_urgencia= 'Alta',
    numero_muestras= 1
)

examen2 = ExamenLaboratorio(
    codigo= 'E002',
    nombre_servicio= 'Examen de Laboratorio',
    costo_base= 15 ,
    paciente= paciente4,
    tipo_analisis= 'Sangre',
    requiere_urgencia= 'Baja',
    numero_muestras= 1
)

examen3 = ExamenLaboratorio(
    codigo= 'E003',
    nombre_servicio= 'Examen de Laboratorio',
    costo_base= 10,
    paciente= paciente5,
    tipo_analisis= 'Orina',
    requiere_urgencia= 'Alta',
    numero_muestras= 2
)

# Crear gestor
gestor = GestorClinica()

# Registrar pacientes
gestor.registrar_paciente(paciente1)
gestor.registrar_paciente(paciente2)
gestor.registrar_paciente(paciente3)
gestor.registrar_paciente(paciente4)
gestor.registrar_paciente(paciente5)

# Registrar servicios
gestor.agregar_servicio(consulta1)
gestor.agregar_servicio(consulta2)
gestor.agregar_servicio(examen1)
gestor.agregar_servicio(examen2)
gestor.agregar_servicio(examen3)

gestor.mostrar_pacientes()

gestor.mostrar_reporte()

print('\n┈┈┈┈┈┈┈┈┈┈┈ TOTAL GENERAL ┈┈┈┈┈┈┈┈┈┈┈')
print(f'Total a pagar por servicios: ${gestor.calcular_total_servicios():.2f}')