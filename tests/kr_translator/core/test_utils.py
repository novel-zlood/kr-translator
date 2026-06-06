from kr_translator.core.utils import has_repeating_chars, STEP, MIN_CHARS


def test_normal_text_no_repeating():
    assert not has_repeating_chars("This is a normal paragraph of text.")


def test_empty_string():
    assert not has_repeating_chars("")


def test_short_repeating_chars_below_step():
    assert not has_repeating_chars("a" * (STEP - 1))


def test_repeating_single_char_at_step():
    assert has_repeating_chars("a" * STEP)


def test_repeating_few_chars_at_step():
    pattern = "ab" * (STEP // 2)
    assert has_repeating_chars(pattern)


def test_diverse_chars_at_step():
    text = "".join(chr(i) for i in range(32, 32 + MIN_CHARS)) * (STEP // MIN_CHARS + 1)
    assert not has_repeating_chars(text[:STEP])


def test_repeating_in_later_window():
    normal = "".join(chr(i) for i in range(32, 127)) * 10
    repeating = "x" * STEP
    assert has_repeating_chars(normal[:STEP] + repeating)
