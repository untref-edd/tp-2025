# Planificación del Proyecto

## Cronograma General

**Fecha de entrega**: 25 y 27 de Noviembre

### Hitos Principales

#### Fase 1: Configuración Inicial (Semana 1)
- Definición de roles y responsabilidades
- Configuración del entorno de desarrollo
- Familiarización con las APIs y fuentes de datos
- Diseño de la arquitectura del sistema

#### Fase 2: Desarrollo de Módulos Base (Semanas 2-3)
- Implementación del módulo de APIs (OpenAlex, The Lens)
- Implementación del módulo de web scraping
- Implementación del módulo RSS
- Primeras pruebas unitarias

#### Fase 3: Integración y Persistencia (Semana 4)
- Generación de archivos CSV
- Integración de todos los módulos
- Desarrollo de la interfaz de consola
- Pruebas de integración

#### Fase 4: Documentación y Refinamiento (Semana 5)
- Jupyter Notebook con informe técnico
- Documentación completa del código
- Casos de prueba adicionales
- Optimización y corrección de bugs

#### Fase 5: Presentación (Semana 6)
- Preparación de material de presentación
- Ensayo de presentación oral
- Revisión final del código
- Entrega final

## Entregas Parciales Recomendadas

| Fecha Estimada | Entregable | Responsable |
|----------------|------------|-------------|
| Semana 1 | Diseño y arquitectura | Todo el equipo |
| Semana 2 | Módulo de APIs funcionando | [Asignar] |
| Semana 3 | Módulos scraping y RSS | [Asignar] |
| Semana 4 | Interfaz y CSV generados | [Asignar] |
| Semana 5 | Documentación completa | Todo el equipo |
| Semana 6 | Presentación lista | Todo el equipo |

## Tareas por Módulo

### Módulo APIs (Parte 1)
- [ ] Investigar documentación de OpenAlex API
- [ ] Investigar documentación de The Lens API
- [ ] Implementar consultas a OpenAlex
- [ ] Implementar consultas a The Lens
- [ ] Extraer metadatos requeridos
- [ ] Generar CSV de artículos
- [ ] Generar CSV de patentes
- [ ] Escribir pruebas unitarias

### Módulo Web Scraping (Parte 2)
- [ ] Analizar estructura HTML de eventseye.com
- [ ] Analizar estructura HTML de nferias.com
- [ ] Analizar estructura HTML de 10times.com
- [ ] Implementar scraper para cada sitio
- [ ] Consolidar datos extraídos
- [ ] Generar CSV de eventos
- [ ] Manejar errores y excepciones
- [ ] Escribir pruebas unitarias

### Módulo RSS (Parte 3)
- [ ] Localizar feeds RSS de WTO
- [ ] Localizar feeds RSS de UN Comtrade
- [ ] Implementar parser de feeds
- [ ] Extraer información de noticias
- [ ] Identificar país asociado
- [ ] Generar CSV de noticias
- [ ] Escribir pruebas unitarias

### Módulo Interfaz (Parte 4)
- [ ] Diseñar menú de opciones
- [ ] Implementar navegación por consola
- [ ] Integrar con módulo de APIs
- [ ] Integrar con módulo de scraping
- [ ] Integrar con módulo RSS
- [ ] Validar entradas de usuario
- [ ] Manejar errores de ejecución
- [ ] Escribir pruebas de integración

### Documentación
- [ ] Crear Jupyter Notebook
- [ ] Documentar análisis de cada técnica
- [ ] Explicar librerías utilizadas
- [ ] Describir estructuras de datos
- [ ] Documentar problemas encontrados
- [ ] Escribir conclusiones
- [ ] Incluir archivos CSV generados
- [ ] Preparar slides de presentación

## Metodología de Trabajo

- **Reuniones semanales** para coordinación y seguimiento
- **Commits frecuentes** en el repositorio
- **Code review** entre pares antes de integrar
- **Testing continuo** durante el desarrollo
- **Documentación incremental** a medida que se desarrolla

## Riesgos y Mitigación

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| APIs no disponibles | Media | Alto | Implementar cache y datos de prueba |
| Sitios web cambian estructura | Alta | Medio | Hacer scraping flexible, documentar estructura |
| Retrasos en desarrollo | Media | Alto | Buffer de tiempo, priorizar funcionalidad core |
| Problemas de integración | Media | Medio | Interfaces claras entre módulos, tests |
| Falta de coordinación | Baja | Alto | Reuniones regulares, comunicación activa |

---

**Nota**: Este cronograma es una guía. Ajustar según las necesidades y capacidad del equipo.
