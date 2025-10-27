
import React, { useEffect, useState } from 'react'
import SearchBar from './components/SearchBar.jsx'
import ProductList from './components/ProductList.jsx'

const API = import.meta.env.VITE_API_URL || 'http://localhost:8000/api'

export default function App() {
  const [products, setProducts] = useState([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const [query, setQuery] = useState('')

  useEffect(() => {
    let canceled = false
    async function load() {
      setLoading(true); setError(null)
      try {
        const url = new URL(`${API}/products/`)
        if (query) url.searchParams.set('q', query)
        const res = await fetch(url)
        if (!res.ok) throw new Error('Error al cargar productos')
        const data = await res.json()
        if (!canceled) setProducts(data.results || [])
      } catch (e) {
        if (!canceled) setError(e.message)
      } finally {
        if (!canceled) setLoading(false)
      }
    }
    load()
    return () => { canceled = true }
  }, [query])

  return (
    <div style={{maxWidth: 840, margin: '32px auto', padding: '0 16px', fontFamily: 'system-ui, sans-serif'}}>
      <h1>Catálogo</h1>
      <p style={{opacity:.8}}>Buscar y listar productos desde el API de Django.</p>
      <SearchBar onChange={setQuery} />
      {loading && <p>Cargando...</p>}
      {error && <p style={{color:'crimson'}}>{error}</p>}
      {!loading && !error && <ProductList items={products} />}
    </div>
  )
}
