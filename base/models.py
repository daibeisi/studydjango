from django.db import models


# Create your models here.
class BaseModel(models.Model):
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True, help_text='创建时间')
    edit_time = models.DateTimeField(verbose_name="修改时间", auto_now=True, help_text='修改时间')
    create_user_id = models.IntegerField(null=True, verbose_name='创建人id', help_text='创建人id')
    update_user_id = models.IntegerField(null=True, verbose_name='更新人id', help_text='更新人id')
    delete_user_id = models.IntegerField(null=True, verbose_name='删除人id', help_text='删除人id')

    class Meta:
        # 声明为抽象基类后，BaseModel不会单独创建一个表，只有在被继承的子类中自动添加BaseModel中的字段
        abstract = True

    # 序列化器中重写create方法
    def create(self, validated_data):
        del validated_data['role_name']
        user = super().create(validated_data)
        # 对密码进行加密
        password = validated_data.get('password')
        if password:  # 填写密码,加密
            user.set_password(password)
        else:  # 未填写密码或传空串,使用系统默认密码,888888
            user.password = "SYSTEM_USER_DEFAULT_PASSWORD"
        # 记录创建人用户id
        create_user_id = self.context.get('request').user.id
        user.create_user_id = create_user_id
        user.save()
        return user

    # 序列化器中重写update方法
    def update(self, instance, validated_data):
        if validated_data.get('role_name'):
            del validated_data['role_name']
        # 对密码进行加密
        password = validated_data.get('password')
        if password:  # 填写密码,加密
            instance.set_password(password)
        else:  # 未填写密码或传空串,使用系统默认密码,888888
            instance.password = "SYSTEM_USER_DEFAULT_PASSWORD"
        # 记录更新人用户id
        update_user_id = self.context.get('request').user.id
        instance.update_user_id = update_user_id
        return super().update(instance, validated_data)

    # view中重写destroy方法
    def destroy(self, request, *args, **kwargs):
        """重写destroy方法,记录删除人用户id"""
        delete_user_id = request.user.id
        instance = self.get_object()
        instance.delete_user_id = delete_user_id
        instance.save()
        return super().destroy(request, *args, **kwargs)
