from django.db import models
from md_store.models import MdBjd


class MdSrch(models.Model):
    srch_id = models.AutoField(primary_key=True, db_comment='�˻�ID')
    user = models.ForeignKey('md_member.MdUser', models.DO_NOTHING, db_comment='ȸ��ID')
    bjd_code = models.ForeignKey(MdBjd, models.DO_NOTHING, db_column='bjd_code', db_comment='�������ڵ�')
    srch_word = models.CharField(max_length=60, db_comment='�˻���')
    srch_ts = models.DateTimeField(db_comment='�˻��ð�')

    class Meta:
        managed = False
        db_table = 'md_srch'
        db_table_comment = '�˻����'


