# Propuesta técnica al cliente — versión 3 separada

**Cliente académico:** Andes Ingeniería y Servicios SpA  
**Proyecto:** red corporativa para matriz en Santiago y sucursal en Valparaíso  
**Fecha:** 1 de noviembre de 2026  
**Estado:** propuesta de avance, **sin precio cerrado ni promesa de operación aún validada**.

## 1. Necesidad del cliente

Se busca conectar las dos sedes de forma segura, separar seis departamentos, disponer de servicios institucionales, controlar accesos, proteger el tráfico entre sedes y facilitar crecimiento y administración. Los supuestos de dotación **85 usuarios en matriz y 38 en sucursal** provienen de un documento auxiliar de requisitos; el cliente debe confirmarlos antes de cerrar capacidad y presupuesto.

## 2. Solución que ya tiene base en Cisco

Theri construyó en Packet Tracer una topología que contempla **dos routers de borde, dos routers de proveedor, cuatro switches multicapa (dos por sede), cinco switches de acceso, un switch de DMZ, siete servidores de laboratorio y equipamiento de usuario/telefonía/IoT**, con **51 dispositivos y 60 enlaces en total**. Esta es la **fuente primaria** de la propuesta, registrada en `TRABAJO REDES-backup.pkt`, no una arquitectura imaginada desde documentos.

La implementación guardada incluye, entre otros componentes:

- VLAN de Gerencia, Finanzas, RR. HH., TI, Ventas y Operaciones, además de Voz, IoT y Gestión; DMZ en matriz.
- Direccionamiento segmentado y gateways de alta disponibilidad mediante HSRP, dos núcleos por sede y enlaces de acceso duplicados.
- Configuración OSPF para el routing interno y DHCP para redes de usuario.
- Configuración IPsec para el tráfico entre sedes, NAT/PAT hacia Internet y publicación web selectiva.
- Controles de SSH, port-security, PortFast, BPDU Guard y administración en switches.

**Límite contractual:** lo anterior se comprobó leyendo la configuración *guardada*; todavía no se ha presenciado una demostración de todo el tráfico, recuperación ante fallas o negociación VPN. La propuesta describe la solución **en construcción**, no una red certificada lista para producción.

## 3. Trabajo necesario para alcanzar los criterios de aceptación

| Prioridad | Entregable al cliente y a la asignatura | Situación al corte |
|---|---|---|
| Crítica | Publicación HTTP limitada a la DMZ y con IP coherente | NAT guardado hacia `10.10.1.146`; servidor web en `.147/24`, con DMZ `/28`; debe corregirse en copia |
| Crítica | Servicios HTTP, DNS, NTP, Email, Syslog y AAA probados | Siete servidores presentes; seis sin IPv4 fija guardada; DNS/AAA deshabilitados |
| Alta | Acceso inalámbrico por departamento con WPA2/3 | No hay puntos de acceso en el `.pkt`; falta implementar o documentar dispensa del profesor |
| Alta | VPN IPsec entre sedes, NAT/PAT y OSPF probados | Comandos guardados; faltan SA, contadores, tablas de rutas y evidencias de tráfico |
| Alta | Continuidad, segmentación y controles de seguridad probados | HSRP/EtherChannel/ACL configurados; faltan resultados observados; la DMZ tiene un solo uplink |
| Media | Telefonía IP e IoT demostrados | Cinco IP Phone y dos MCU; los dos objetos «Termostato» son PC; llamadas y sensores sin validar |
| Obligatoria | Presupuesto y documentación final | Pendientes cotizaciones verificadas, planilla, PDF y defensa de 15 minutos |

## 4. Presupuesto y contratación

La PPTX original indicaba **$20–$30 millones CLP con IVA**; **Christopher confirma permiso posterior del profesor para presupuestar hasta $35 millones con IVA**. Se requieren **al menos dos cotizaciones chilenas por ítem relevante**. Se presupuestarán equipos empresariales actuales equivalentes a las funciones verificadas, no necesariamente los modelos antiguos del simulador. Se separarán servicios ISP de compras del cliente; se estudiará virtualizar los siete roles de servidor y dimensionar PCs/AP/teléfonos con la dotación real. Las categorías y cantidades de partida se detallan en [BASE_PRESUPUESTO_DESDE_PKT.md](BASE_PRESUPUESTO_DESDE_PKT.md).

**No se propone una cifra estimada sin ofertas ni se afirma que esté adjudicada una marca.** El costo total se calculará cuando se tengan las cotizaciones, licencias, instalación, respaldo eléctrico, cableado y soporte.

## 5. Aceptación y entrega

Antes de considerar instalado el proyecto académico se necesitan, como mínimo:

1. Un archivo `.pkt` definitivo derivado **en una copia** del de Theri, sin sobrescribir el original.
2. Capturas repetibles de VLAN/VLSM, OSPF, HSRP, DHCP, VPN IPsec, NAT/DMZ, controles de acceso, servidores, telefonía, IoT y WLAN o dispensa docente.
3. Registro de pruebas positivas y negativas, incluida caída de enlace y acceso indebido bloqueado.
4. Planilla de presupuesto con fuentes chilenas comparables y total con IVA dentro de la pauta.
5. Informe técnico en PDF y defensa grupal de 15 minutos coherentes con las pruebas.

Esta propuesta y su memoria técnica son **documentos nuevos de versión 3**. Reconocen la implementación de **Theri** como trabajo principal y utilizan los apuntes de **Nico** solamente como apoyo cuando coinciden con la red real. Ningún archivo original se modifica.
