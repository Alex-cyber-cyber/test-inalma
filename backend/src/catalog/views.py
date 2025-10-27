
from rest_framework import generics, status
from rest_framework.response import Response
from django.db.models import Q
from .models import Product
from .serializers import ProductSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        qs = Product.objects.all()
        q = self.request.query_params.get("q")
        min_price = self.request.query_params.get("min_price")
        max_price = self.request.query_params.get("max_price")
        tags = self.request.query_params.get("tags")
        ordering = self.request.query_params.get("ordering")

        if q:
            qs = qs.filter(Q(name__icontains=q))

        if min_price is not None:
            try:
                qs = qs.filter(price__gte=float(min_price))
            except ValueError:
                pass

        if max_price is not None:
            try:
                qs = qs.filter(price__lte=float(max_price))
            except ValueError:
                pass

        if tags:
            requested = [t.strip().lower() for t in tags.split(",") if t.strip()]
            def has_all(obj_tags):
                obj_tags_lower = [str(t).lower() for t in (obj_tags or [])]
                return all(t in obj_tags_lower for t in requested)
            ids = [p.id for p in qs if has_all(p.tags)]
            qs = qs.filter(id__in=ids)

        allowed_order = {"price", "-price", "name", "-name"}
        if ordering in allowed_order:
            qs = qs.order_by(ordering)

        return qs

    def create(self, request, *args, **kwargs):
        name = (request.data.get("name") or "").strip()
        if not name:
            return Response({"name": ["Este campo es requerido."]}, status=status.HTTP_400_BAD_REQUEST)

        if Product.objects.filter(name__iexact=name).exists():
            return Response({"name": ["Ya existe un producto con ese nombre (insensible a mayúsculas)."]},
                            status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)
