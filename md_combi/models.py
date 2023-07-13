from django.db import models


class MdCLike(models.Model):
    like_id = models.AutoField(primary_key=True, db_comment='LikeID')
    user = models.ForeignKey('MdUser', models.DO_NOTHING, db_comment='회원ID')
    comb = models.ForeignKey('MdComb', models.DO_NOTHING, db_comment='추천조합ID')
    like_reg_ts = models.DateTimeField(db_comment='등록일')

    class Meta:
        managed = False
        db_table = 'md_c_like'
        db_table_comment = '추천조합_Like'


class MdComb(models.Model):
    comb_id = models.AutoField(primary_key=True, db_comment='추천조합ID')
    user = models.ForeignKey('MdUser', models.DO_NOTHING, db_comment='회원ID')
    comb_tit = models.CharField(max_length=90, db_comment='제목')
    comb_nop = models.IntegerField(db_comment='인원수')
    comb_cont = models.TextField(db_comment='조합내용')
    comb_img = models.CharField(max_length=30, blank=True, null=True, db_comment='이미지경로')
    comb_reg_ts = models.DateTimeField(db_comment='작성일시')

    class Meta:
        managed = False
        db_table = 'md_comb'
        db_table_comment = '추천조합'


class MdCombM(models.Model):
    comb_m_id = models.AutoField(primary_key=True, db_comment='조합메뉴ID')
    comb = models.ForeignKey(MdComb, models.DO_NOTHING, db_comment='추천조합ID')
    menu = models.ForeignKey('MdMenu', models.DO_NOTHING, db_comment='메뉴ID')

    class Meta:
        managed = False
        db_table = 'md_comb_m'
        db_table_comment = '조합메뉴'


class MdCombR(models.Model):
    c_reply_id = models.AutoField(primary_key=True, db_comment='댓글ID')
    comb = models.ForeignKey(MdComb, models.DO_NOTHING, db_comment='추천조합ID')
    user = models.ForeignKey('MdUser', models.DO_NOTHING, db_comment='회원ID')
    c_reply_cont = models.CharField(max_length=300, db_comment='댓글내용')
    c_reply_ts = models.DateTimeField(db_comment='댓글작성일')

    class Meta:
        managed = False
        db_table = 'md_comb_r'
        db_table_comment = '추천조합댓글'


