def table_color(color_choice):
    if color_choice == 'yellow_light':
        color = '#BF8F00'
        border_bottom = '2px solid #BF8F00'
        odd_background_color = '#FFF2CC'
        header_background_color = '#FFFFFF'

    if color_choice == 'grey_light':
        color = '#808080'
        border_bottom = '2px solid #808080'
        odd_background_color = '#EDEDED'
        header_background_color = '#FFFFFF'

    if color_choice == 'blue_light':
        color = '#305496'
        border_bottom = '2px solid #305496'
        odd_background_color = '#D9E1F2'
        header_background_color = '#FFFFFF'

    if color_choice == 'orange_light':
        color = '#C65911'
        border_bottom = '2px solid #C65911'
        odd_background_color = '#FCE4D6'
        header_background_color = '#FFFFFF'

    if color_choice == 'green_light':
        color = '#548235'
        border_bottom = '2px solid #548235'
        odd_background_color = '#E2EFDA'
        header_background_color = '#FFFFFF'

    if color_choice == 'red_light':
        color = '#823535'
        border_bottom = '2px solid #823535'
        odd_background_color = '#efdada'
        header_background_color = '#FFFFFF'

    if color_choice == 'yellow_dark':
        color = '#FFFFFF'
        border_bottom = '2px solid #BF8F00'
        odd_background_color = '#FFF2CC'
        header_background_color = '#BF8F00'

    if color_choice == 'grey_dark':
        color = '#FFFFFF'
        border_bottom = '2px solid #808080'
        odd_background_color = '#EDEDED'
        header_background_color = '#808080'

    if color_choice == 'blue_dark':
        color = '#FFFFFF'
        border_bottom = '2px solid #305496'
        odd_background_color = '#D9E1F2'
        header_background_color = '#305496'

    if color_choice == 'orange_dark':
        color = '#FFFFFF'
        border_bottom = '2px solid #C65911'
        odd_background_color = '#FCE4D6'
        header_background_color = '#C65911'

    if color_choice == 'green_dark':
        color = '#FFFFFF'
        border_bottom = '2px solid #548235'
        odd_background_color = '#E2EFDA'
        header_background_color = '#548235'

    if color_choice == 'red_dark':
        color = '#FFFFFF'
        border_bottom = '2px solid #823535'
        odd_background_color = '#efdada'
        header_background_color = '#823535'
        
    return color, border_bottom, odd_background_color, header_background_color

def build_table(df, color, font_family = 'Century Gothic', text_align = 'left', padding="0px 20px 0px 0px", even_background_color = '#FFFFFF'):

    color, border_bottom, odd_background_color, header_background_color = table_color(color)

    #build html table
    a = 0
    while a != len(df):
        if a == 0:        
            df_html_output = df.iloc[[a]].to_html(na_rep = "", index = False, border = 0)
            # change format of header
            df_html_output = df_html_output.replace('<th>'
                                                    ,'<th style = "background-color: ' + header_background_color
                                                    + ';font-family: ' + font_family
                                                    + ';color: ' + color
                                                    + ';text-align: ' + text_align
                                                    + ';border-bottom: ' + border_bottom
                                                    + ';padding: ' + padding + '">')

            #change format of table
            df_html_output = df_html_output.replace('<td>'
                                                    ,'<td style = "background-color: ' + odd_background_color
                                                    + ';font-family: ' + font_family
                                                    + ';text-align: ' + text_align
                                                    + ';padding: ' + padding + '">')

            body = """<p>""" + format(df_html_output)

            a = 1

        elif a % 2 == 0:
            df_html_output = df.iloc[[a]].to_html(na_rep = "", index = False, header = False)
             
            #change format of table
            df_html_output = df_html_output.replace('<td>'
                                                    ,'<td style = "background-color: ' + odd_background_color
                                                    + ';font-family: ' + font_family
                                                    + ';text-align: ' + text_align
                                                    + ';padding: ' + padding + '">')

            body = body + format(df_html_output)

            a += 1       

        elif a % 2 != 0:
            df_html_output = df.iloc[[a]].to_html(na_rep = "", index = False, header = False)
             
            #change format of table
            df_html_output = df_html_output.replace('<td>'
                                                    ,'<td style = "background-color: ' + even_background_color
                                                    + ';font-family: ' + font_family
                                                    + ';text-align: ' + text_align
                                                    + ';padding: ' + padding + '">')

            body = body + format(df_html_output)

            a += 1

    body = body + """</p>"""

    body = body.replace("""</td>
    </tr>
  </tbody>
</table>
            <table border="1" class="dataframe">
  <tbody>
    <tr>""","""</td>
    </tr>
    <tr>""").replace("""</td>
    </tr>
  </tbody>
</table><table border="1" class="dataframe">
  <tbody>
    <tr>""","""</td>
    </tr>
    <tr>""")
    
    return body
