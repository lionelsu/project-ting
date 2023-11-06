from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()

    high_priority_1 = {'qtd_linhas': 4}
    high_priority_2 = {'qtd_linhas': 3}
    no_priority_1 = {'qtd_linhas': 5}
    no_priority_2 = {'qtd_linhas': 6}

    priority_queue.enqueue(high_priority_1)
    priority_queue.enqueue(high_priority_2)
    priority_queue.enqueue(no_priority_1)
    priority_queue.enqueue(no_priority_2)

    assert len(priority_queue) == 4

    assert priority_queue.is_priority(high_priority_1) is True
    assert priority_queue.is_priority(high_priority_2) is True
    assert priority_queue.is_priority(no_priority_1) is False
    assert priority_queue.is_priority(no_priority_2) is False

    # A ordem deve ser:
    # high_priority_1, high_priority_2, no_priority_1, no_priority_2
    assert priority_queue.search(0) == high_priority_1
    assert priority_queue.search(1) == high_priority_2
    assert priority_queue.search(2) == no_priority_1
    assert priority_queue.search(3) == no_priority_2

    priority_queue.dequeue()  # Remove high_priority_1
    assert len(priority_queue) == 3
    # Agora high_priority_2, no_priority_1, no_priority_2 devem permanecer
    assert priority_queue.search(0) == high_priority_2
    assert priority_queue.search(1) == no_priority_1
    assert priority_queue.search(2) == no_priority_2

    priority_queue.dequeue()  # Remove high_priority_2
    assert len(priority_queue) == 2
    # Agora no_priority_1, no_priority_2 devem permanecer
    assert priority_queue.search(0) == no_priority_1
    assert priority_queue.search(1) == no_priority_2

    priority_queue.dequeue()  # Remove no_priority_1
    assert len(priority_queue) == 1
    # Agora apenas no_priority_2 deve permanecer
    assert priority_queue.search(0) == no_priority_2

    priority_queue.dequeue()  # Remove no_priority_2
    assert len(priority_queue) == 0

    with pytest.raises(IndexError):
        priority_queue.search(0)
