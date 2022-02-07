# 1. descriptor
#   - 描述符是对多个属性运行相同存取逻辑的一种方式.
#   - 描述符是实现了特定协议的类, 包括__get__, __set__, __delete__.
#   - property类实现了完整的描述符协议.
#   - classmethod, staticmethod装饰器都用到了描述符.
#   - 用法: 创建一个描述符实例, 作为另一个类的类属性.
# 2. 覆盖型描述符
#   - 描述符的__set__方法使用托管实例中的同名属性覆盖了要设置的属性.
# 3. Python存取属性的方式不对等.
# 4. 非覆盖型描述符
#   - 没有实现__set__方法的描述符.
#   - 如果设置了同名的实例属性, 描述符会被遮盖.
# 5. 为类属性赋值都能覆盖描述符. 除非元类上有描述符.
# 6. 方法/函数是非覆盖型描述符
#   - 方法都有__get__.
#   - Text.reverse.__get__(word)
#   - word.reverse: 绑定方法对象, 包含__call__, __func__属性.
# 7. 建议
#   - 优先使用 property
#   - 只读描述符(非覆盖描述符)必须有__set__, 否则实例的同名属性会遮盖描述符.
#   - 用于验证的描述符可以只有__set__.
#   - 仅有__get__方法的描述符可以实现高效缓存:
#   为实例设置同名属性，缓存结果。同名实例属性会遮盖描述符，因此后续访问会直接从实例的__dict__属性中获取值，而不会再触发描述符的__get__方法。
#   - 非特殊的方法可以被实例属性遮盖.


class Quantity:
    """
    描述符类
    """
    def __init__(self, storage_name):
        self.storage_name = storage_name

    def __set__(self, instance, value):
        """
        不能使用setattr(), 否则会再次触发__set__, 导致无限递归. 因为托管属性和存储属性同名.
        """
        if value > 0:
            instance.__dict__[self.storage_name] = value  # 使用托管实例的存储属性
        else:
            raise ValueError('value mast be > 0')


class LineItem:
    """
    委托类
    """
    weight = Quantity('weight')  # 托管属性
    price = Quantity('price')