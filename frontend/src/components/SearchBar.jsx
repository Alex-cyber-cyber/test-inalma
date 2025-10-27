
import React, { useEffect, useState } from 'react'
import useDebounce from '../hooks/useDebounce.js'

export default function SearchBar({ onChange }) {
  const [value, setValue] = useState('')
  const debounced = useDebounce(value, 300)

  useEffect(() => { onChange?.(debounced) }, [debounced])

  return (
    <input
      aria-label="search"
      placeholder="Buscar..."
      value={value}
      onChange={e => setValue(e.target.value)}
      style={{width:'100%', padding:'12px', border:'1px solid #ccc', borderRadius:8}}
    />
  )
}
