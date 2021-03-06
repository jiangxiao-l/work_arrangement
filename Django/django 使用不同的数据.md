#  django 使用不同的数据库

## 1、不同APP使用不同的数据库

### 1.1 在settings.py文件里设置数据库连接

```Python
# 1. 设置过个数据库的连接
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'db1': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_advanced',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': 'root',
    }
}
# 2. 设置数据库的路由
DATABASES_APPS_MAPPING = {'app01': 'default','app02': 'db1'}

# 3. 配置路由文件 untitled(项目的目录)；database_app_router(py文件名);DatabaseAppsRouter(类名)
DATABASE_ROUTERS = ['untitled.database_app_router.DatabaseAppsRouter']
```

### 1.2 编写路由文件 database_app_router.py

```python
# -*- coding: utf-8 -*-
from django.conf import settings
 
DATABASE_MAPPING = settings.DATABASE_APPS_MAPPING
 
 
class DatabaseAppsRouter(object):
    """
    A router to control all database operations on models for different
    databases.
 
    In case an app is not set in settings.DATABASE_APPS_MAPPING, the router
    will fallback to the `default` database.
 
    Settings example:
 
    DATABASE_APPS_MAPPING = {'app01': 'db1', 'app02': 'db2'}
    """
 
    def db_for_read(self, model, **hints):
        """"Point all read operations to the specific database."""
        if model._meta.app_label in DATABASE_MAPPING:
            return DATABASE_MAPPING[model._meta.app_label]
        return None
 
    def db_for_write(self, model, **hints):
        """Point all write operations to the specific database."""
        if model._meta.app_label in DATABASE_MAPPING:
            return DATABASE_MAPPING[model._meta.app_label]
        return None
 
    def allow_relation(self, obj1, obj2, **hints):
        """Allow any relation between apps that use the same database."""
        db_obj1 = DATABASE_MAPPING.get(obj1._meta.app_label)
        db_obj2 = DATABASE_MAPPING.get(obj2._meta.app_label)
        if db_obj1 and db_obj2:
            if db_obj1 == db_obj2:
                return True
            else:
                return False
        return None
 
    # for Django 1.4 - Django 1.6
    def allow_syncdb(self, db, model):
        """Make sure that apps only appear in the related database.""" 
        if db in DATABASE_MAPPING.values():
            return DATABASE_MAPPING.get(model._meta.app_label) == db
        elif model._meta.app_label in DATABASE_MAPPING:
            return False
        return None
 
    # Django 1.7 - Django 1.11
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure that apps only appear in the related database.
        根据app_label的值只在相应的数据库中创建一个表，如果删除该def或
        不指定过滤条件，则一个Model会在每个数据库里都创建一个表。
        """
        if db in DATABASE_MAPPING.values():
            return DATABASE_MAPPING.get(app_label) == db
        elif app_label in DATABASE_MAPPING:
            return False
        return None
```

### 1.3 定义modle层

```python
# app01
from django.db import models
class Agent(models.Model):
    b_id = models.IntegerField()
    name = models.CharField(max_length=30)
    mobile_number = models.BigIntegerField()
    mobile_password_hash = models.CharField(max_length=80, blank=True, null=True)
    id_number = models.CharField(max_length=30)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    balance_frozen = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    # 待返还的金额(每年的最后一天，将此金额返还到可用余额里面) jxl 9.25
    balance_restitution = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0)
    guid = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'agent'


# app02 
from django.db import models


# Create your models here.
class TLDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        if self.auto_now or (self.auto_now_add and add):
            value = getattr(model_instance, self.attname)
            if not value:
                value = models.Func(function="NOW")
                setattr(model_instance, self.attname, value)
            return value
        else:
            # by pass the pre_save of TLDateTimeField
            return super(models.DateTimeField, self).pre_save(model_instance, add)
class RoleUser(models.Model):
    role_id = models.IntegerField()
    user_id = models.IntegerField()
    user_type = models.CharField(max_length=20)
    create_date = TLDateTimeField(auto_now_add=True, help_text="创建日期")
    modify_date = TLDateTimeField(auto_now=True, help_text="修改日期")

    class Meta:
        db_table = "role_user"

```



## 2、同一APP使用不同的数据库

```python
# 复制 “不同APP使用不同的数据库的方法”，因为需要用到不同的app，故需要创建多余的空的app
# 在此基础上设置modl层

from django.db import models

class Agent(models.Model):
    b_id = models.IntegerField()
    name = models.CharField(max_length=30)
    mobile_number = models.BigIntegerField()
    mobile_password_hash = models.CharField(max_length=80, blank=True, null=True)
    id_number = models.CharField(max_length=30)
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    balance_frozen = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    # 待返还的金额(每年的最后一天，将此金额返还到可用余额里面) jxl 9.25
    balance_restitution = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0)
    guid = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        # DATABASES_APPS_MAPPING = {'app01': 'default','app02': 'db1'}
        app_label = 'app01' # 制定使用的数据库 app01-->default(默认的数据库)
        db_table = 'agent'
        

class TLDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        if self.auto_now or (self.auto_now_add and add):
            value = getattr(model_instance, self.attname)
            if not value:
                value = models.Func(function="NOW")
                setattr(model_instance, self.attname, value)
            return value
        else:
            # by pass the pre_save of TLDateTimeField
            return super(models.DateTimeField, self).pre_save(model_instance, add)


class RoleUser(models.Model):
    role_id = models.IntegerField()
    user_id = models.IntegerField()
    user_type = models.CharField(max_length=20)
    create_date = TLDateTimeField(auto_now_add=True, help_text="创建日期")
    modify_date = TLDateTimeField(auto_now=True, help_text="修改日期")

    class Meta:
        # DATABASES_APPS_MAPPING = {'app01': 'default','app02': 'db1'}
        app_label = 'app02' # 制定使用的数据库 app02-->db1
        db_table = "role_user"

```

