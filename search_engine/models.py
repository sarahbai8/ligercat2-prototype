from django.db import models

class Gene(models.Model):
    id = models.CharField(max_length=190, primary_key=True)
    name = models.CharField(max_length=255, null=True)
    short_description = models.TextField(null=True)
    description = models.TextField(null=True)
    chromosome_number = models.CharField(max_length=255, null=True)
    location = models.CharField(max_length=255, null=True)

    class Meta:
       db_table = 'gene'


class SNP(models.Model):
    id = models.CharField(max_length=190, primary_key=True)
    chromosome_number = models.CharField(max_length=255, null=True)
    observed_bases = models.CharField(max_length=255, null=True)
    genes = models.ManyToManyField(Gene, db_table='snp_to_gene')

    class Meta:
       db_table = 'snp'


class Article(models.Model):
    id = models.CharField(max_length=190, primary_key=True)
    title = models.TextField(null=True)
    description = models.TextField(null=True)
    journal_name = models.CharField(max_length=255, null=True)
    snps = models.ManyToManyField(SNP, db_table='article_to_snp')

    class Meta:
       db_table = 'article'
