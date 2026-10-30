# Correcciones de la rúbrica de página web

## Objetivo

Mantener la identidad y el contenido de Capricornio Studio 83 y corregir los riesgos encontrados en la revisión de la rúbrica del curso.

## Alcance y decisiones

- Conservar HTML estático, Bootstrap local y CSS existente; no migrar de plataforma ni rediseñar el sitio.
- Representar los tres pasos del proceso como una lista ordenada semántica sin cambiar su presentación de tarjetas.
- Evitar que la sección del estudio use dos columnas en tablets estrechas (601-800 px), conservando el diseño de escritorio y móvil.
- Reducir significativamente el peso de las doce escenas, la imagen principal y el logo visible, sin cambiar su contenido ni proporción.
- Mantener los originales PNG en el repositorio para no perder fuentes de imagen.
- Mejorar el README con enlaces a GitHub Pages y al código para facilitar la entrega.

## Enfoques considerados

1. **Corrección puntual (elegido):** ajustar HTML/CSS, comprimir recursos y añadir pruebas. Menor riesgo y conserva el diseño aprobado.
2. Rediseño completo en otro framework: más posibilidades, pero innecesario y arriesgado para una evaluación anterior a JavaScript.
3. Mantener el diseño y añadir solo avisos de revisión: no elimina los problemas detectados.

## Exclusiones y verificación

No se alteran los textos comerciales, contactos ni la funcionalidad del carrusel/modal. Se requieren pruebas locales y una revisión de la web publicada tras actualizar GitHub Pages. No se garantiza la nota docente: la decide el profesor.
