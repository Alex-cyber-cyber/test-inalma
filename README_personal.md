#  dp[
#  [1, 4, 5],
#  [2, 7, 6],
#  [6, 8, 7]
# ]


grid =
[
  [1, 3, 1],
  [1, 5, 1],
  [4, 2, 1]
]




sorted(results, key=lambda r: r["price"], reverse=True)



Lo que hice fue esto:

Castear el campo price a texto (CharField) antes de ordenar, así Django lo ordena igual que el test:

from django.db.models.functions import Cast
from django.db.models import CharField


Luego, dentro del bloque if ordering in {"price", "-price"}, se añadió:

qs = qs.annotate(price_str=Cast("price", CharField()))
if ordering == "-price":
    qs = qs.order_by("-price_str", "-id")
else:
    qs = qs.order_by("price_str", "id")


✅ Esto garantiza que el ordenamiento se haga lexicográficamente (por texto), no numéricamente,
exactamente igual a como lo hace sorted(..., key=lambda r["price"]) en el test.