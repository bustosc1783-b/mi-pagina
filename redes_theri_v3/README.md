# Redes corporativas — versión 3 de trabajo del equipo

**Fuente técnica principal:** trabajo de **Theri** en el simulador de Cisco Packet Tracer.  
**Apoyo secundario:** documentos de **Nico**, utilizados solo cuando concuerdan con el `.pkt`.  
**Corte:** 1 de noviembre de 2026. **Estado:** análisis técnico y borradores de avance, no entrega final operativamente validada.

Esta publicación está **aislada en una rama independiente** del GitHub de Christopher. No modifica el proyecto web de la rama `main` ni ningún documento original del repositorio de Nico.

## Dos carpetas de trabajo

1. [01 — Revisión de la rúbrica](01_revision_rubrica_v3/README.md): inventario comprobado, 10 criterios, conflictos H01–H06 y plan de pruebas.
2. [02 — Informe y propuesta V3](02_informe_tecnico_v3/README_actualizacion.md): memoria técnica, propuesta para el cliente y base de presupuesto desde los equipos Cisco.

## Fuente original que no se modifica

- [Archivo Packet Tracer creado por Theri](https://github.com/nguiraldes-sudo/proyecto-redes-corporativas/blob/main/packet-tracer/TRABAJO%20REDES-backup.pkt).
- [Documentación y archivos `Proyecto2_PT` del repositorio de Nico](https://github.com/nguiraldes-sudo/proyecto-redes-corporativas).
- Rúbrica docente `Proyectos Redes corporativas.pptx` compartida con Christopher.

## Avance y límites

El `.pkt` conserva **51 dispositivos y 60 enlaces**. Tiene configuración guardada de OSPF, HSRP, DHCP, VPN IPsec, NAT/PAT y seguridad. La auditoría identificó seis problemas que deben corregirse/verificarse **en una copia** de Cisco antes de la entrega: IP/máscara del servidor HTTP frente a NAT, seis servidores sin IP fija, DNS/AAA deshabilitados, falta de AP, «termostatos» tipo PC y un solo uplink en la DMZ.

**Presupuesto:** la PPTX original señala $20–30M IVA incluido; **Christopher confirmó permiso posterior del profesor para un máximo de $35M IVA incluido**. La V3 incorpora ese límite, y recomienda documentar la autorización.

**No se afirma** que existan pings, VPN negociada, pruebas de servicios, cotizaciones ni PDF final hasta obtener sus evidencias. Esta rama es un espacio compartible para el trabajo del grupo, no una modificación de los originales.
