# anomaly_detection
Arquitectura para un microservicio de deteccion de anomalias. Incluye un contenedor que corre un servicio de base de datos con el historico de precios y un microservicio desarrollado en django que usa el modelo de isolation forest para realizar la deteccion de anomalias sobre un nuevo precio basandose en el historico de ese precio
