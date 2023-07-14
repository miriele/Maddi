from django.db import models


class MdGen(models.Model):
    gen_id = models.IntegerField(primary_key=True, db_comment='성별ID')
    gen_name = models.CharField(max_length=10, db_comment='성별')

    class Meta:
        managed = False
        db_table = 'md_gen'
        db_table_comment = '성별'


class MdIntrT(models.Model):
    intr_t_id = models.IntegerField(primary_key=True, db_comment='관심사분류ID')
    intr_t_name = models.CharField(max_length=21, db_comment='관심사분류명')

    class Meta:
        managed = False
        db_table = 'md_intr_t'
        db_table_comment = '관심사분류'


class MdTastT(models.Model):
    tast_t_id = models.IntegerField(primary_key=True, db_comment='맛분류ID')
    tast_t_name = models.CharField(max_length=12, db_comment='맛분류명')

    class Meta:
        managed = False
        db_table = 'md_tast_t'
        db_table_comment = '맛분류'


class MdUAlgy(models.Model):
    u_algy_id = models.AutoField(primary_key=True, db_comment='사용자알러지ID')
    user = models.ForeignKey('MdUser', models.DO_NOTHING, db_comment='회원ID')
    algy_t = models.ForeignKey('md_store.MdAlgyT', models.DO_NOTHING, db_comment='알러지분류ID')

    class Meta:
        managed = False
        db_table = 'md_u_algy'
        db_table_comment = '사용자알러지'


class MdUDrnk(models.Model):
    u_drnk_id = models.AutoField(primary_key=True, db_comment='사용자음료ID')
    user = models.ForeignKey('MdUser', models.DO_NOTHING, db_comment='회원ID')
    drnk_t = models.ForeignKey('md_store.MdDrnkT', models.DO_NOTHING, db_comment='음료분류ID')

    class Meta:
        managed = False
        db_table = 'md_u_drnk'
        db_table_comment = '사용자음료'


class MdUDsrt(models.Model):
    u_dsrt_id = models.AutoField(primary_key=True, db_comment='사용자디저트ID')
    user = models.ForeignKey('MdUser', models.DO_NOTHING, db_comment='회원ID')
    dsrt_t = models.ForeignKey('md_store.MdDsrtT', models.DO_NOTHING, db_comment='디저트분류ID')

    class Meta:
        managed = False
        db_table = 'md_u_dsrt'
        db_table_comment = '사용자디저트'


class MdUIntr(models.Model):
    u_intr_id = models.AutoField(primary_key=True, db_comment='사용자관심사ID')
    user = models.ForeignKey('MdUser', models.DO_NOTHING, db_comment='회원ID')
    intr_t = models.ForeignKey(MdIntrT, models.DO_NOTHING, db_comment='관심사분류ID')

    class Meta:
        managed = False
        db_table = 'md_u_intr'
        db_table_comment = '사용자관심사'


class MdUTast(models.Model):
    u_tast_id = models.AutoField(primary_key=True, db_comment='사용자맛ID')
    user = models.ForeignKey('MdUser', models.DO_NOTHING, db_comment='회원ID')
    tast_t = models.ForeignKey(MdTastT, models.DO_NOTHING, db_comment='맛분류ID')

    class Meta:
        managed = False
        db_table = 'md_u_tast'
        db_table_comment = '사용자맛'


class MdUser(models.Model):
    user_id = models.CharField(primary_key=True, max_length=20, db_comment='회원ID')
    user_g = models.ForeignKey('MdUserG', models.DO_NOTHING, db_comment='회원등급ID')
    gen = models.ForeignKey(MdGen, models.DO_NOTHING, db_comment='성별ID')
    user_nick = models.CharField(unique=True, max_length=45, db_comment='닉네임')
    user_pass = models.CharField(max_length=20, db_comment='비밀번호')
    user_name = models.CharField(max_length=30, db_comment='회원이름')
    user_bir = models.DateField(db_comment='생년월일')
    user_img = models.CharField(max_length=50, db_comment='이미지')
    user_reg_ts = models.DateTimeField(db_comment='가입일시')
    user_ext_ts = models.DateTimeField(blank=True, null=True, db_comment='탈퇴일시')

    class Meta:
        managed = False
        db_table = 'md_user'
        db_table_comment = '회원'


class MdUserG(models.Model):
    user_g_id = models.IntegerField(primary_key=True, db_comment='회원등급ID')
    user_g_name = models.CharField(max_length=15, db_comment='등급명')

    class Meta:
        managed = False
        db_table = 'md_user_g'
        db_table_comment = '회원등급'


