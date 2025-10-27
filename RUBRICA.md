
# RÚBRICA OFICIAL — Prueba Técnica (Sin Docker)

> Condición dura: **todos los tests en verde**. Si falla alguno, la calificación final se **topea en 59**.

## Ponderación (Total 100 pts)
1. **Lógica de Programación — 25 pts**
   - Correctitud total (tests + casos borde) — 15
   - Eficiencia razonable — 5
   - Claridad (nombres, docstrings breves) — 5

2. **Fundamentos de Python — 20 pts**
   - Idiomaticidad (listas/dicts comp, `set`, `enumerate`, `zip`) — 6
   - Estructura (funciones pequeñas, DRY, módulos limpios) — 6
   - Errores/validaciones (try/except juicioso) — 4
   - Pruebas (no tocar tests provistos; puede añadir propios) — 4

3. **Fundamentos de React — 20 pts**
   - Estado/efectos (fetch correcto, deps, cleanup) — 8
   - UX mínima (loading/error, debounce 300 ms) — 6
   - Componentización (props claras, separación SearchBar/ProductList/hook) — 4
   - Pruebas UI (Vitest/RTL con selectores semánticos) — 2

4. **Uso de GitHub — 15 pts**
   - Flujo ramas → PR (nada directo a `main`) — 5
   - Commits claros e incrementales — 5
   - Descripción de PR (qué, por qué, cómo probar, riesgos) — 5

5. **Buenas Prácticas — 10 pts**
   - Legibilidad/estilo (consistencia, formateo) — 4
   - Configuración/secretos (env vars, nada sensible en repo) — 3
   - Errores/logs (mensajes claros, sin ruido) — 3

6. **Uso de IA — 10 pts**
   - Transparencia (archivo `AI_USAGE.md` con prompts y qué generó la IA) — 4
   - Criterio (no copiar ciego; adaptación y explicación) — 4
   - Ética/seguridad (sin datos sensibles/licencias violadas) — 2

### Penalizaciones
- Modificar/burlar tests existentes — **−20**
- Romper contrato (API o props) — **−10**
- Hardcodear datos en vez de llamar al API — **−5**
- Commits caóticos o sin `README_personal.md` — **−5 / −3**
- Warnings/errores en consola o secretos expuestos — **−3 / −5**

### Escala de decisión
- **90–100**: contratable
- **80–89**: sólido
- **70–79**: aceptable con mentoría
- **60–69**: flojo
- **<60**: no aprobado
> Si falla algún test → **tope 59**.

---

## Checklist de Revisión Rápida
- [ ] Tests backend + frontend en verde (CI y local)
- [ ] Lógica: casos borde cubiertos; sin O(n²) innecesario
- [ ] Python: idiomático; funciones cortas; no tocó tests provistos
- [ ] React: debounce real; loading/error; fetch limpio con deps correctas
- [ ] GitHub: rama de feature; PR bien descrito; commits claros
- [ ] Buenas prácticas: sin secretos; logs/errores claros
- [ ] IA: `AI_USAGE.md` honesto; decisiones con criterio

## Cómo calificar (fórmula)
1. Suma de secciones (100 pts).
2. Resta **Penalizaciones**.
3. Si `tests_passed = false` → setear **59** como máximo.
