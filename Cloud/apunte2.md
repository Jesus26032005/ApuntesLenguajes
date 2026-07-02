# COMPUTACION TRADICIONAL VS COMPUTO EN LA NUBE

## Computacion tradicional

Traditional computing is a computing model that enables data storage, access, and management through the use of physical hardware and software within a network infrastructure, typically located on-premises.

### Ventajas

- Control total sobre la infraestructura y los datos, lo que puede ser importante para organizaciones con requisitos de seguridad estrictos o regulaciones específicas.
- Seguridad: Es más fácil proteger los datos y la infraestructura de TI, ya que se encuentran en las instalaciones de la organización.
- Puede ser viable si los datos deben estar en sus propias instalaciones

### Desventajas

- Acceso limitado a los datos y recursos, lo que puede dificultar la colaboración y el trabajo remoto.
- Dificultad para escalar recursos rápidamente en respuesta a cambios en la demanda, lo que puede resultar en costos adicionales y tiempos de inactividad.
- Requiere una inversión inicial significativa en hardware, software y personal de TI para mantener la infraestructura.
- Mantenimiento y actualización de la infraestructura pueden ser costosos y requerir tiempo, lo que hace que sea difícil mantenerse al día con las últimas tecnologías y tendencias.
- Ineficieniente dado que cada usuario debe comprar y mantener su propio hardware y software, lo que puede resultar en costos adicionales y desperdicio de recursos.

Introducción a los Cloud Data Warehouses
Los Cloud Data Warehouses (almacenes de datos en la nube) son soluciones de almacenamiento a gran escala alojadas en servidores remotos. Surgen para resolver las limitaciones de las bases de datos tradicionales ante la analítica moderna.

## ¿Qué es un Cloud Data Warehouse?

Es un sistema que permite recolectar, almacenar, integrar y analizar datos de diversas fuentes en un solo lugar.

• Analogía: Como un gran almacén que organiza contenedores de diferentes orígenes.

### Ventajas Principales

- Totalmente Administrado: El proveedor se encarga del mantenimiento y la infraestructura. El usuario solo se enfoca en obtener insights.
- Salva tiempo, dinero y recursos al eliminar la necesidad de gestionar hardware, software y actualizaciones.
- Mayor Uptime: Garantizan que los sistemas estén operativos casi el 100% del tiempo, permitiendo escalar según la demanda.
- Integración de Datos: Reúne datos de fuentes dispersas (ventas, listas de correo, sitios web) en un solo lugar.
- Analítica en Tiempo Real: Acceso rápido a la información más reciente para una toma de decisiones competitiva.
- Havilidad para escalar y soportar la demanda de datos en crecimiento sin preocuparse por la infraestructura subyacente.
- Integracion separada de los datos.
- Reportes y consultas personalizadas sin afectar el rendimiento del negocio actual.

### IA y Machine Learning

Permiten aplicar modelos predictivos para mejorar la eficiencia.

• Ejemplo: Google utilizó ML para predecir la demanda en sus cafeterías, analizando más de 30 factores para reducir desperdicios.

### Reportes Personalizados

El análisis se realiza en servidores separados de las operaciones diarias, lo que permite consultar datos históricos sin afectar el rendimiento del negocio actual.

## Resumen

Benet Cloud data warehouses Traditional data warehouses
Cost Save time and resources since
servers don’t need to be hosted
locally
Require resources to implement,
maintain, and optimize servers
Scalability and
exibility
Can be adjusted to match changing
data needs at any time, oen
through autoscaling
Require additional physical
computer resources any time a
change is requested
Uptime Have more uptime than traditional
server warehouses, meaning the
system is operational more oen
Have less uptime and are only
operational when the server is
running
Accessibility Data is more accessible to users in
dierent locations working at
dierent times, meaning both
analysts and stakeholders can
access the data they need when they
need it
Accessing data on-site involves
more security mechanisms, limiting
how and when data can be accessed

# 🔍 Conociendo Google BigQuery

**BigQuery** es el potente almacén de datos (Data Warehouse) en la nube de Google, diseñado para almacenar, consultar y analizar enormes cantidades de información de forma rápida utilizando la infraestructura de Google.

## ¿Por qué es importante?

El almacenamiento eficiente permite un acceso rápido a la información, lo que se traduce en nuevas ideas, *insights* (conocimientos) y, lo más importante, una **toma de decisiones basada en datos**.

## Características Principales

**Uso de SQL:** Funciona con SQL (*Structured Query Language*), el lenguaje estándar para comunicarse con bases de datos. Permite buscar información en bases de datos masivas de manera increíblemente rápida.
**Migración Sencilla:** Facilita la migración de almacenes de datos existentes desde otros proveedores de servicios en la nube.
- Parámetro de Prueba (*Dry-run*):** * Permite verificar la lógica y el plan de la consulta antes de ejecutarla (como un *swing* de práctica en el golf). 
- Te indica la cantidad de *bytes* que procesará la consulta, lo que ayuda a **estimar el costo** antes de gastar recursos.
* **Consultas Programadas:** Permite automatizar la actualización de los datos (cada hora, día o semana) para mantener las tablas al día y entregar métricas oportunas a los *stakeholders*.
* 1**Múltiples Fuentes:** Puede almacenar y ejecutar consultas de datos provenientes de servidores, sensores y otros dispositivos.
* **Machine Learning Integrado:** Cuenta con capacidades de aprendizaje automático (*Machine Learning*) directamente en su interfaz.

## Flujo de Trabajo y Casos de Uso

Como analista de datos en la nube, BigQuery es una herramienta esencial para el trabajo diario:

1. **Conexión de Datos:** Permite acceder a una multitud de fuentes de datos diferentes.
2. **Transformación:** Usa SQL para unir (*join*) conjuntos de datos y transformarlos.
3. **Generación de Resultados:** Ayuda a crear tablas y gráficos que responden a preguntas de negocio.
4. **Escalabilidad (Autoservicio):** Cuando se encuentra una respuesta útil y recurrente, se puede escalar construyendo reportes y *dashboards* de autoservicio para que los usuarios puedan consultar la información por sí mismos cuando la necesiten.

## Integración

El resultado de tu trabajo en BigQuery no se queda aislado; se integra sin problemas con:
* Herramientas típicas de Inteligencia de Negocios (BI Tools).
* Hojas de cálculo (Spreadsheets).

> **Resumen:** BigQuery actúa como un puente entre los datos existentes y los problemas que las empresas intentan resolver. Su interfaz amigable, integración fluida y el uso de SQL lo convierten en una herramienta invaluable para cualquier carrera en datos en la nube.