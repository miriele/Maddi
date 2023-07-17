from django.db import models


class MdAlgyT(models.Model):
    algy_t_id = models.SmallIntegerField(primary_key=True, db_comment='알러지분류ID')
    algy_t_name = models.CharField(max_length=15, db_comment='알러지분류명')

    class Meta:
        managed = False
        db_table = 'md_algy_t'
        db_table_comment = '알러지분류'


class MdAreaT(models.Model):
    area_t_id = models.IntegerField(primary_key=True, db_comment='면적분류ID')
    area_t_name = models.CharField(max_length=10, db_comment='면적분류명')
    area_t_min = models.SmallIntegerField(db_comment='면적 min')
    area_t_max = models.SmallIntegerField(db_comment='면적 max')

    class Meta:
        managed = False
        db_table = 'md_area_t'
        db_table_comment = '매장면적타입'


class MdBjd(models.Model):
    bjd_code = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0, db_comment='법정동코드')
    bjd_name = models.CharField(max_length=80, db_comment='법정동명')

    class Meta:
        managed = False
        db_table = 'md_bjd'
        db_table_comment = '법정동코드'


class MdDrnkT(models.Model):
    drnk_t_id = models.SmallIntegerField(primary_key=True, db_comment='음료분류ID')
    drnk_t_name = models.CharField(max_length=30, db_comment='음료분류명')

    class Meta:
        managed = False
        db_table = 'md_drnk_t'
        db_table_comment = '음료분류'


class MdDsrtT(models.Model):
    dsrt_t_id = models.SmallIntegerField(primary_key=True, db_comment='디저트분류ID')
    dsrt_t_name = models.CharField(max_length=20, db_comment='디저트분류명')

    class Meta:
        managed = False
        db_table = 'md_dsrt_t'
        db_table_comment = '디저트분류'


class MdIce(models.Model):
    ice_t_id = models.IntegerField(primary_key=True, db_comment='아이스분류ID')
    ice_t_name = models.CharField(max_length=10, db_comment='아이스타입명')

    class Meta:
        managed = False
        db_table = 'md_ice'
        db_table_comment = '아이스분류'


class MdMAlgy(models.Model):
    m_algy_id = models.SmallAutoField(primary_key=True, db_comment='메뉴알러지ID')
    menu = models.ForeignKey('MdMenu', models.DO_NOTHING, db_comment='메뉴ID')
    algy_t = models.ForeignKey(MdAlgyT, models.DO_NOTHING, db_comment='알러지분류ID')

    class Meta:
        managed = False
        db_table = 'md_m_algy'
        db_table_comment = '메뉴알러지'


class MdMenu(models.Model):
    menu_id = models.IntegerField(primary_key=True, db_comment='메뉴ID')
    dsrt_t = models.ForeignKey(MdDsrtT, models.DO_NOTHING, blank=True, null=True, db_comment='디저트분류ID')
    drnk_t = models.ForeignKey(MdDrnkT, models.DO_NOTHING, blank=True, null=True, db_comment='음료분류ID')
    menu_name = models.CharField(max_length=60, db_comment='메뉴명')
    menu_cal = models.SmallIntegerField(db_comment='칼로리')
    menu_info = models.CharField(max_length=300, db_comment='메뉴소개')
    menu_img = models.ImageField(max_length=30, blank=True, null=True, db_comment='메뉴이미지', upload_to="images")

    class Meta:
        managed = False
        db_table = 'md_menu'
        db_table_comment = '메뉴'


class MdMenuT(models.Model):
    menu_t_id = models.IntegerField(primary_key=True, db_comment='메뉴타입ID')
    menu_t_name = models.CharField(max_length=15, db_comment='메뉴타입명')

    class Meta:
        managed = False
        db_table = 'md_menu_t'
        db_table_comment = '메뉴타입 : 1 : 일반\r\n2 : 시그니처'


class MdStor(models.Model):
    stor_id = models.AutoField(primary_key=True, db_comment='매장ID')
    stor_t = models.ForeignKey('MdStorT', models.DO_NOTHING, db_comment='매장구분ID')
    user = models.ForeignKey('md_member.MdUser', models.DO_NOTHING, blank=True, null=True, db_comment='회원ID')
    bjd_code = models.ForeignKey(MdBjd, models.DO_NOTHING, db_column='bjd_code', db_comment='법정동코드')
    area_t = models.ForeignKey(MdAreaT, models.DO_NOTHING, db_comment='면적분류ID')
    stor_img = models.ImageField(max_length=100, db_comment='이미지', upload_to="images")
    stor_name = models.CharField(max_length=50, db_comment='매장명')
    stor_addr = models.CharField(max_length=200, db_comment='매장주소')
    stor_lati = models.DecimalField(max_digits=19, decimal_places=15, blank=True, null=True, db_comment='위치-위도')
    stor_long = models.DecimalField(max_digits=19, decimal_places=15, blank=True, null=True, db_comment='위치-경도')
    stor_tel = models.CharField(max_length=20, blank=True, null=True, db_comment='전화번호')
    stor_num = models.CharField(max_length=20, blank=True, null=True, db_comment='사업자등록번호')

    class Meta:
        managed = False
        db_table = 'md_stor'
        db_table_comment = '매장'


class MdStorM(models.Model):
    stor_m_id = models.AutoField(primary_key=True, db_comment='매장메뉴ID')
    stor = models.ForeignKey(MdStor, models.DO_NOTHING, db_comment='매장ID')
    menu = models.ForeignKey(MdMenu, models.DO_NOTHING, db_comment='메뉴ID')
    ice_t = models.ForeignKey(MdIce, models.DO_NOTHING, db_comment='아이스분류ID')
    menu_t = models.ForeignKey(MdMenuT, models.DO_NOTHING, db_comment='메뉴타입ID')
    stor_m_pric = models.SmallIntegerField(db_comment='가격')
    stor_m_name = models.CharField(max_length=60, db_comment='매장메뉴명')
    stor_m_cal = models.SmallIntegerField(db_comment='매장메뉴칼로리')
    stor_m_info = models.CharField(max_length=600, db_comment='매장메뉴소개')
    stor_m_img = models.ImageField(max_length=100, db_comment='매장메뉴이미지', upload_to="images")

    class Meta:
        managed = False
        db_table = 'md_stor_m'
        db_table_comment = '매장메뉴'


class MdStorReg(models.Model):
    reg_id = models.AutoField(primary_key=True, db_comment='매장등록신청ID')
    user = models.ForeignKey('md_member.MdUser', models.DO_NOTHING, db_comment='회원ID')
    stor = models.ForeignKey(MdStor, models.DO_NOTHING, db_comment='매장ID')
    reg_num = models.CharField(max_length=40, db_comment='사업자등록번호')
    reg_img = models.CharField(max_length=50, db_comment='사업자등록증경로')
    reg_sub_ts = models.DateTimeField(db_comment='신청일시')
    reg_con_ts = models.DateTimeField(blank=True, null=True, db_comment='승일일시')

    class Meta:
        managed = False
        db_table = 'md_stor_reg'
        db_table_comment = '매장등록신청'


class MdStorT(models.Model):
    stor_t_id = models.IntegerField(primary_key=True, db_comment='매장구분ID')
    stor_t_name = models.CharField(max_length=60, db_comment='구분명')

    class Meta:
        managed = False
        db_table = 'md_stor_t'
        db_table_comment = '매장구분 : 1 : 개인\r\n2 : 스타벅스\r\n3 : 커피빈\r\n4 : 바나프레소'


