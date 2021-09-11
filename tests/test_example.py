from hexlet_pytest.example import reverse

def test_revers():
	assert reverse('hexlet') == 'telxeh'

def test_reverse_for_empty_string():
    assert reverse('') == ''