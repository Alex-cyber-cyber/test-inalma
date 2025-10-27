
import { render, screen, waitFor } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import App from '../App.jsx'

const mockData = {
  count: 2,
  results: [
    { id: 1, name: 'Monitor', price: 299.99, tags: ['tech','pc'] },
    { id: 2, name: 'Mouse', price: 20.00, tags: ['tech','accessories'] }
  ]
}

beforeEach(() => {
  global.fetch = vi.fn(async () => ({
    ok: true,
    json: async () => mockData
  }))
})

afterEach(() => {
  vi.restoreAllMocks()
})

it('muestra productos y permite buscar con debounce', async () => {
  render(<App />)

  await waitFor(() => expect(screen.getByText('Monitor')).toBeInTheDocument())
  expect(screen.getByText('Mouse')).toBeInTheDocument()

  const input = screen.getByLabelText('search')
  await userEvent.type(input, 'mon')
  await new Promise(r => setTimeout(r, 350))

  expect(fetch).toHaveBeenCalledTimes(2)
  const lastCallUrl = new URL(fetch.mock.calls.at(-1)[0])
  expect(lastCallUrl.searchParams.get('q')).toBe('mon')
})
