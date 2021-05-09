from django.contrib import admin

# Register your models here.
from blog_v1.models import Post
from blog_v1.models import Professor
from blog_v1.models import Coordenaçao
from blog_v1.models import Funcionario
from blog_v1.models import Matricula
from blog_v1.models import Curso
from blog_v1.models import Aluno
from blog_v1.models import Turma
from blog_v1.models import Evento
from blog_v1.models import Biblioteca
from blog_v1.models import Calendario
from blog_v1.models import Duvida
from blog_v1.models import Lanche
from blog_v1.models import Cantina
from blog_v1.models import Comentario

admin.site.register(Post)
admin.site.register(Professor)
admin.site.register(Coordenaçao)
admin.site.register(Funcionario)
admin.site.register(Matricula)
admin.site.register(Curso)
admin.site.register(Aluno)
admin.site.register(Turma)
admin.site.register(Evento)
admin.site.register(Biblioteca)
admin.site.register(Calendario)
admin.site.register(Duvida)
admin.site.register(Lanche)
admin.site.register(Cantina)
admin.site.register(Comentario)