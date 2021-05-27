from __future__ import annotations

from typing import Any


class UnitIsDead(Exception):
    pass


class Unit:
    def __init__(self, name: str = 'default unit', hp: float = 100, damage: float = 10) -> None:
        self._name = self._check_name(name)
        self._current_HP = self._validate(hp)
        self._max_HP = self._validate(hp)
        self._damage = self._validate(damage)

    def _validate(self, value: Any) -> float:
        return float(value)

    def _check_name(self, name: Any) -> str:
        if not isinstance(name, str):
            raise TypeError(
                f'name should be of type str, got {name.__class__.__name__} instead'
            )
        return name

    def _check_type(self, enemy: Any) -> None:
        if not isinstance(enemy, self.__class__):
            raise TypeError(
                f'Should be of type {self.__class__.__name__}, got {enemy.__class__.__name__} instead'
            )

    def ensure_is_alive(self) -> None:
        raise UnitIsDead('Unit is already dead')

    @property
    def name(self) -> str:
        return self._name

    @property
    def current_HP(self) -> float:
        return self._current_HP

    @property
    def max_HP(self) -> float:
        return self._max_HP

    @property
    def damage(self) -> float:
        return self._damage

    @name.setter
    def name(self, name: Any) -> None:
        self._check_name(name)
        self.name = name

    @current_HP.setter
    def current_HP(self, hp: Any) -> None:
        self._validate(hp)
        self.current_HP = hp
        self._limit()

    @max_HP.setter
    def max_HP(self, hp: Any) -> None:
        self._validate(hp)
        self.max_HP = hp

    @damage.setter
    def damage(self, damage: Any) -> None:
        self._validate(damage)
        self.damage = damage

    def _limit(self) -> None:
        if self.current_HP < 0:
            self.current_HP = 0
            return
        if self.current_HP > self.max_HP:
            self.current_HP = self.max_HP

    def add_hp(self, hp: Any) -> None:
        self._validate(hp)
        self.current_HP += hp
        self._limit()

    def take_damage(self, damage: Any) -> None:
        self._validate(damage)
        self.current_HP -= damage
        self._limit()

    def attack(self, enemy: Any) -> None:
        self._check_type(enemy)
        enemy.ensure_is_alive()
        enemy.take_damage(self.damage)

    def counter_attack(self, enemy: Any) -> None:
        self._check_type(enemy)
        enemy.take_damage(self.damage / 2)

    def __str__(self) -> str:
        return f'Name: {self.name}/n' \
               f'HP: {self.current_HP} / {self.max_HP}/n' \
               f'Damage: {self.damage}'
