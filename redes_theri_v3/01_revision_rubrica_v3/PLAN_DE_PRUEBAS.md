# Plan de pruebas y evidencias para cerrar la rúbrica

**Regla:** realizar estas pruebas en una **copia de trabajo** del `.pkt` de Theri, guardar capturas de Packet Tracer y no sobrescribir el original. La inspección directa ya confirmó configuración guardada y hallazgos H01–H06, pero todos los **resultados operativos** siguientes están pendientes hasta ejecutarlos.

| ID | Prueba | En qué equipo / pantalla | Evidencia que aprobaría |
|---|---|---|---|
| T01 | Inventario y cableado | Captura de topología completa; `show cdp neighbors`, `show ip interface brief` en routers/core | Todos los equipos y enlaces previstos presentes, interfaces activas |
| T02 | VLAN y troncales | `show vlan brief`, `show interfaces trunk` en core/acceso | VLAN y puertos correctos; troncal lleva las VLAN esperadas |
| T03 | VLSM y DHCP | `ipconfig` de un PC por departamento en las dos sedes; `show ip dhcp binding` | IP, máscara, gateway HSRP y DNS coinciden con tabla vigente |
| T04 | OSPF | `show ip ospf neighbor`, `show ip route ospf` en R-HQ, R-SUC y core | Vecinos en estado esperado y rutas aprendidas |
| T05 | HSRP y EtherChannel | `show standby brief`, `show etherchannel summary` | Activo/respaldo y canal correctamente formados |
| T06 | VPN IPsec | `show crypto isakmp sa`, `show crypto ipsec sa` antes/después de tráfico autorizado | Negociación válida y contadores de cifrado/descifrado aumentan |
| T07 | NAT/PAT | `show ip nat translations` y navegación desde cliente interno | Traducción para Internet; tráfico intersede no traducido |
| T08 | DMZ y publicación | Comprobar NAT `10.10.1.146:80` frente a IP real `10.10.1.147` y máscara `/24`; corregir en copia y abrir HTTP desde PC externo | Dirección/máscara coherentes con DMZ `/28`, HTTP responde y accesos no publicados bloqueados |
| T09 | ACL y SSH | `show access-lists`, `show ip ssh`; prueba desde TI y otra VLAN | Acceso administrativo permitido solo desde orígenes autorizados |
| T10 | Port-security / STP | `show port-security interface ...`, `show spanning-tree`, BPDU Guard | Controles habilitados y resultado comprobado sin dañar la versión final |
| T11 | Servicios | Revisar IP/máscara/gateway de `Server HTTP` y Server1–Server6; DNS/AAA aparecen apagados; probar HTTP, DNS, NTP, correo, Syslog y AAA | Siete roles asignados y comprobados según pauta, captura por servicio; habilitar lo necesario en copia |
| T12 | VoIP e IoT | Registro de IP Phones, llamada 100x ↔ 200x, cámara y sensores reales; los objetos llamados `Termostato` son PC | Registro, llamada y control IoT visibles; aislamiento probado; tipo de equipo aclarado |
| T13 | Wireless | No hay AP en el `.pkt`: agregar y probar SSID por área con WPA2/3, `ipconfig` y aislamiento | VLAN/SSID por departamento en ambas sedes o dispensa docente escrita adjunta |
| T14 | Redundancia | Desconectar un enlace/core en una **copia de prueba** del `.pkt`, con especial atención al único uplink de SW-DMZ | Antes/después del tráfico, estado HSRP, pérdida de DMZ y recuperación documentados |

## Convención para compartir evidencias

Crear posteriormente, sin cambiar configuraciones del equipo, una subcarpeta de evidencias con nombres como:

- `T04_R-HQ_ospf_neighbor_YYYY-MM-DD.png`
- `T06_R-HQ_crypto_isakmp_sa_YYYY-MM-DD.png`
- `T06_R-SUC_crypto_ipsec_sa_YYYY-MM-DD.png`
- `T08_PC-Externo_HTTP_YYYY-MM-DD.png`
- `T14_HSRP_caida_core_YYYY-MM-DD.png`

## Ficha única de registro por prueba

| Campo | Completar por el grupo |
|---|---|
| ID y fecha | |
| Nombre exacto del `.pkt` usado | |
| Equipo, interfaz o PC | |
| Comando / procedimiento | |
| Resultado esperado | |
| Resultado real observado | |
| Evidencia (archivo) | |
| Estado aprobado / fallido | |
| Responsable y corrección pendiente | |

**Cierre de entrega:** además de lo técnico, producir PDF final, planilla presupuestaria de hasta **$35M CLP con IVA**, conforme al permiso posterior informado por Christopher (pauta original: $20M–$30M; adjuntar constancia de cambio), dos cotizaciones por ítem relevante y presentación comercial de 15 minutos. Mantener los `.pkt` originales sin sobrescribirlos.
