export default function SearchBar({ value = '', onChange }) {
  return (
    <input
      aria-label="search"
      placeholder="Buscar productos…"
      value={value}
      onChange={(e) => onChange?.(e.target.value)}
      style={{ width:'100%', padding:'10px 12px', borderRadius:8, border:'1px solid #ddd', marginBottom:12 }}
    />
  )
}