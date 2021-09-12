from hexlet_pytest.example import reverse
from hexlet_pytest.stack import Stack
import pytest


def test_revers():
	assert reverse('hexlet') == 'telxeh'

def test_reverse_for_empty_string():
    assert reverse('') == ''


# пример модульного тестирования  
# 1 Тестируем основную функциональность (пример стек)

def test_stack():
    stack = Stack()
    stack.push('one')
    stack.push('two')

    assert stack.pop() == 'two'
    assert stack.pop() == 'one'

# 2 Тестируем дополнительную функциональность

def test_emptiness():
    stack = Stack()
    assert not stack
    stack.push('one')
    assert bool(stack)  # not not stack

    stack.pop()
    assert not stack

# Пограничные случаи  (попытка взять элемент из пустого стека)

def test_pop_with_empty_stack():
    stack = Stack()
    with pytest.raises(IndexError):
        stack.pop()