from django.db import models
from md_member.models import MdUser
from md_store.models import MdStor


class MdFavorite(models.Model):
    fav_id = models.AutoField(primary_key=True, db_comment='즐겨찾기ID')
    user = models.ForeignKey(MdUser, models.DO_NOTHING, db_comment='회원ID')
    stor = models.ForeignKey(MdStor, models.DO_NOTHING, db_comment='매장ID')
    fav_reg_ts = models.DateTimeField(db_comment='등록일')

    class Meta:
        managed = False
        db_table = 'md_favorite'
        db_table_comment = '즐겨찾기'


