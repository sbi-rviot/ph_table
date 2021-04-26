import pandas as pd
from pretty_html_table import build_table

"""
Code which generates example tables html for documentation.
"""

def generate_table():
    df = pd.DataFrame(data={
        'ID' : [1,2,3,4],
        'First Name' : ['Flore', 'Grom', 'Truip', 'Ftro'],
        'Last Name' : ['Ju', 'Re', 'Ve', 'Cy'],
        'Age' : [23, 45, 67, 12],
        'Place of Birth' : ['France', 'USA', 'China', 'India'],
        'Date of Birth' : ['1996-10-04', '1974-10-10', '1952-04-07', '2007-10-06']
    })

    start = """<html><body>"""
    end = """ </body></html>"""

    output = start \
            + '<p style="font-family:Century Gothic;">blue_light<br /><p>' \
            + build_table(df, 'blue_light') \
            + '<p style="font-family:Century Gothic;">blue_dark<br /><p>' \
            + build_table(df, 'blue_dark') \
            + '<p style="font-family:Century Gothic;">grey_light<br /><p>' \
            + build_table(df, 'grey_light') \
            + '<p style="font-family:Century Gothic;">grey_dark<br /><p>' \
            + build_table(df, 'grey_dark') \
            + '<p style="font-family:Century Gothic;">orange_light<br /><p>' \
            + build_table(df, 'orange_light') \
            + '<p style="font-family:Century Gothic;">orange_dark<br /><p>' \
            + build_table(df, 'orange_dark') \
            + '<p style="font-family:Century Gothic;">yellow_light<br /><p>' \
            + build_table(df, 'yellow_light') \
            + '<p style="font-family:Century Gothic;">yellow_dark<br /><p>' \
            + build_table(df, 'yellow_dark') \
            + '<p style="font-family:Century Gothic;">green_light<br /><p>' \
            + build_table(df, 'green_light') \
            + '<p style="font-family:Century Gothic;">green_dark<br /><p>' \
            + build_table(df, 'green_dark') \
            + '<p style="font-family:Century Gothic;">red_light<br /><p>' \
            + build_table(df, 'red_light') \
            + '<p style="font-family:Century Gothic;">red_dark<br /><p>' \
            + build_table(df, 'red_dark') \
            + end

    with open('example.html', 'w') as f:
        f.write(output)

if __name__ == "__main__":
    generate_table()