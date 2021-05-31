import unittest

from catdog import Cat, Dog, CatDog


def test_cat():
    cat = Cat()
    cat.meow()
    assert 'Cat say "meow"'

    cat.eat()
    assert 'Cat eats fish'


def test_dog():
    dog = Dog()
    dog.bark()
    assert 'Dog say "woof"'

    dog.eat()
    assert 'Dog eat meat'


def test_catdog():
    catdog = CatDog()
    catdog.eat()
    assert 'CatDog eats meat and fish'
