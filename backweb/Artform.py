from django import forms

class Artform(forms.Form):
    title = forms.CharField(min_length=5, required=True, error_messages={
                            'required': '文章标题必填',
                            'min_length': '文章内容不能少于5个字符'
    })
    desc = forms.CharField(min_length=5, required=True, error_messages={
                            'required': '描述必填',
                            'min_length': '描述不能少于5个字符'
    })
    content = forms.CharField(required=True, error_messages={
                            'required': '文章内容必填'
    })
    category = forms.CharField(required=True, error_messages={
                            'required': '文章类型必填'
    })
    icon = forms.ImageField(required=True, error_messages={
                            'required': '文章图片必填'
    })


class Editform(forms.Form):
    title = forms.CharField(min_length=2, required=True, error_messages={
        'required': '文章标题必填',
        'min_length': '文章内容不能少于5个字符'
    })
    desc = forms.CharField(min_length=5, required=True, error_messages={
        'required': '描述必填',
        'min_length': '描述不能少于5个字符'
    })
    content = forms.CharField(required=True, error_messages={
        'required': '文章内容必填'
    })
    category = forms.CharField(required=True, error_messages={
        'required': '文章类型必填'
    })
    icon = forms.ImageField(required=True)
