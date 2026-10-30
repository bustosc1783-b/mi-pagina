# Rubrica Web Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Corregir problemas de semántica, layout en tablets y peso de recursos sin perder el diseño de Capricornio Studio 83.

**Architecture:** Sitio estático con `index.html`, `assets/css/styles.css`, Bootstrap local e imágenes propias. Las pruebas son de contratos de entrega y recursos, usando Python estándar sin dependencias nuevas.

**Tech Stack:** HTML5, CSS, Bootstrap 5, WebP, Python unittest.

**Spec:** `docs/superpowers/specs/2026-10-29-rubrica-web-design.md`

## Global Constraints

- Mantener enlaces, textos, logos y 12 escenas originales.
- No introducir servicios externos ni dependencias del servidor.
- Conservar los PNG originales como respaldo; las variantes optimizadas pueden tener extensión WebP.

## Review Focus

- Anchos 601-800 px: sección estudio en una columna, sin overflow.
- Imágenes para redes lentas: las 12 escenas no deben sumar más de 7 MB.
- Imágenes visibles: `src` corresponde a archivos del repositorio, con `alt`.
- Pasos: lista ordenada real de tres elementos.
- Publicación: ruta de GitHub Pages resuelve todos los recursos.

---

### Task 1: Semántica y adaptación

**Files:** `index.html`, `assets/css/styles.css`, `tests/test_site.py`.

- [ ] Escribir pruebas para lista de tres pasos y regla CSS de tablets.
- [ ] Ejecutar `python3 -m unittest discover -s tests -v` y observar errores esperados.
- [ ] Convertir los tres pasos a `<ol>` / `<li>` y darles CSS compatible con Bootstrap.
- [ ] Agregar media query 601-800 px para una columna en estudio.
- [ ] Ejecutar pruebas hasta verde.

### Task 2: Optimizar imágenes y referencias

**Files:** `assets/images/martes/*.webp`, imágenes WebP nuevas, `index.html`, `assets/css/styles.css`, `tests/test_site.py`.

- [ ] Escribir pruebas de presupuesto de bytes, existencia de recursos y atributos de imágenes.
- [ ] Ejecutar pruebas y observar fallo inicial por peso de imágenes.
- [ ] Reconvertir escenas a WebP de buena calidad; crear WebP de hero y logo.
- [ ] Actualizar las referencias en HTML y CSS.
- [ ] Ejecutar la suite completa hasta verde, verificar tamaño y dimensiones.

### Task 3: Entrega y revisión

**Files:** `README.md`, repositorio GitHub.

- [ ] Documentar enlaces al código y sitio publicado.
- [ ] Inspeccionar `git diff` y ejecutar pruebas completas.
- [ ] Subir el commit a `main` con autorización de edición ya concedida.
- [ ] Verificar la web pública, enlaces, imágenes, menú, galería y carrusel.
