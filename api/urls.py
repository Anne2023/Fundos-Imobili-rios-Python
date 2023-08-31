from rest_framework.routers import DefaultRouter
from api.views import FundoImobiliarioViewsSet


app_name = 'api' #é necessario para dar contexto ás ULs geradas. Esse parametro especifica os nameespace das URLConfs adicionadas

router = DefaultRouter(trailing_slash=False) # é o router que escolhemos para ageração automatica das URLS. o oarametro 'trailing_slash' especificaqu não é necessario o usa de barras// no final da URl
router.register(r'fundos', FundoImobiliarioViewsSet) #o método 'register' recebe dois parametros: o primeiro é prefixo que serausado na URL (no nosso caso: http://localhost:8000/fundos) e o segundo é a 'view' que ira responder as URLs desse app prefixo

urlpatterns = router.urls # utilizamos para expor as URLs desse app