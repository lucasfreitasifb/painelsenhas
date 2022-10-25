from django.db import models

class Tipo(models.Model):
    id_tipo = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=45, null=False)


class StatusSenha(models.Model):
    id_status = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=45, null=False)

class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=45, null=False)

class Senha(models.Model):

    id_senha = models.IntegerField(primary_key=True)
    senha = models.IntegerField()
    hora_data = models.DateTimeField()
    categoria_id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    tipo_id_tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    status_senha_id_status_senha = models.ForeignKey(StatusSenha, on_delete=models.CASCADE)