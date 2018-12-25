import demo_class as dc
import pytest

### test character class
# def testNameFuncCharacterOject():
#     testCases = [
#         {
#             'description': 'test function get name return true name after init',
#             'obj': dc.Character('name'),
#             'expect': {'name', 'name'} 
#         }
    
#     ]

class TestClassCharacter:
    #test attr
    def testAttr(self):
        # test has attr in class Character
        assert hasattr(dc.Character, 'age')
        assert hasattr(dc.Character, 'name')
    
    #test class method init and method get
    @pytest.mark.parametrize("test_input,expected", [
        ('anh', 'anh'),
        ('riot', 'riot'),

    ])
    def testInstanceWithInit(self, test_input, expected):
        instance = dc.Character(name=test_input)
        assert instance.name == expected

    # test class method set
    @pytest.mark.parametrize("test_input,expected", [
        ('anh', 'anh'),
        ('riot', 'admin'),
    ])
    def testInstanceWithSet(self, test_input, expected):
        instance = dc.Character(name="default")
        instance.name = test_input
        assert instance.name == expected


class TestClassSkill:
    #test attr
    def testAttr(self):
        # test has attr in class skill
        assert hasattr(dc.Skill, 'skname')
        assert hasattr(dc.Skill, 'action')
    
    #test instance
    # def testInstanceCharacter(self):

    #test class method init and method get
    @pytest.mark.parametrize("test_input,expected", [
        ('hasagi', 'Skill hasagi'),
        ('leftgame', 'Skill leftgame'),

    ])
    def testInstanceWithInit(self, test_input, expected):
        instance = dc.Skill(skname=test_input)
        assert instance.skname == expected

    # test class method set
    @pytest.mark.parametrize("test_input,expected", [
        ('hasagi', 'Skill hasagi'),
        ('leftgame', 'Skill leftgame'),
    ])
    def testInstanceWithSet(self, test_input, expected):
        instance = dc.Skill(skname="default")
        instance.skname = test_input
        assert instance.skname == expected

class TestClassYasuo:
    #test attr
    def testAttr(self):
        # test has attr in class Yasuo
        assert hasattr(dc.Yasuo, 'name')
        assert hasattr(dc.Yasuo, 'action')
        assert hasattr(dc.Yasuo, 'skname')

    # test class method set
    @pytest.mark.parametrize("test_input,expected", [
        ('hasagi', ['hasagi', 'Skill hasagi']),
        ('leftgame', ['leftgame', 'Skill leftgame']),
    ])
    def testInstanceWithSet(self, test_input, expected):
        instance = dc.Yasuo(name="default")
        instance.name = test_input
        instance.skname = test_input
        assert instance.name == expected[0]
        assert instance.skname == expected[1]
