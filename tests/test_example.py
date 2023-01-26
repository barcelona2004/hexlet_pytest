from hexlet_pytest.example import reverse

def test_reverse():
    assert reverse('hexlet') == 'telxeh'


def test_reverse_with_caps():
    assert reverse('God') == 'doG'
