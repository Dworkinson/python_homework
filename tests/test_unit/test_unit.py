import pytest

from unit.unit import Unit
from unit.unit import UnitIsDead

DEFAULT_NAME = 'default unit'
DEFAULT_HP = 100
DEFAULT_DAMAGE = 10

NEW_NAME = 'Unit'
NEW_HP = 150
NEW_DAMAGE = 15

FLASH_WOUND = 90
HEAVY_WOUND = 10


@pytest.mark.parametrize('params', [
    (), (NEW_NAME, NEW_HP, NEW_DAMAGE)
])
def test_constructor(params):
    unit = Unit(*params)

    assert unit.name == params[0] if params != () else DEFAULT_NAME
    assert unit.current_HP == params[1] if params != () else DEFAULT_HP
    assert unit.max_HP == params[1] if params != () else DEFAULT_HP
    assert unit.damage == params[2] if params != () else DEFAULT_DAMAGE


@pytest.mark.parametrize('name, hp, damage, exception_type', [
    (DEFAULT_NAME, 'text', 'text', ValueError), (12, DEFAULT_HP, DEFAULT_DAMAGE, TypeError),
    (Unit, Unit, Unit, TypeError)
])
def test_constructor_exception(name, hp, damage, exception_type):
    with pytest.raises(exception_type):
        Unit(name, hp, damage)


def test_setters():
    unit = Unit()

    assert unit.name == DEFAULT_NAME
    assert unit.current_HP == DEFAULT_HP
    assert unit.max_HP == DEFAULT_HP
    assert unit.damage == DEFAULT_DAMAGE

    unit.name = NEW_NAME
    unit.max_HP = NEW_HP
    unit.current_HP = NEW_HP
    unit.damage = NEW_DAMAGE

    assert unit.name == NEW_NAME
    assert unit.current_HP == NEW_HP
    assert unit.max_HP == NEW_HP
    assert unit.damage == NEW_DAMAGE


def test_add_hp():
    unit = Unit()

    unit.current_HP = FLASH_WOUND
    unit.add_hp(20)

    assert unit.current_HP == DEFAULT_HP


def test_take_damage():
    unit = Unit()

    unit.current_HP = HEAVY_WOUND
    unit.take_damage(20)

    assert unit.current_HP == 0


def test_attacking_counter_attacking():
    attacker = Unit()
    enemy = Unit()

    attacker.attack(enemy)

    assert enemy.current_HP == 90
    assert attacker.current_HP == 95


def test_unit_is_dead_exception():
    unit = Unit()

    unit.current_HP = 0

    with pytest.raises(UnitIsDead):
        unit.add_hp(20)


def test_attack_exception():
    unit = Unit()

    with pytest.raises(TypeError):
        unit.attack('Unit')


def test_counter_attack_exception():
    unit = Unit()

    with pytest.raises(TypeError):
        unit.counter_attack('Unit')


@pytest.mark.parametrize('params, string_repr', [
    ((), ('Name: default unit\n'
          'HP: 100.0/100.0\n'
          'Damage: 10.0')),
    ((NEW_NAME, NEW_HP, NEW_DAMAGE),
     ('Name: Unit\n'
      'HP: 150.0/150.0\n'
      'Damage: 15.0'))
])
def test_string_repr(params, string_repr):
    unit = Unit(*params)

    assert str(unit) == string_repr
