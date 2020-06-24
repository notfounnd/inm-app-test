from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import empregados.views

urlpatterns = [
    path('', empregados.views.lista_empregados, name='lista_empregados'),
    path('admin/', admin.site.urls),
    path('empregados/', empregados.views.lista_empregados, name='lista_empregados'),
    path('empregados/new_empregado', empregados.views.new_empregado, name='new_empregado'),
    path('accounts/', include('accounts.urls')),
    path('empregados/edit/<int:emp_id>', empregados.views.edit, name='edit'),
    path('empregados/delete/<int:emp_id>', empregados.views.delete_empregado, name='delete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
