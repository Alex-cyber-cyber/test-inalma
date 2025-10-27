
import React from 'react'

export default function ProductList({ items }) {
  if (!items?.length) return <p>No hay resultados.</p>
  return (
    <ul role="list" style={{listStyle:'none', padding:0, marginTop:16}}>
      {items.map(p => (
        <li key={p.id} style={{display:'flex', justifyContent:'space-between', padding:'12px 8px', borderBottom:'1px solid #eee'}}>
          <span>{p.name}</span>
          <span>${Number(p.price).toFixed(2)}</span>
        </li>
      ))}
    </ul>
  )
}
