# Versión 3: informe técnico independiente

**Corte:** 1 de noviembre de 2026 · **Estado:** borrador técnico de avance, sujeto a validación y revisión del equipo. **Aclaración de autoría:** Christopher confirmó que Theri es quien armó el trabajo en Cisco Packet Tracer; Nico desarrolló la documentación de apoyo.

## Qué se creó

- [INFORME_TECNICO_V3_BORRADOR.md](INFORME_TECNICO_V3_BORRADOR.md): nueva memoria técnica **fundamentada en el `.pkt` de Theri**, los requisitos del cliente y la rúbrica oficial.
- [BASE_PRESUPUESTO_DESDE_PKT.md](BASE_PRESUPUESTO_DESDE_PKT.md): inventario de Cisco frente a partidas comerciales; sin precios ficticios, con tope docente actualizado de **$35M IVA incluido** informado por Christopher.
- [PROPUESTA_CLIENTE_V3_BORRADOR.md](PROPUESTA_CLIENTE_V3_BORRADOR.md): versión comercial para el cliente, con alcance, riesgos, criterios de aceptación y presupuesto aún sin cotizar.
- [01_revision_rubrica_v3](../01_revision_rubrica_v3/): carpeta hermana para ver qué está documentado, qué se ha comprobado y qué falta.

## Qué se tomó de los avances del grupo

1. **Cliente y enfoque comercial:** Andes Ingeniería y Servicios SpA, casa matriz en Santiago y sucursal en Valparaíso; origen `documentacion/01-requisitos-del-cliente.md`.
2. **Dispositivos y arquitectura:** **51 dispositivos y 60 enlaces efectivamente guardados** en el `.pkt` de Theri, con cuatro switches core L3, R-HQ/R-SUC, ISP1/ISP2, switches de acceso y DMZ.
3. **VLSM y VLAN:** numeración hallada en los core de Theri; el esquema distinto de `documentacion/03` se señala como histórico y no se copia como si estuviera implementado.
4. **Seguridad y servicios:** configuración guardada de IPsec, NAT/PAT, OSPF, HSRP v2, SSH, VTP transparent, port-security, PortFast, BPDU Guard y DHCP; los `.txt` de `Proyecto2_PT/` solo se citan como soporte, no como evidencia principal.
5. **Evaluación:** los diez criterios y pesos de `Proyectos Redes corporativas.pptx` del profesor. La PPTX fija **$20 a $30 millones con IVA**, pero Christopher confirma autorización posterior para llegar a **$35 millones con IVA**.

## Qué significa «trabajo original de Theri»

Christopher aclaró que **Theri realizó la implementación y el armado de la topología en Cisco Packet Tracer**. Por tanto, **su trabajo de base es la topología `.pkt`**, no un supuesto informe Word o PDF de su autoría. El conjunto `Proyecto2_PT/` ofrece comandos de configuración para contrastar con la simulación; la documentación de Nico se utiliza como explicación y soporte.

El archivo `packet-tracer/TRABAJO REDES-backup.pkt` **ya fue inspeccionado directamente en modo de solo lectura**, y su hash coincide con el archivo de GitHub. Se verificaron el inventario, los enlaces, los comandos almacenados y seis problemas concretos; el detalle está en [AUDITORIA_DIRECTA_PKT_THERI.md](../01_revision_rubrica_v3/AUDITORIA_DIRECTA_PKT_THERI.md). Para atribuirle un estado **operativo** sigue siendo obligatorio ejecutar el simulador y aportar capturas. La V3 es una **redacción derivada de la red de Theri**; no se atribuye a ella un informe textual cuya autoría no se ha identificado.

## Límites explícitos

- No se editó ningún archivo de `documentacion/`, `Proyecto2_PT/`, `packet-tracer/` ni de la raíz del proyecto.
- La presencia de comandos en un `.txt` **no prueba** que estén en el `.pkt` entregable. Se contrastaron los comandos almacenados de Theri; esto tampoco sustituye las pruebas operativas.
- Se registraron conflictos **verificados en el `.pkt`**: NAT HTTP a .146 vs servidor .147/24, seis servidores sin IP fija, DNS y AAA apagados, ausencia de AP, dos «termostatos» que son PC y un solo uplink de DMZ.
- No se han realizado simulaciones, pings, capturas, demostraciones de IPsec ni cotizaciones nuevas en esta tarea.
- No se reproducen contraseñas académicas ni claves compartidas presentes en las configuraciones del repositorio.
- El resultado es Markdown revisable en GitHub; al cerrar pruebas y anexos, deberá exportarse a PDF para la entrega del docente.

## Tareas para cerrar esta versión

1. Confirmar con Theri que `TRABAJO REDES-backup.pkt` es la versión definitiva; conservar intacto este archivo y trabajar sobre una **copia separada**.
2. Corregir H01–H06 y obtener evidencias operativas de la [lista de pruebas](../01_revision_rubrica_v3/PLAN_DE_PRUEBAS.md).
3. Resolver los [conflictos de información](../01_revision_rubrica_v3/RIESGOS_Y_CONFLICTOS.md) sin borrar el historial del equipo.
4. Completar presupuesto formal (dos cotizaciones chilenas por ítem relevante, IVA y fuentes) y preparar defensa de 15 minutos.
5. Revisar con Nico y Theri el informe antes de presentarlo como documento grupal final, respetando sus aportes diferenciados.
