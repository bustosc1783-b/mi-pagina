# Informe técnico de redes corporativas — versión 3 de avance

**Proyecto 2: Casa matriz y sucursal seguras**  
**Asignatura:** Redes Computacionales · Cisco Packet Tracer 9.0  
**Cliente académico:** Andes Ingeniería y Servicios SpA  
**Fecha de actualización:** 1 de noviembre de 2026  
**Estado:** borrador V3, no entrega final validada.

> **Nota de autoría y alcance.** Christopher confirmó que **Theri es quien armó la implementación de la red en Cisco Packet Tracer**. Se inspeccionó directamente la estructura y la configuración guardada de `TRABAJO REDES-backup.pkt`, que coincide con el archivo de ese nombre publicado en GitHub. **Esa implementación es la fuente técnica principal**; los 15 archivos `Proyecto2_PT/` y los textos de Nico son referencias auxiliares que pueden estar desactualizadas. Esta V3 es una redacción nueva y separada, no un supuesto informe escrito por Theri. La lectura estática del archivo **no equivale a ejecutar la simulación** ni comprueba por sí sola conectividad, servicios, VPN o disponibilidad.

## 1. Resumen ejecutivo

Andes Ingeniería y Servicios SpA es un cliente ficticio de ingeniería y soporte técnico con una casa matriz en Santiago y sucursal en Valparaíso. El proyecto busca conectar ambas ubicaciones de forma segura, separar la información de los departamentos, resguardar servidores y ofrecer continuidad en el núcleo de red. La propuesta contempla dos routers perimetrales conectados por dos equipos ISP simulados, VPN IPsec de sitio a sitio, NAT/PAT, DMZ de servicios, VLAN, dos switches multicapa por sede, OSPF, DHCP, VoIP, IoT y controles de administración.

El avance ya es verificable a nivel de archivo: el trabajo de Theri contiene **51 dispositivos y 60 enlaces**, incluyendo los dos perímetros, cuatro switches multicapa, seis switches de acceso/DMZ, siete servidores y cinco teléfonos IP. El proyecto muestra configuraciones guardadas de OSPF, HSRP, IPsec y NAT/PAT. También presenta problemas concretos: la publicación web apunta a una IP diferente de la del servidor, seis servidores no tienen IPv4 fija guardada y no hay puntos de acceso inalámbrico. Esta V3 distingue deliberadamente entre **lo presente**, **lo incompleto** y **lo que exige pruebas**.

## 2. Problema, necesidad y alcance comercial

Según [requisitos del cliente](https://github.com/nguiraldes-sudo/proyecto-redes-corporativas/blob/main/documentacion/01-requisitos-del-cliente.md), las sedes crecieron sin una política uniforme de segmentación. Eso puede permitir accesos innecesarios entre departamentos, publicar servicios sensibles junto a sistemas internos o impedir una administración centralizada.

La solución propuesta aporta:

- **Confidencialidad:** separación por departamento y control con ACL; IPsec para el tráfico corporativo autorizado entre sedes.
- **Disponibilidad:** pareja de switches L3 por sede con HSRP v2 y enlaces agregados entre núcleos; la continuidad real debe demostrarse.
- **Administración:** SSH v2, acceso desde redes autorizadas, Syslog, NTP y AAA.
- **Servicios:** HTTP, DNS, correo, infraestructura y control IoT con publicación restringida desde la DMZ.
- **Escalabilidad:** direccionamiento VLSM y VLAN por función; se reservan subredes para ampliar usuarios sin reestructurar todo.

Los números iniciales de referencia del [caso del cliente](https://github.com/nguiraldes-sudo/proyecto-redes-corporativas/blob/main/documentacion/01-requisitos-del-cliente.md) son **85 usuarios en matriz y 38 en sucursal**. Son supuestos de dimensionamiento, no una cuenta de computadores efectivamente instalados en el `.pkt`.

## 3. Criterios obligatorios del proyecto

La presentación docente **`Proyectos Redes corporativas.pptx`**, diapositiva 7, exige:

1. Dos sedes y túnel IPsec site-to-site a través de **dos routers ISP**; NAT/PAT hacia Internet.
2. DMZ con HTTP, DNS, NTP, Email, Syslog y AAA; ACL para publicar únicamente lo necesario.
3. Al menos **seis departamentos por sede**, cada uno con VLAN y SSID con WPA2/WPA3 y clave propia.
4. **Dos switches multicapa por sede**, OSPF interno y DHCP por VLAN.
5. Telefonía IP, cámaras, termostatos conectados al servidor IoT y red móvil para gerencia.
6. Hardening con SSH v2, usuarios locales por área, port-security, banners y contraseñas cifradas.

Los entregables son `.pkt` funcional, **informe PDF**, planilla de presupuesto respaldada por cotizaciones y presentación/demostración de **15 minutos**. La pauta original fija **$20M–$30M CLP con IVA**; **Christopher confirmó permiso posterior del profesor para llegar hasta $35M con IVA**. Se trabajará con ese máximo y conviene adjuntar la constancia del cambio.

## 4. Arquitectura física y lógica construida por Theri

| Zona | Equipos encontrados en el `.pkt` | Función observada o configurada |
|---|---|---|
| Red externa | ISP1, ISP2 | Simulan conectividad entre las dos sedes y un cliente externo |
| Perímetro matriz | R-HQ | IP pública simulada, OSPF interno, DHCP, NAT/PAT, IPsec, ACL y CME |
| Núcleo matriz | CORE-HQ1, CORE-HQ2 | Inter-VLAN, SVI, HSRP v2, OSPF, trunks y EtherChannel |
| Acceso matriz | SW-HQ-A1, SW-HQ-A2, SW-HQ-A3 | Puertos de usuarios, seguridad de acceso y administración |
| Servidores | SW-DMZ y siete objetos `Server` | Segmento DMZ en matriz; la existencia de un servidor no demuestra que su servicio esté configurado |
| Perímetro sucursal | R-SUC | Funciones equivalentes de WAN y servicios de sucursal |
| Núcleo sucursal | CORE-S1, CORE-S2 | Inter-VLAN, HSRP v2, OSPF y EtherChannel |
| Acceso sucursal | SW-S-A1, SW-S-A2 | VLAN departamentales y puertos seguros |

El inventario estructural del archivo de Theri identifica **4 routers** (`R-HQ`, `R-SUC`, `ISP1`, `ISP2`), **4 switches multicapa**, **6 switches** (cinco de acceso y `SW-DMZ`), **7 servidores**, **15 dispositivos clasificados como PC**, **1 laptop**, **4 impresoras**, **5 teléfonos IP**, **2 componentes MCU IoT** y **3 dispositivos de distribución eléctrica**. Los 15 objetos PC incluyen los denominados `Termostato` y `Termostato2`, que **están tipificados como PC y no como termostatos IoT**, además del PC externo de pruebas. No debe confundirse ese inventario académico con una lista de compras.

El `.pkt` almacena **60 enlaces**. Los equipos de acceso tienen conexiones hacia los pares de core; `SW-DMZ`, en cambio, tiene **un único uplink físico a CORE-HQ1**. Este punto de fallo no desaparece por disponer de HSRP en el núcleo. La presencia de enlaces en el archivo no prueba la conmutación correcta ni la conectividad en vivo. Véase la [auditoría directa](../01_revision_rubrica_v3/AUDITORIA_DIRECTA_PKT_THERI.md).

## 5. Esquema VLSM y VLAN guardado en el proyecto de Theri

**Se usa el esquema compatible con las configuraciones guardadas en los cuatro core del `.pkt`**, no la numeración histórica de `documentacion/03`. Los gateways se proyectan como IP virtuales HSRP en los switches multicapa. Las direcciones de los hosts, el estado de los SVI y la operación real deben comprobarse con `show ip interface brief`, `show standby brief` e `ipconfig` al ejecutar la simulación.

### 5.1 Casa matriz (Santiago)

| VLAN | Área / servicio | Red y prefijo | Gateway HSRP |
|---:|---|---|---|
| 10 | Gerencia | 10.10.1.128/28 | 10.10.1.129 |
| 20 | Finanzas | 10.10.1.0/27 | 10.10.1.1 |
| 30 | Recursos Humanos | 10.10.1.32/27 | 10.10.1.33 |
| 40 | TI | 10.10.1.64/27 | 10.10.1.65 |
| 50 | Ventas | 10.10.0.0/25 | 10.10.0.1 |
| 60 | Operaciones | 10.10.0.128/26 | 10.10.0.129 |
| 70 | Telefonía IP | 10.10.0.192/26 | 10.10.0.193 |
| 80 | IoT | 10.10.1.96/27 | 10.10.1.97 |
| 90 | DMZ | 10.10.1.144/28 | 10.10.1.145 |
| 99 | Gestión | 10.10.1.160/28 | 10.10.1.161 |

### 5.2 Sucursal (Valparaíso)

| VLAN | Área / servicio | Red y prefijo | Gateway HSRP |
|---:|---|---|---|
| 10 | Gerencia | 10.20.1.16/28 | 10.20.1.17 |
| 20 | Finanzas | 10.20.0.160/27 | 10.20.0.161 |
| 30 | Recursos Humanos | 10.20.0.192/27 | 10.20.0.193 |
| 40 | TI | 10.20.0.224/27 | 10.20.0.225 |
| 50 | Ventas | 10.20.0.0/26 | 10.20.0.1 |
| 60 | Operaciones | 10.20.0.64/26 | 10.20.0.65 |
| 70 | Telefonía IP | 10.20.0.128/27 | 10.20.0.129 |
| 80 | IoT | 10.20.1.0/28 | 10.20.1.1 |
| 99 | Gestión | 10.20.1.32/28 | 10.20.1.33 |

Las seis primeras VLAN de cada sede satisfacen **la estructura de segmentación para seis departamentos**, pero no acreditan aún clientes y SSID por área. La sucursal no tiene DMZ propia en esta topología. La VLAN 999 se usa como nativa en troncales. No aparecen VLAN 110 ni 120 en la configuración guardada de los core, aunque ambas se mencionan en textos anteriores de Nico.

Los enlaces enrutados R-HQ–CORE-HQ1 y R-HQ–CORE-HQ2 usan **10.10.2.0/30** y **10.10.2.4/30**; los equivalentes R-SUC–CORE-S1/S2 usan **10.20.2.0/30** y **10.20.2.4/30**. Las loopbacks de routers sirven como fuentes de DHCP/CME. Las interfaces WAN simuladas usan 200.10.10.0/30 y 200.20.20.0/30, con enlaces ISP entre sí y hacia un equipo externo.

## 6. Conmutación, HSRP y alta disponibilidad

La capa de núcleo usa switches multicapa Cisco 3650 en el simulador. Los archivos de configuración contienen `ip routing`, SVI de las VLAN, enlaces troncales y EtherChannel LACP entre los dos core de cada sede.

**HSRP v2:** en matriz CORE-HQ1 tiene prioridad para VLAN 10, 20, 30, 40, 90 y 99, mientras CORE-HQ2 la tiene para VLAN 50, 60, 70 y 80. En sucursal CORE-S1 prioriza 10, 20, 30, 40 y 99; CORE-S2 prioriza 50, 60, 70 y 80. Se configura `preempt`, pero hace falta demostrar estado activo/respaldo y recuperación al cortar un enlace.

**STP y protección:** se declara Rapid PVST+ con raíces distribuidas por VLAN; VTP se encuentra en modo transparent. Los switches de acceso incluyen `port-security`, MAC sticky, máximo de dos dispositivos en puertos de usuario, `PortFast` y `BPDU Guard`. No se puede afirmar protección aplicada en el `.pkt` sin `show port-security` y pruebas del simulador.

## 7. Enrutamiento OSPF, WAN y salida a Internet

R-HQ, R-SUC y los cuatro switches core tienen una configuración OSPF área 0 con router IDs definidos. Las redes de los usuarios se anuncian desde core; los routers de borde anuncian rutas por defecto hacia Internet mediante `default-information originate`. Las interfaces LAN pasivas evitan vecindades innecesarias. Se requiere capturar las tablas de rutas y vecindades efectivas para evaluar convergencia.

En ambos routers perimetrales, NAT/PAT overload está preparado sobre la interfaz WAN. Sus ACL de NAT excluyen redes corporativas remotas del proceso de traducción, para que los paquetes intersede puedan asociarse a IPsec. El router de matriz también dispone de publicación NAT estática de **HTTP TCP/80** hacia el servidor web DMZ.

**Estado:** se identificaron comandos OSPF, PAT y NAT directamente en la configuración guardada de `R-HQ` y `R-SUC` dentro del `.pkt`; los [archivos de texto del equipo](https://github.com/nguiraldes-sudo/proyecto-redes-corporativas/tree/main/Proyecto2_PT) son apoyo, no la prueba principal. No hay en esta revisión salidas ejecutadas de `show ip route`, `show ip ospf neighbor` ni `show ip nat translations`.

## 8. VPN IPsec sitio a sitio

En **los dos routers del `.pkt`** se guardaron comandos de IKE/ISAKMP, AES-256, hash SHA, grupo Diffie-Hellman 2, autenticación de práctica con clave compartida, transform-set ESP y crypto maps en WAN. Los textos auxiliares describen tráfico interesante entre **10.10.0.0/20** (matriz) y **10.20.0.0/21** (sucursal); al ejecutar el simulador habrá que cotejar ambos sentidos y las ACL realmente activas, junto con la exclusión NAT.

**No se publica en esta memoria la clave de práctica.** Los algoritmos y dispositivos corresponden al entorno didáctico y deben reevaluarse si la solución se implementara sobre infraestructura comercial real.

**Diferencia entre configuración y resultado:** la documentación antigua afirma que un IOS de R-SUC no soportaba IPsec, pero **ambos routers de Theri sí contienen configuraciones criptográficas guardadas**. Esto no demuestra que el túnel esté negociado. La prueba decisiva será generar tráfico permitido, observar `show crypto isakmp sa` y `show crypto ipsec sa` en ambos extremos, verificar los contadores y registrar capturas.

## 9. DMZ, servidores y políticas de seguridad

La DMZ guardada en la configuración de los core ocupa **VLAN 90, 10.10.1.144/28**, con puerta de enlace virtual **10.10.1.145**. La [guía de hosts de Nico](https://github.com/nguiraldes-sudo/proyecto-redes-corporativas/blob/main/Proyecto2_PT/15_Servidores_y_hosts.txt) **propone** direcciones .146 a .152, pero **no refleja por completo el estado guardado de Theri**:

- En `R-HQ`, la regla de NAT estática de HTTP apunta a **10.10.1.146:80**, mientras que el objeto `Server HTTP` tiene guardada la IP **10.10.1.147**, con **máscara /24**, diferente de la DMZ **/28**. Hay que ajustar direccionamiento, NAT y máscara en una copia del proyecto y probar la publicación.
- Los otros seis objetos `Server` no presentan **IPv4 fija guardada** en su interfaz. No se puede afirmar que tengan las IP que aparecen en los documentos.
- En los siete servidores, el estado guardado indica **DNS y AAA deshabilitados**. Otros servicios pueden aparecer habilitados por defecto, sin demostrar configuración o funcionamiento real.

El siguiente cuadro indica los servicios **exigidos por la pauta y previstos en el proyecto**, no un cumplimiento validado:

| Servicio | Uso académico esperado | Verificación/corrección necesaria |
|---|---|---|
| HTTP/HTTPS | Página web corporativa | Corregir NAT .146 frente a NIC .147 y máscara; navegar desde LAN y PC externo |
| DNS | Resolución de nombres de servicios | Habilitar/configurar DNS; consultar registros desde cada sede |
| NTP | Sincronización de equipos | Validar sincronización del cliente/infraestructura |
| Email | Correo de demostración | Enviar y recibir correo entre usuarios de prueba |
| Syslog | Centralización de eventos | Generar evento y comprobar recepción |
| AAA | Autenticación administrativa | Habilitar/configurar AAA; probar autorización y rechazo desde gestión |
| IoT Server | Registro de cámara y termostato | Alta/control y aislamiento desde VLAN IoT |

No debe interpretarse que todos estén expuestos a Internet. Las ACL de núcleo y perímetro intentan limitar servicios; falta ensayar **permisos y denegaciones** desde cada zona. En una solución de producción se recomienda mantener AAA, Syslog e infraestructura sensible fuera de una zona publicada a usuarios externos.

## 10. DHCP, telefonía IP e IoT

Los routers R-HQ y R-SUC contienen pools DHCP para las VLAN 10–80 (departamentales, voz e IoT). Las interfaces SVI del núcleo llevan `ip helper-address` hacia la loopback del router de su sede; DHCP asigna como gateway la IP virtual HSRP del segmento. La VLAN 99 de gestión utiliza direccionamiento estático y control de acceso.

La telefonía IP se plantea mediante CME: anexos de matriz **1001–1003** y de sucursal **2001–2002**, con `option 150` hacia el servicio CME y dial peers para llamadas intersede. Hay dos componentes MCU IoT y dos objetos denominados `Termostato` y `Termostato2`, pero estos últimos **son de tipo PC** en el `.pkt`, no sensores IoT comprobados. Tampoco se acredita todavía una cámara funcional. El objetivo de prueba incluye registro telefónico, llamada entre sedes, enrolamiento IoT y **bloqueo de acceso IoT a áreas sensibles**.

Las configuraciones y la guía son específicas, pero **el registro real de equipos y las llamadas no están demostrados** en esta revisión.

## 11. Conectividad inalámbrica y requisito de SSID

La pauta del profesor exige mínimo seis departamentos por sede, cada uno con SSID y WPA2/WPA3 de clave propia. **El inventario real del `.pkt` de Theri no contiene ningún Access Point ni Wireless Router.** No es simplemente que falten capturas: la infraestructura inalámbrica **está ausente en este archivo**, aunque los textos auxiliares mencionen AccessPoint-PT.

El grupo señaló en su documentación que el docente habría aceptado Wireless como opcional. Si existe esa excepción, conviene anexar la instrucción del profesor. Mientras no se haga, para la rúbrica oficial este requisito queda **pendiente de implementación o de aclaración formal**. La WLAN no debe reemplazar la red cableada que da servicio a los equipos fijos.

## 12. Seguridad de administración

El diseño incluye acceso remoto por SSH v2, usuarios locales de demostración, restricciones VTY desde redes de TI/gestión, banners, contraseñas almacenadas con mecanismos del IOS simulado y ACL perimetrales. La simulación usa claves académicas visibles en el repositorio: **no son credenciales aptas para producción ni deben reutilizarse**.

Las pruebas deben verificar explícitamente que un administrador autorizado puede entrar desde TI y que otra red no puede hacerlo. También deben registrar el comportamiento de `port-security`, el estado de BPDU Guard y la restricción a los servidores DMZ.

## 13. Presupuesto comercial y equipos equivalentes 2026

El cliente necesita justificar compra, instalación y operación. Los modelos 2911 y 2960 usados en Packet Tracer son **representaciones didácticas**, no se deben presupuestar como sustitutos comerciales actuales sin estudiar soporte y licencias. Se deberán considerar:

- Cuatro switches multicapa (dos por sede), cinco switches de acceso, un switch DMZ y dos routers/firewalls del cliente con soporte VPN y routing correspondiente. Los **otros dos routers ISP** simulan al proveedor y no se añaden automáticamente como compra del cliente.
- Puntos de acceso y protección WPA2/WPA3 si se exige la WLAN; teléfonos IP, cámaras y sensores.
- PCs/laptops del estándar 2026 indicado en la pauta, servidores y respaldo eléctrico.
- Cableado Cat6, racks, patch panels, UPS, módulos y licencias.

**Tope presupuestario vigente informado por Christopher: $35.000.000 CLP, IVA incluido, autorizado por el profesor** (la PPTX original mencionaba máximo $30M). Para cada ítem relevante habrá al menos dos cotizaciones chilenas con precio, fecha, disponibilidad, enlace/documento y explicación de elección. El proyecto no tiene aún aquí una planilla completa validada; por ello no se inventan valores ni se repiten precios antiguos como cotizaciones vigentes. Véase [BASE_PRESUPUESTO_DESDE_PKT.md](BASE_PRESUPUESTO_DESDE_PKT.md) para distinguir lo simulado de los equipos a cotizar.

## 14. Matriz de pruebas pendientes

La rúbrica otorga **15% a OSPF** y **15% al requisito central P2 (VPN/NAT/DMZ)**, por lo que son verificaciones prioritarias. El plan completo está en [PLAN_DE_PRUEBAS.md](../01_revision_rubrica_v3/PLAN_DE_PRUEBAS.md).

| Bloque | Pruebas mínimas para el informe final | Estado |
|---|---|---|
| LAN/VLSM | `show vlan brief`, `show interfaces trunk`, `ipconfig`, ping autorizado y denegado | Sin captura de la V3 |
| Routing | `show ip ospf neighbor`, `show ip route ospf` | Sin captura de la V3 |
| Alta disponibilidad | `show standby brief`, `show etherchannel summary`, caída de un enlace | Sin captura de la V3 |
| VPN | `show crypto isakmp sa`, `show crypto ipsec sa`, contadores antes/después | Sin captura de la V3 |
| NAT/DMZ | Corregir .146↔.147 y /24↔/28; `show ip nat translations`, HTTP externo, ACL de denegación | **Inconsistencia comprobada en el archivo** |
| Servicios | IP de seis servidores, habilitar/probar DNS/AAA y verificar NTP, email, Syslog, VoIP, IoT | **DNS/AAA apagados; resto sin pruebas** |
| Wireless | Puntos de acceso y seis SSID por sede o excepción docente acreditada | **No hay AP en `.pkt`** |
| Entrega | `.pkt` único, PDF, cotizaciones, presentación de 15 minutos | Pendiente de consolidación |

Cada evidencia debe estar vinculada al nombre exacto del `.pkt`, fecha, equipo y resultado observado. No se sustituirán capturas por instrucciones de cómo probar.

## 15. Riesgos abiertos y acciones prioritarias

1. **Corregir publicación web en una copia del `.pkt`:** NAT .146 frente a servidor .147, máscara /24 frente a DMZ /28; probar HTTP desde el exterior.
2. **Completar direccionamiento y servicios:** seis servidores sin IPv4 fija guardada, DNS/AAA deshabilitados; probar cada rol exigido.
3. **Resolver la WLAN:** ningún AP presente en el `.pkt`; implementar SSID/seguridad o acreditar excepción docente.
4. **Confirmar IPsec, OSPF y HSRP operativos:** sin SA, vecinos/rutas ni failover observado no se pueden dar por cumplidos.
5. **Revisar IoT y redundancia DMZ:** los objetos `Termostato` son PC y `SW-DMZ` tiene un único uplink.
6. **Respetar la numeración real:** 70 voz, 80 IoT, 90 DMZ, 99 gestión; los textos históricos de Nico difieren.
7. **Completar cotizaciones y defensa:** hasta $35M IVA incluido con permiso docente informado, proveedores chilenos y presentación de 15 minutos.

## 16. Conclusión técnica provisional

Theri ha construido una topología concreta de **51 dispositivos y 60 enlaces**, cuyos equipos guardan configuraciones de VLAN, VLSM, OSPF, HSRP, DHCP, IPsec, NAT/PAT, DMZ, VoIP y seguridad de acceso. **Es un avance real, pero no una validación integral de la rúbrica:** hay conflictos técnicos localizados y requisitos ausentes.

La siguiente etapa es **corregir los hallazgos en una copia del proyecto de Theri, ejecutar pruebas y reunir evidencias**. Los textos de Nico pueden servir para explicar o proponer configuraciones, pero **no permiten declarar implementado algo ausente del `.pkt`**. Este informe V3 permanece separado de los originales y atribuye a Theri la implementación en Cisco.

## Fuentes del equipo

- [README y estado grupal](https://github.com/nguiraldes-sudo/proyecto-redes-corporativas/blob/main/README.md).
- [Requisitos del cliente](https://github.com/nguiraldes-sudo/proyecto-redes-corporativas/blob/main/documentacion/01-requisitos-del-cliente.md).
- [Diseño de topología](https://github.com/nguiraldes-sudo/proyecto-redes-corporativas/blob/main/documentacion/02-diseno-de-topologia.md).
- [VLAN y direccionamiento histórico](https://github.com/nguiraldes-sudo/proyecto-redes-corporativas/blob/main/documentacion/03-vlan-y-direccionamiento-ip.md).
- [Seguridad y VPN histórica](https://github.com/nguiraldes-sudo/proyecto-redes-corporativas/blob/main/documentacion/04-seguridad-perimetral-y-vpn.md).
- [Matriz inicial de políticas](https://github.com/nguiraldes-sudo/proyecto-redes-corporativas/blob/main/documentacion/05-matriz-de-trafico-y-politicas.md).
- [Conjunto de configuraciones Proyecto2_PT](https://github.com/nguiraldes-sudo/proyecto-redes-corporativas/tree/main/Proyecto2_PT), especialmente `05`, `06`, `07`, `10`, `11`, `12` y `15`.
- **Fuente primaria:** `packet-tracer/TRABAJO REDES-backup.pkt`, hecho por Theri; SHA-256 `18a404cadd2dbc8e4e0a38c9d44903ecf0512b60391ad5a59cbfd0b0a644460d`. El `.pkt` **no se modifica ni se incluye** en el paquete V3.
- [Auditoría directa del `.pkt`](../01_revision_rubrica_v3/AUDITORIA_DIRECTA_PKT_THERI.md).
- Rúbrica de la asignatura: **`Proyectos Redes corporativas.pptx`**, disponible entre los archivos compartidos por Chris, no alojada en el repositorio.
