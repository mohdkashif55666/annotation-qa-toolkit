import pytest
from annotation_qa import cohens_kappa, fleiss_kappa, percent_agreement, majority_vote


def test_perfect_agreement():
    a = ["pos", "neg", "neu", "pos"]
    assert percent_agreement(a, a) == 1.0
    assert cohens_kappa(a, a) == pytest.approx(1.0)


def test_cohens_kappa_known_value():
    a = ["y"] * 20 + ["y"] * 5 + ["n"] * 10 + ["n"] * 15
    b = ["y"] * 20 + ["n"] * 5 + ["y"] * 10 + ["n"] * 15
    assert cohens_kappa(a, b) == pytest.approx(0.4, abs=0.01)


def test_fleiss_all_agree():
    assert fleiss_kappa([["a", "a", "a"], ["b", "b", "b"], ["a", "a", "a"]]) == pytest.approx(1.0)


def test_majority_vote_tie():
    assert majority_vote(["a", "b"])["tie"] is True
    assert majority_vote(["a", "a", "b"])["label"] == "a"
