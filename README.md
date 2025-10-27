
# Prueba Técnica — Lógica + Python + Django + React

**Tiempo sugerido:** 4 a 6 horas (puede repartirse en 2 días).  
**Nivel objetivo:** Semi–Senior (ajustable).  
**Stack:** Python 3.11+, Django 4.2+, DRF, React (Vite), Vitest.

## Objetivo
1) Resolver ejercicios de **lógica de programación** en Python (tests unitarios).  
2) Implementar endpoints en **Django REST** para un catálogo de productos con filtros y validaciones.  
3) Construir una UI en **React** que consuma el API con búsqueda y filtros (tests de componentes).

> ⚠️ Los tests están **fallando** al inicio. Tu trabajo es hacerlos pasar sin romper estilos o contratos públicos.

---

## Entregables del candidato
- Código funcional con **todos los tests en verde** (`backend` y `frontend`).
- Commits claros y un **README_personal.md** explicando decisiones.
- (Opcional) Cobertura de pruebas mínima 80% en `backend/` y `frontend/`.

## Cómo correr todo (rápido)
Requisitos: Python 3.11+, Node 18+, pip, npm.

### 1) Backend (Django + DRF)
```bash
cd backend
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata src/catalog/fixtures/products.json
pytest -q
python manage.py runserver 8000
```
API en `http://localhost:8000/api/products/`

### 2) Frontend (React)
```bash
cd frontend
npm install
npm test
npm run dev
```
Web en `http://localhost:5173` (ya consume `http://localhost:8000`).

---

## Rúbrica de evaluación (resumen)
- Lógica 25, Python 20, React 20, GitHub 15, Buenas prácticas 10, Uso de IA 10.  
- Ver **RUBRICA.md** para el detalle y `plantillas/score.json` para calificar rápido.

---

## Desafíos

### A. Lógica (Python)
Implementa funciones en `backend/src/algos/functions.py` para pasar `backend/tests/test_algos.py`:

- `is_palindrome(s: str) -> bool`
- `compress_ranges(nums: list[int]) -> list[str]` (p.ej. `[1,2,3,5,7,8] -> ["1-3","5","7-8"]`)
- `min_path_sum(grid: list[list[int]]) -> int` (camino mínimo con solo derecha/abajo)
- `top_k_frequent_words(words: list[str], k: int) -> list[str]` (frecuencia y orden alfabético)

### B. API (Django + DRF)
Completa el API de `Product` en `backend/src/catalog/` para pasar `backend/src/catalog/tests/test_api.py`:

- `GET /api/products/?q=&min_price=&max_price=&tags=&ordering=`  
- `POST /api/products/` con validación de nombre **case-insensitive único** y precio ≥ 0.
- Paginación por 10 y ordenación (`price`, `-price`, `name`, `-name`).

### C. UI (React)
Termina los componentes en `frontend/src/` para pasar `frontend/src/__tests__/ProductList.test.jsx`:

- `SearchBar` con debounce 300 ms.
- `ProductList` que muestra, filtra y ordena resultados del API.
- Manejo de loading/errors básico.

---

## Cómo validar
- `backend`: `pytest -q`
- `frontend`: `npm test`
- **Todo OK** si ambos quedan en verde.

**Documentos útiles:** consulta la [RÚBRICA](./RUBRICA.md) y la plantilla de calificación en `plantillas/score.json`.
