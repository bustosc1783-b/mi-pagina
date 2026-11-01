# Base para propuesta al cliente y presupuesto — derivada del Cisco de Theri

**Estado:** insumo de costeo, **no una cotización ni una planilla final**. Fecha de corte: 1 de noviembre de 2026. Fuente: inspección estática de `TRABAJO REDES-backup.pkt` de Theri, contrastada con la rúbrica oficial.

## Regla central

La red simulada establece **necesidades y capacidades**; una compra real debe usar modelos vigentes y la escala del cliente. No es válido tomar todos los iconos de Packet Tracer como una factura: routers ISP, computadoras de demostración, servidores virtualizables, elementos de prueba y dispositivos etiquetados como IoT tienen tratamientos distintos.

| Componente | Cantidad vista en Cisco | Criterio para cotizar |
|---|---:|---|
| Router de borde de empresa | 2 (R-HQ, R-SUC) | Dos equipos o firewalls empresariales equivalentes con IPsec, NAT y routing, considerando licencias |
| Router ISP | 2 (ISP1, ISP2) | Representan red del proveedor; cotizar **servicio de conectividad** y condiciones SLA, no comprar automáticamente estos routers |
| Switch multicapa de núcleo | 4 | Dos L3 por sede, capacidad HSRP/equivalente, OSPF, uplinks y soporte |
| Switch de acceso | 5 | Modelos administrables con VLAN, 802.1Q, seguridad y PoE según puertos requeridos |
| Switch de DMZ | 1 | Switch administrable específico, revisar segundo uplink/alta disponibilidad |
| Servidores simulados | 7 | Dimensionar servicios HTTP, DNS, NTP, correo, Syslog, AAA e IoT; **evaluar virtualización**, respaldo, OS/licencias y redundancia; no comprar siete servidores físicos sin justificación |
| PCs etiquetados PC0–PC12 | 13 | Incluye PC externo de ensayo; definir puestos reales desde demanda del cliente (Nico propone 85 en matriz y 38 sucursal, **dato aún sin validar**) |
| PCs etiquetados «Termostato» | 2 | Son tipo PC en el archivo, no termostatos demostrados; cotizar sensores **solo cuando se acuerde la solución IoT real** |
| Laptop | 1 | El dispositivo sirve como referencia, no fija demanda comercial |
| Impresoras | 4 | Validar necesidad por sede, volumen, conectividad y servicio |
| Teléfonos IP | 5 | Referencia de PoC; dimensionar extensiones finales y licencias del sistema telefónico |
| Componentes MCU IoT | 2 | Validar si serán controladores, sensores o equipos de prueba antes de presupuestar |
| Distribuidores de energía simulados | 3 | No sustituyen UPS, PDU comerciales o protección eléctrica; dimensionar consumo y autonomía |
| Access Points | **0** | La rúbrica exige WLAN por departamento; diseñar cobertura/SSID por área y cotizar AP, control y licencias si corresponde |
| Cableado y pasivos | 60 enlaces simulados | Levantar metros reales, canalizaciones, puntos Cat6, racks, patch panels, fibra/módulos, certificación y mano de obra |

## Estructura requerida de la planilla de compras

Una fila por producto o servicio con: **sede**, categoría, requisito de la rúbrica, especificación técnica, cantidad justificada, proveedor A y B de Chile, enlaces a cotizaciones, fecha, precio neto unitario, IVA, precio total IVA incluido, licencias/garantía, instalación, decisión comercial y argumento técnico. Los precios se recogen cuando existan ofertas verificables; este documento **no inventa montos**.

Partidas mínimas a considerar:

1. Borde/WAN: equipos empresariales, licencias IPsec/seguridad, contratación ISP, instalación y soporte.
2. Switching: cuatro core L3, cinco de acceso, DMZ, PoE, transceptores y reservas de puertos.
3. WLAN: AP, cobertura, múltiples SSID/WPA2-WPA3, administración y posibilidad de excepción docente por escrito.
4. Servicios: infraestructura de virtualización o servidores, respaldo, sistema operativo, NTP/DNS/AAA/Email/Syslog/HTTP/IoT.
5. Puestos y colaboración: terminales según dotación validada, impresoras, teléfonos, cámaras y sensores auténticos.
6. Infraestructura: racks, UPS/PDU reales, Cat6, fibra si aplica, certificación, puesta en marcha, capacitación, contingencia y soporte.

## Validaciones presupuestarias antes de declarar cumplimiento

- La **pauta original dice $20.000.000–$30.000.000 CLP, IVA incluido**. Christopher confirma que el profesor autorizó posteriormente **hasta $35.000.000 CLP IVA incluido**. Utilizar **$35M como máximo vigente** y conservar constancia del permiso para anexarla a la entrega; **no es necesario agotar el tope**.
- Reunir **dos cotizaciones chilenas por partida relevante**, actuales y comparables; confirmar moneda y si incluyen IVA, despacho, licencias y soporte.
- Justificar el número de usuarios y puertos por sede: **51 objetos Packet Tracer no equivalen a 51 empleados** y la cifra 85/38 es solo un antecedente documental.
- Evaluar equipos equivalentes de catálogo contemporáneo; **Cisco 2911/2960 del simulador no son automáticamente la oferta recomendada**.
- No prometer disponibilidad 100 %, túnel VPN operando ni servicios DMZ funcionales antes de corregir H01–H06 y ejecutar pruebas.

## Condición para entregar al cliente

La propuesta comercial podrá cerrarse cuando haya arquitectura final aprobada, fichas de prueba del `.pkt`, cotizaciones comparables y una tabla de inversión total que cuadre con el rango oficial. Mientras tanto, esta base distingue con honestidad la ingeniería hecha por Theri de la ingeniería todavía pendiente.
