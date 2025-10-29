
import React, { use, useEffect, useState } from 'react'
import SearchBar from './components/SearchBar.jsx'
import ProductList from './components/ProductList.jsx'

const API = import.meta.env.VITE_API_URL || 'http://localhost:8000/api'

export default function App() {
  const [products, setProducts] = useState([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const [query, setQuery] = useState('')

  const debounceRef = React.useRef(null);

  async function loadProducts(q = '') {
    setLoading(true); setError(null)
    try {
      const url = new URL(`${API}/products/`)
      if (q && q.trim() !== '') url.searchParams.set('q', q)
      const res = await fetch(url)
      if (!res.ok) throw new Error('Error al cargar productos')
      const data = await res.json()
      setProducts(Array.isArray(data) ? data : data.results || [])
    }catch (e) {
      setError(e.message || 'Error al cargar productos')
    }finally {
      setLoading(false)
    }
  }
  useEffect(() => {
    loadProducts(query)
  }, [])

  useEffect(() => {
    if(!query) return;
    if(debounceRef.current) clearTimeout(debounceRef.current);
    debounceRef.current = setTimeout(() => {
      loadProducts(query)
    }, 300)

    return () => {
      if(debounceRef.current) clearTimeout(debounceRef.current);
    }
  }, [query])

  return (
    <div style={{maxWidth: 840, margin: '32px auto', padding: '0 16px', fontFamily: 'system-ui, sans-serif'}}>
      <h1>Catálogo</h1>
      <p style={{opacity:.8}}>Buscar y listar productos desde el API de Django.</p>

      <SearchBar value={query} onChange={setQuery} />

      {loading && <p>Cargando...</p>}
      {error && <p style={{color:'crimson'}}>{error}</p>}
      {!loading && !error && <ProductList items={products} />}
    </div>
  )
}
