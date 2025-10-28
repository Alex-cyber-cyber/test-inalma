from collections import Counter
from typing import List, Iterable

def is_palindrome(s: str) -> bool:
    """Devuelve True si s es palíndromo (ignorando espacios y mayúsculas y no alfanuméricos)."""
    if s is None:
        return False
    cleaned = [ch.lower() for ch in s if ch.isalnum()]
    i, j = 0, len(cleaned) - 1
    while i < j:
        if cleaned[i] != cleaned[j]:
            return False
        i += 1
        j -= 1
    return True

def compress_ranges(nums: Iterable[int]) -> List[str]:
    """Comprime secuencias consecutivas:
    [1,2,3,5,7,8] -> ["1-3","5","7-8"]
    """
    arr = sorted(set(nums))
    if not arr:
        return []
    res: List[str] = [] # Lista de rangos comprimidos, ej. ["1-3","5","7-8"]
    start = prev = arr[0] # Inicio y previo del rango actual
    for n in arr[1:]:
        if n == prev + 1: # validacion de que el numero es consecutivo.
            prev = n
            continue
        res.append(f"{start}-{prev}" if start != prev else f"{start}")
        start = prev = n
    res.append(f"{start}-{prev}" if start != prev else f"{start}")
    return res


def min_path_sum(grid: List[List[int]]) -> int:
    """Suma mínima de camino desde (0,0) a (n-1,m-1) moviéndose solo derecha/abajo."""
    if not grid or not grid[0]:
        return 0 # Caso base: grid vacía
    n, m = len(grid), len(grid[0]) # Dimensiones del grid Columnas y filas
    dp = [[0] * m for _ in range(n)] # dp[i][j] = suma mínima para llegar 
    dp[0][0] = grid[0][0] # Inicialización
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + grid[i][0] # Primera columna (única opción: desde arriba)
    for j in range(1, m): 
        dp[0][j] = dp[0][j - 1] + grid[0][j] # Primera fila (única opción: desde la izquierda)
    for i in range(1, n):
        for j in range(1, m): 
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j] # Mínimo entre arriba y izquierda
    return dp[n - 1][m - 1]


def top_k_frequent_words(words: List[str], k: int) -> List[str]:
    """Top k palabras por frecuencia; empate por orden alfabético ascendente."""
    if k <= 0 or not words:
        return []
    cnt = Counter(words)
    ordenadas = sorted(cnt.items(), key=lambda x: (-x[1], x[0]))
    return [palabra for palabra, _ in ordenadas[:k]]






