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
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata src/catalog/fixtures/products.json
pytest -q
python manage.py runserver 8000
