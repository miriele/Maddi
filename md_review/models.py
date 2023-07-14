from django.db import models
from md_order.models import MdOrdr


class MdTagG(models.Model):
    tag_g_id = models.IntegerField(primary_key=True, db_comment='태그그룹ID')
    tag_g_name = models.CharField(max_length=15, db_comment='태그그룹명')

    class Meta:
        managed = False
        db_table = 'md_tag_g'
        db_table_comment = '태그그룹'


class MdTag(models.Model):
    tag_id = models.SmallIntegerField(primary_key=True, db_comment='태그ID')
    tag_g = models.ForeignKey(MdTagG, models.DO_NOTHING, db_comment='태그그룹ID')
    tag_name = models.CharField(max_length=50, db_comment='태그명')

    class Meta:
        managed = False
        db_table = 'md_tag'
        db_table_comment = '태그'


class MdReview(models.Model):
    rev_id = models.AutoField(primary_key=True, db_comment='리뷰ID')
    ordr = models.ForeignKey(MdOrdr, models.DO_NOTHING, db_comment='주문ID')
    rev_star = models.DecimalField(max_digits=2, decimal_places=1, db_comment='리뷰별점')
    rev_ts = models.DateTimeField(db_comment='작성일시')
    rev_cont = models.CharField(max_length=300, blank=True, null=True, db_comment='리뷰내용')
    rev_img = models.CharField(max_length=30, blank=True, null=True, db_comment='이미지경로')

    class Meta:
        managed = False
        db_table = 'md_review'
        db_table_comment = '리뷰'


class MdRevT(models.Model):
    rev_t_id = models.AutoField(primary_key=True, db_comment='리뷰태그ID')
    rev = models.ForeignKey(MdReview, models.DO_NOTHING, db_comment='리뷰ID')
    tag = models.ForeignKey(MdTag, models.DO_NOTHING, db_comment='태그ID')

    class Meta:
        managed = False
        db_table = 'md_rev_t'
        db_table_comment = '리뷰태그'


