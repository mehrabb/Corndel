import pytest

def test_upper():
    assert 'foo'.upper() == 'FOO'
    
def test_isupper():
    assert 'FOO'.isupper()
    assert not 'Foo'.isupper()
    
def test_split():
    s = 'hello world'
    assert s.split() == ['hello','world']
    #check that s.split fails when the separator is not a string
    with pytest.raises(TypeError):
        s.split(2)

def test_starts_vowel_normal():
    assert starts_vowel("apple") is True
    assert starts_vowel("Banana") is False
    assert starts_vowel("Orange") is True
    assert starts_vowel("grape") is False
        
def starts_vowel(s: str) -> bool:
    """
    Check if the string s starts with a vowel.
    Return True if it does, False otherwise.
    """
    if not s:  # handle empty string
        return False
    return s[0].lower() in "aeiou"


