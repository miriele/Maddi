from django.db import models
from md_store.models import MdBjd


class MdSrch(models.Model):
    srch_id = models.AutoField(primary_key=True, db_comment='검색ID')
    user = models.ForeignKey('md_member.MdUser', models.DO_NOTHING, blank=True, null=True, db_comment='회원ID')
    bjd_code = models.ForeignKey(MdBjd, models.DO_NOTHING, db_column='bjd_code', db_comment='법정동코드')
    srch_word = models.CharField(max_length=60, db_comment='검색어')
    srch_ts = models.DateTimeField(db_comment='검색시각')

    class Meta:
        managed = False
        db_table = 'md_srch'
        db_table_comment = '검색통계'


