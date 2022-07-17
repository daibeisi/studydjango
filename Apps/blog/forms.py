from django import forms
from . import models
from django.core.exceptions import ValidationError

class reg_form(forms.Form):
    # 定义了username字段类型为CharField,通过error_messages设置对应出错类型的文字提示，widget设置了字段在页面表现的形式
    username=forms.CharField(
        max_length=20,
        label='登录账号',
        error_messages={
            "max_length":"登录账号不能超过20位",
            "required":"登录账号不能为空"
        },
        widget=forms.widgets.TextInput(
            # attrs属性是字典类型，设置“class”为“form-control”，这是Bootstrap样式类，是为了同Bootstrap框架的样式类一致
            attrs={"class":"form-control"},
        )
    )
    password=forms.CharField(
        min_length=6,
        label='密码',
        error_messages={
            'min_length':'密码最少6位',
            "required":"密码不能为空",
        },
        widget=forms.widgets.PasswordInput(
            attrs={'class':'form-control'},
            # 当render_value=True，表单数据校验不通过，重新返回页面时这个字段的输入还在，没有在页面刷新的过程中被清空
            render_value=True,
        )
    )
    repassword = forms.CharField(
        min_length=6,
        label='确认密码',
        error_messages={
            'min_length': '密码最少6位',
            "required": "密码不能为空",
        },
        widget=forms.widgets.PasswordInput(
            attrs={'class': 'form-control'},
            render_value=True,
        )
    )
    nikename=forms.CharField(
        max_length=20,
        required=False,
        label='姓名',
        error_messages={
            'max_length':'姓名长度不能超过20位',
        },
        # 如果不输入nickname，默认值为“无名氏”
        initial='无名氏',
        widget=forms.widgets.TextInput(
            attrs={'class':'form-control'}
        )
    )
    # 设置email为EmailField类型，实际上还是字符类型，但是增加了邮箱的格式校验功能
    email=forms.EmailField(
        label='邮箱',
        error_messages={
            'invalid':'邮箱格式不对',
            'required':'邮箱不能为空',

        },
        widget=forms.widgets.EmailInput(
            attrs={'class': 'form-control',}
        )
    )
    telephone=forms.CharField(
        label='联系电话',
        required=False,
        error_messages={
            'max_length':'最大长度不超过11位',
        },
        widget=forms.widgets.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    # head_img为ImageField类型，在页面上生成<input type="file">标签
    head_img=forms.ImageField(
        label='头像',
        widget=forms.widgets.FileInput(
            # 在attrs中设置style为display:none是为了在页面中不显示这个标签
            attrs={'style': "display: none"}
        )
    )

    # 定义一个校验字段的函数，校验字段函数的命名是有规则的，形式：clean_字段名()
    def clean_username(self): #重写username字段校验函数
        # 取得字段值，clean_data保存着通过第一步is_valid()校验的各字段值，是字典类型
        uname=self.cleaned_data.get('username')
        users = models.BlogUser.objects.filter(username=uname)
        if users:
            # 如果有同记录，增加一条错误信息给该字段的error属性
            self.add_error('username',ValidationError('登录账号已存在!'))
        else:
            return uname

    def clean_repassword(self):
        passwd=self.cleaned_data.get('password')
        repasswd=self.cleaned_data.get('repassword')
        if repasswd and repasswd != passwd:
            self.add_error('repassword', ValidationError('两次录入密码不一致'))
        else:
            return repasswd