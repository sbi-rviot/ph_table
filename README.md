pretty_html_table - Beautiful html tables made easy
Detailed usage documentation is still in progress
The objective of this package is to convert a pandas dataframe into a pretty html table.
As of now, 10 colors are available. This package is embedding very nicely with other packages used to send emails.
The format is set down to the line item, which allows it to be understood by every email providers (instead of using CSS style).

This is for example how you can convert your dataframe:

import pretty_html_table
html_table_blue_light = build_table(pd.read_excel('df.xlsx'), 'blue_light')
print(html_table_blue_light)


Why choose pretty_html_table?
It integrates very well with other python packages used to send emails. Just add the result of this package to the body of the email and voila.


List of colors available

| Name         | font style     | Header                                                  | Rows                                                          |
|--------------|----------------|---------------------------------------------------------|---------------------------------------------------------------|
| 'blue_light' | Century Gothic | Bold: yes Background color: white Font color: dark blue | Odd background color: light blue Even background color: white |
|              |                |                                                         |                                                               |
|              |                |                                                         |                                                               |

Name
'blue_light'
'grey_light'
'orange_light'
'yellow_light'
'green_light'
'blue_dark'
'grey_dark'
'orange_dark'
'yellow_dark'
'green_dark'


This project was also a learning resource for us. This is a list of not so common python idioms used in this project:
New unpacking technics: def method(argument, *, with_name=None, **other_params):
Enums: from enum import Enum
Factory paradigm
Package organization
Timezone conversion and timezone aware datetimes
Etc. (see the code!)
What follows is kind of a wiki...