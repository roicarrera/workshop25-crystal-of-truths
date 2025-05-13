from hypothesis import given, strategies as st
from PBT.invariants import reverse, sort, deduplicate

@given(st.lists(st.integers()))
def test_reverse_preserves_length(xs):
    assert len(reverse(xs)) == len(xs)

@given(st.lists(st.integers()))
def test_sort_preserves_multiset(xs):
    assert set(sort(xs)) == set(xs)

@given(st.lists(st.integers()))
def test_deduplicate_output_is_unique(xs):
    output = deduplicate(xs)
    assert len(set(output)) == len(output)