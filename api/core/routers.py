from rest_framework import routers
from core.hello.viewsets import Hello
from core.summarize.viewsets import SummarizeViewSet

router = routers.SimpleRouter()

router.register(r"hello", Hello, basename="hello")
router.register(r"summarize", SummarizeViewSet, basename="summarize")

urlpatterns = [
    *router.urls
]