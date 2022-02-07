#
# 1. property: class
#   - 特性是用于管理(包含业务)实例属性的类属性.
#   - 特性是覆盖型描述符.
#   - property(fget=None, fset=None, fdel=None, doc=None)
#   - 在不改变类接口的前提下(统一访问原则), 使用存取方法修改数据属性.
#   - 为实例添加创建的属性可能会遮盖类属性/方法, 但是不会遮盖 property: 这个问题是Python字典不能像Js对象那样访问的原因.
# 2. __dict__: 如果类没有声明__slots__属性, 则它存储对象的属性.
# 3. obj.attr
#   - 从 obj.__class__ 开始查找有没有同名特性, 如果没有 ->
#   - 从 实例中寻找
# 4. globals().get(cls_name, DbRecord): 从模块的全局作用域中获取名称对应的对象.
# 5. 抽象特性的两种方式: 使用特性工厂函数, 或者使用描述符类.
# 6. 函数和类都是可调用对象. 只要能返回新的可调用对象, 代替被装饰的函数, 二者都可以作为装饰器.
# 7. vars(obj) 返回 __dict__ 属性. 如果没有参数, 则表示本地作用域字典.
# 8. __class__: type(obj)
# 9. __dict__: 存储对象/类的可写属性. 包含该属性的对象, 可以随时随意设置新属性. 可以使用该属性跳过特殊方法的调用.
# 10. dir(): 列出对象的大多数属性.
# 11. getattr(): 获取属性, 可能来自对象所属的类或者超类.
# 12. hasattr()
# 13. setattr()
# 14. __getattr__(): 仅当获取指定属性失败, 搜索过obj, class, 和超类之后调用.
# 15. __getattribute__(): 获取属性时调用. 特殊属性和特殊方法除外. getattr/hasattr会触发. 如果查找不到会调用__getattr__.
# 16. __setattr__(): 点号和setattr()会触发.

from collections import abc
import keyword


class FrozenJSON:
    """
    使用点语法访问字典
    """
    def __new__(cls, arg):
        """
        __new__ 可以返回其他类的实例, 此时, 解释器不会调用__init__.
        """
        if isinstance(arg, abc.Mapping):
            return super().__new__(cls)  # 构建 FrozenJSON 实例
        elif isinstance(arg, abc.MutableSequence):
            return [cls(item) for item in arg]
        else:
            return arg

    def __init__(self, mapping):
        # self.__data = dict(mapping)
        self.__data = {}
        for key, value in mapping.items():
            if keyword.iskeyword(key):  # 检查是否为关键字
                key += '_'
            self.__data[key] = value

    def __getattr__(self, name):
        """
        1. 仅在实例, 类, 超类中找不到指定的属性时, 才会调用该方法.
        2. d = {'a': 1} hasattr(d, 'a') False: 元素非属性.
        """
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJSON.build(self.__data[name])

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):  # 判断字典
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):  # 判断列表
            return [cls.build(item) for item in obj]
        else:
            return obj


class LineItem:
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight  # 走 setter
        self.price = price

    def subtotal(self):
        return self.weight * self.price

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value > 0:
            self.__weight = value
        else:
            raise ValueError('value must be > 0')


if __name__ == '__main__':
    print('🚀')

    print('🌺')