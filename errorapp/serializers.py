from rest_framework import serializers

# 定义序列化器类 跟模型moles对应的
from errorapp.models import Employeel
from drf_day01 import settings


# 序列化器
class EmployeeSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    # gender = serializers.IntegerField()
    # pic = serializers.ImageField()

    # 自定义字段 返回盐  使用SerializerMethodField来定义
    salt = serializers.SerializerMethodField()
    def get_salt(self, obj):
        return "salt"

    gender = serializers.SerializerMethodField()
    def get_gender(self, obj):
        return obj.get_gender_display()

    pic = serializers.SerializerMethodField()
    def get_pic(self, obj):
        # return "%s%s" % ("http://127.0.0.1:8000/media/", str(obj.pic))
        return "%s%s%s" % ("http://127.0.0.1:8000", settings.MEDIA_URL, str(obj.pic))


# 反序列化器
class EmployeeDeSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=5,
        min_length=2,
        error_messages={
            "max_length": "长度不能大于五",
            "min_length": "长度不能小于二",
        }
    )
    password = serializers.CharField(required=False)
    phone = serializers.CharField()
    def create(self, validated_data):
        return Employeel.objects.create(**validated_data)