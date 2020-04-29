'''
如果想访问属性可以通过属性的getter（访问器）和setter（修改器）方法
进行对应的操作。如果要做到这点，就可以考虑使用@property包装器来包装
getter和setter方法，使得对属性的访问既安全又方便，代码如下所示。
'''
class Person(object):

    def __init__(self, name, age):
        self._name = name # 私有变量的该声明赋值
        self._age = age

    # 访问器 - getter方法
    @property             #获取私有变量的值
    def name(self):
        return self._name

    # 访问器 - getter方法
    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def main():
    person = Person('王大锤', 12)
    person.play()
    person.age = 22
    person.play()
    # person.name = '白元芳'  # AttributeError: can't set attribute


if __name__ == '__main__':
    main()