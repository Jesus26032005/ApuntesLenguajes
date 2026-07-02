# ☁️ Gestión de Costos en la Nube (Cloud Costs)

Administrar los costos en la nube es como hacer una lista para el supermercado: debes saber exactamente qué recursos necesitas y en qué cantidad para evitar gastos excesivos y desperdicios.

Los costos en la nube se ven afectados principalmente por tres factores: **aprovisionamiento de recursos, almacenamiento y ejecución de consultas**.

## 1. Aprovisionamiento de Recursos (Resource Provisioning)

Es el proceso donde el usuario selecciona los recursos de hardware y software adecuados, y el proveedor de la nube los configura y administra durante su uso. Existen tres modelos de entrega:

* **Aprovisionamiento Anticipado (Advanced Provisioning):** Se firma un acuerdo formal con el proveedor. Se paga un precio fijo o una factura mensual, y el proveedor entrega exactamente los recursos acordados.
* **Aprovisionamiento Dinámico (Dynamic Provisioning):** Los recursos se ajustan automáticamente según las necesidades cambiantes del usuario (escalabilidad). Solo se cobra por lo que se utiliza.
* **Auto-aprovisionamiento (Self-provisioning / Cloud Self-service):** El usuario compra los recursos a través de un portal web, y estos quedan disponibles casi de inmediato (en minutos u horas).

> **Nota sobre Pagos:** Las tarifas para estos modelos pueden ser *fijas*, de *pago por uso (pay-as-you-go)* o de *compra instantánea*.

## 2. Costos de Almacenamiento (Storage Costs)

El almacenamiento es uno de los tres gastos más altos en la nube. Estos costos varían según tres elementos:

* **Almacenamiento de Datos (Data Storage):** La cantidad de datos guardados (generalmente en *Buckets*). El costo cambia según la ubicación geográfica y la **"clase"** de almacenamiento.
  * *Ejemplo:* La clase *Coldline* es ideal para datos que se leen una vez al trimestre, mientras que la clase *Archive* (para copias de seguridad) es la opción más barata.
* **Procesamiento de Datos (Data Processing):** El paso donde los datos crudos se limpian y organizan. Procesar más datos o hacerlo más rápido requiere soluciones de almacenamiento más avanzadas y costosas.
* **Uso de Red (Network Use):** Se refiere a la cantidad de datos que se leen o se mueven entre diferentes *buckets* de almacenamiento.

## 3. Costos por Consultas (Running Queries)

🚨 **Regla de oro:** La mayoría de los proveedores cobran por la cantidad de datos **procesados** al ejecutar la consulta, NO por la cantidad de datos que te devuelve el resultado.

### Modelos de Precios en Google BigQuery

BigQuery ofrece dos formas de pagar por las consultas:

* **Precios Bajo Demanda (On-demand Pricing):** Se cobra en función de la cantidad de datos (en bytes) que procesa cada consulta. Es ideal si tus necesidades de computación y almacenamiento fluctúan constantemente.
* **Precios por Capacidad (Capacity Pricing):** Se basa en el poder de cómputo utilizado a lo largo del tiempo, medido en unidades de procesamiento virtual (llamadas *slots*). Es ideal si buscas tener costos predecibles y controlables mes a mes.

---

> **El Valor del Analista:** Como profesional de datos en la nube, entender estos modelos te permite ayudar a tu empresa a optimizar recursos, mejorar procesos y, en última instancia, cuidar el presupuesto final.
