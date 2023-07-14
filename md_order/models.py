from django.db import models
from md_member.models import MdUser
from md_store.models import MdStorM


class MdWeather(models.Model):
    weather_id = models.IntegerField(primary_key=True, db_comment='날씨분류ID')
    weather_name = models.CharField(max_length=10, db_comment='날씨분류명')

    class Meta:
        managed = False
        db_table = 'md_weather'
        db_table_comment = '날씨분류'


class MdBuck(models.Model):
    buck_id = models.AutoField(primary_key=True, db_comment='장바구니ID')
    user = models.ForeignKey(MdUser, models.DO_NOTHING, db_comment='회원ID')
    stor_m = models.ForeignKey(MdStorM, models.DO_NOTHING, db_comment='매장메뉴ID')
    buck_num = models.IntegerField(db_comment='주문수량')
    buck_reg_ts = models.DateTimeField(db_comment='등록일시')
    buck_del_ts = models.DateTimeField(blank=True, null=True, db_comment='삭제일시')
    buck_ord_ts = models.DateTimeField(blank=True, null=True, db_comment='주문일시')

    class Meta:
        managed = False
        db_table = 'md_buck'
        db_table_comment = '장바구니'


class MdOrdr(models.Model):
    ordr_id = models.AutoField(primary_key=True, db_comment='주문ID')
    user = models.ForeignKey(MdUser, models.DO_NOTHING, db_comment='회원ID')
    weather = models.ForeignKey(MdWeather, models.DO_NOTHING, db_comment='날씨분류ID')
    ordr_temp = models.IntegerField(db_comment='기온')
    ordr_ord_ts = models.DateTimeField(db_comment='주문일시')
    ordr_com_ts = models.DateTimeField(blank=True, null=True, db_comment='완료일시')

    class Meta:
        managed = False
        db_table = 'md_ordr'
        db_table_comment = '주문'


class MdOrdrM(models.Model):
    ordr_m_id = models.AutoField(primary_key=True, db_comment='주문메뉴ID')
    ordr = models.ForeignKey(MdOrdr, models.DO_NOTHING, db_comment='주문ID')
    stor_m = models.ForeignKey(MdStorM, models.DO_NOTHING, db_comment='매장메뉴ID')
    ordr_num = models.IntegerField(db_comment='주문수량')

    class Meta:
        managed = False
        db_table = 'md_ordr_m'
        db_table_comment = '주문메뉴'


