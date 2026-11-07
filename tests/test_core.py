import pytest

pd = pytest.importorskip("pandas")

from tableloom import build_table


def test_build_table_empty_returns_empty_string():
    df = pd.DataFrame()
    assert build_table(df, color="blue_light") == ""


def test_build_table_basic_html_contains_values_and_styles():
    df = pd.DataFrame({"A": [1, 2], "B": ["x", "y"]})
    html = build_table(
        df,
        color="yellow_light",
        index=False,
        width="auto",
        width_dict=["50px", "60px"],
    )
    assert "A" in html
    assert "B" in html
    # header background color for "yellow_light" is "#FFF2CC"
    assert "background-color: #FFF2CC" in html
    # width from width_dict should be applied to first column
    assert "width: 50px" in html
