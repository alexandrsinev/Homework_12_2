import pytest

from utils import arrs, dicts

LIST_1 = [1, 2, 3]
LIST_2 = [1, 2, 3, 4]

@pytest.fixture
def list_fixture1():
    return LIST_1

@pytest.fixture
def list_fixture2():
    return LIST_2


def test_get(list_fixture1):
    assert arrs.get(list_fixture1, 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice(list_fixture1, list_fixture2):
    assert arrs.my_slice(list_fixture2, 1, 3) == [2, 3]
    assert arrs.my_slice(list_fixture1, 1) == [2, 3]
    assert arrs.my_slice([]) == []
    assert arrs.my_slice(list_fixture1) == [1, 2, 3]


def test_get_val():
    assert dicts.get_val({"vcs": "mercurial"}, "vcs") == "mercurial"
    assert dicts.get_val({"vcs": "mercurial"}, "vcs", "git") == "mercurial"
    assert dicts.get_val({}, "vcs", "git") == "git"
    assert dicts.get_val({}, "vcs", "bazaar") == "bazaar"

