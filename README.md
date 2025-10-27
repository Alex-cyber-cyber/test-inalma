# Prueba Técnica — Lógica + Python + Django + React

**Tiempo sugerido:** 4–6 horas (puedes dividirlo en 2 días).  
**Nivel objetivo:** Semi–Senior (ajustable).  
**Stack:** Python 3.11+, Django 4.2+, DRF, React 18 (Vite), Vitest.

---

## 1) Objetivo

Resolver tres frentes:

1. **Lógica de programación (Python):** Implementar funciones en `backend/src/algos/functions.py` hasta pasar los tests de `backend/tests/test_algos.py`.
2. **API (Django + DRF):** Completar/ajustar el endpoint de productos para búsqueda, filtros, orden y validaciones; pasar `backend/src/catalog/tests/test_api.py`.
3. **UI (React):** Consumir el API con búsqueda (debounce 300 ms), manejo de loading/error y lista; pasar `frontend/src/__tests__/ProductList.test.jsx`.

> Los tests vienen fallando al inicio: tu trabajo es **ponerlos en verde sin romper contratos**.

---

## 2) Reglas y entregables

- **Entrega en GitHub** mediante **PR a `main`** (no push directo).
- **Todos los tests en verde** (backend y frontend).  
  - **Condición dura:** si algún test falla → **la nota final se topea en 59**.
- Incluye:
  - `README_personal.md` con decisiones, trade-offs y cómo probar tu entrega.
  - `AI_USAGE.md` si usaste IA u otras asistencias (ver sección 6).
- **No modifiques** los tests provistos para “hacerlos pasar”. Puedes añadir tests propios.

---

## 3) Requisitos

- **Python 3.11+**, **Node.js 18+**, `pip`, `npm`.
- Sistema operativo: Windows/macOS/Linux.

---

## 4) Instrucciones rápidas

### 4.1 Backend (Django + DRF)

```bash
cd backend
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata src/catalog/fixtures/products.json
pytest -q
python manage.py runserver 8000
```

- API en: `http://localhost:8000/api/products/`

### 4.2 Frontend (React + Vite)

```bash
cd frontend
npm install
npm test
npm run dev
```

- Web en: `http://localhost:5173`  
- **Config opcional:** `VITE_API_URL` (default `http://localhost:8000/api`).

### 4.3 Validación

- **Backend:** `pytest -q`
- **Frontend:** `npm test`
- **Éxito:** ambos en verde.

---

## 5) Especificación del API

**Ruta principal:** `GET /api/products/` y `POST /api/products/`

### 5.1 GET `/api/products/` (con paginación por 10)
Parámetros soportados:
- `q` — búsqueda por nombre (icontains)
- `min_price`, `max_price` — filtros por precio
- `tags` — coma separada; debe contener **todos** los tags solicitados (p. ej. `tech,pc`)
- `ordering` — uno de: `price`, `-price`, `name`, `-name`

**Respuesta (paginada):**
```json
{
  "count": 42,
  "next": "...",
  "previous": null,
  "results": [
    { "id": 1, "name": "Monitor", "price": "299.99", "tags": ["tech","pc"] }
  ]
}
```

### 5.2 POST `/api/products/`
Crea un producto con reglas:
- `name` **único case-insensitive** (no se permiten duplicados como “monitor” y “Monitor”).
- `price` `>= 0`.
- `tags`: lista de strings.

---

## 6) Uso de herramientas y asistencia (IA, foros, etc.)

Puedes usar **cualquier** herramienta o apoyo para completar la prueba:
- Buscadores, documentación oficial, blogs, Stack Overflow.
- Asistentes de IA (ChatGPT, Copilot, Claude, Perplexity, Cursor, etc.).
- Librerías, snippets y repos públicos **con licencia compatible**.

**Reglas de transparencia**
1. Si usas IA u otros recursos, **documenta** cómo te ayudaron en `AI_USAGE.md`  
   (qué pediste, qué te sugirió, qué adaptaste y por qué).
2. **No** pegues código que no entiendas; podrías tener que explicarlo.
3. **No** subas secretos/credenciales ni material propietario de terceros.
4. Cita **fuentes** cuando tomes ideas o fragmentos.
5. La evaluación pondera tu **criterio y calidad**, no solo pasar tests.

**Plantilla sugerida para `AI_USAGE.md`:**
```md
# AI_USAGE
## Herramientas usadas
- (ej.) ChatGPT / Copilot / Perplexity / Docs oficiales

## Prompts o consultas clave (resumen)
- “Validar nombre único case-insensitive en DRF…”
- “Debounce en React con prueba en Vitest…”

## Qué generó la herramienta y cómo lo adapté
- Sugerencia inicial: …
- Cambios propios: …
- Razón de los cambios: …

## Fuentes citadas
- Enlaces…

## Notas de ética/seguridad
- Sin secretos/credenciales.
- Licencias revisadas para cualquier snippet externo.
```

---

## 7) Evaluación (resumen)

La rúbrica detallada está en **[RUBRICA.md](./RUBRICA.md)**.  
Plantilla de calificación: **`plantillas/score.json`**.

**Ponderación (100 pts):**
- **Lógica de programación — 25**
- **Fundamentos de Python — 20**
- **Fundamentos de React — 20**
- **Uso de GitHub — 15**
- **Buenas prácticas — 10**
- **Uso de IA — 10**

**Penalizaciones (ejemplos):**
- Modificar/burlar tests existentes: **−20**
- Romper contrato (API/props): **−10**
- Hardcodear datos en lugar de llamar al API: **−5**
- Commits caóticos o sin `README_personal.md`: **−5 / −3**
- Warnings/errores en consola o secretos expuestos: **−3 / −5**

**Regla dura:** Si falla algún test → **tope 59**.

---

## 8) Flujo de trabajo en GitHub

1. Trabaja en **rama de feature** (no en `main`).  
2. Abre **PR a `main`** con:
   - Descripción clara: *qué cambia / por qué / cómo probar / riesgos*.
   - Evidencia de tests en verde (logs locales o CI).
3. Recomendado: proteger `main` en *Settings → Branches → Add rule*:
   - Requerir PR.
   - Requerir checks de estado (CI).
   - Bloquear force pushes.

---

## 9) Estructura del proyecto

```
.
├─ .github/workflows/ci.yml
├─ backend/
│  ├─ manage.py
│  ├─ requirements.txt
│  ├─ pytest.ini
│  └─ src/
│     ├─ algos/
│     │  └─ functions.py               # (a completar)
│     └─ catalog/
│        ├─ models.py
│        ├─ serializers.py
│        ├─ views.py
│        ├─ urls.py
│        ├─ fixtures/products.json
│        ├─ tests/test_api.py          # tests del API
│        └─ migrations/0001_initial.py
├─ frontend/
│  ├─ package.json
│  ├─ vite.config.js
│  └─ src/
│     ├─ App.jsx
│     ├─ components/
│     │  ├─ SearchBar.jsx
│     │  └─ ProductList.jsx
│     ├─ hooks/useDebounce.js
│     ├─ __tests__/ProductList.test.jsx
│     └─ test/setup.js
├─ plantillas/
│  └─ score.json                        # plantilla de evaluación
├─ README.md
├─ RUBRICA.md                            # rúbrica detallada
└─ LICENSE
```

---

## 10) Notas para Windows (CRLF)

Si ves avisos de EOL (`LF will be replaced by CRLF`), puedes añadir un `.gitattributes` para normalizar:

```
* text=auto
*.py  eol=lf
*.js  eol=lf
*.jsx eol=lf
*.json eol=lf
*.yml eol=lf
*.md  eol=lf
*.sh  eol=lf
*.bat eol=crlf
*.ps1 eol=crlf
```

---

## 11) Licencia

Este repo usa **MIT License** (ver `LICENSE`).

---

## 12) Soporte

Si algo no corre o un test parece ambiguo, abre un **Issue** o descríbelo en tu **PR** con pasos para reproducir.
