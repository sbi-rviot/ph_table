import pandas as pd
import io

# Reformat table_color as dict of tuples

dict_colors = {
    'yellow_light' : ('#BF8F00', '2px solid #BF8F00', '#FFF2CC', '#FFFFFF'),
    'grey_light' : ('#808080', '2px solid #808080', '#EDEDED', '#FFFFFF'),
    'blue_light' : ('#305496', '2px solid #305496', '#D9E1F2', '#FFFFFF'),
    'orange_light' : ('#C65911', '2px solid #C65911', '#FCE4D6', '#FFFFFF'),
    'green_light' : ('#548235', '2px solid #548235', '#E2EFDA', '#FFFFFF'), 
    'red_light' : ('#823535', '2px solid #823535', '#efdada', '#FFFFFF'),
    'yellow_dark' : ('#FFFFFF', '2px solid #BF8F00', '#FFF2CC', '#BF8F00'),
    'grey_dark' : ('#FFFFFF', '2px solid #808080', '#EDEDED', '#808080'),
    'blue_dark': ('#FFFFFF', '2px solid #305496', '#D9E1F2', '#305496'),
    'orange_dark' : ('#FFFFFF', '2px solid #C65911', '#FCE4D6', '#C65911'),
    'green_dark' : ('#FFFFFF', '2px solid #548235', '#E2EFDA', '#548235'),
    'red_dark' : ('#FFFFFF', '2px solid #823535', '#efdada', '#823535')
}


def build_table(
        df, 
        color, 
        font_size='medium', 
        font_family='Century Gothic, sans-serif', 
        text_align='left', 
        width='auto', 
        index=False, 
        even_color='black', 
        even_bg_color='white', 
        escape=True,
        width_dict=[],
        conditions={}):

    if df.empty:
      return ''
     
    # Set color
    padding="0px 20px 0px 0px"
    color, border_bottom, odd_background_color, header_background_color = dict_colors[color]

    a = 0
    while a != len(df):
        if a == 0:        
            df_html_output = df.iloc[[a]].to_html(na_rep = "", index = index, border = 0, escape=escape)
            # change format of header
            if index:
                df_html_output = df_html_output.replace('<th>'
                                                        ,'<th style = "background-color: ' + header_background_color
                                                        + ';font-family: ' + font_family
                                                        + ';font-size: ' + str(font_size)
                                                        + ';color: ' + color
                                                        + ';text-align: ' + text_align
                                                        + ';border-bottom: ' + border_bottom
                                                        + ';padding: ' + padding
                                                        + ';width: ' + str(width) + '">', len(df.columns)+1)

                df_html_output = df_html_output.replace('<th>'
                                                        ,'<th style = "background-color: ' + odd_background_color
                                                        + ';font-family: ' + font_family
                                                        + ';font-size: ' + str(font_size)
                                                        + ';text-align: ' + text_align
                                                        + ';padding: ' + padding
                                                        + ';width: ' + str(width) + '">')

            else:
                df_html_output = df_html_output.replace('<th>'
                                                        ,'<th style = "background-color: ' + header_background_color
                                                        + ';font-family: ' + font_family
                                                        + ';font-size: ' + str(font_size)
                                                        + ';color: ' + color
                                                        + ';text-align: ' + text_align
                                                        + ';border-bottom: ' + border_bottom
                                                        + ';padding: ' + padding
                                                        + ';width: ' + str(width) + '">')

            #change format of table
            df_html_output = df_html_output.replace('<td>'
                                                    ,'<td style = "background-color: ' + odd_background_color
                                                    + ';font-family: ' + font_family
                                                    + ';font-size: ' + str(font_size)
                                                    + ';text-align: ' + text_align
                                                    + ';padding: ' + padding
                                                    + ';width: ' + str(width) + '">')
            body = """<p>""" + format(df_html_output)

            a = 1

        elif a % 2 == 0:
            df_html_output = df.iloc[[a]].to_html(na_rep = "", index = index, header = False, escape=escape)
             
            # change format of index
            df_html_output = df_html_output.replace('<th>'
                                                    ,'<th style = "background-color: ' + odd_background_color
                                                    + ';font-family: ' + font_family
                                                    + ';font-size: ' + str(font_size)
                                                    + ';text-align: ' + text_align
                                                    + ';padding: ' + padding
                                                    + ';width: ' + str(width) + '">')

            #change format of table
            df_html_output = df_html_output.replace('<td>'
                                                    ,'<td style = "background-color: ' + odd_background_color
                                                    + ';font-family: ' + font_family
                                                    + ';font-size: ' + str(font_size)
                                                    + ';text-align: ' + text_align
                                                    + ';padding: ' + padding
                                                    + ';width: ' + str(width) + '">')

            body = body + format(df_html_output)

            a += 1       

        elif a % 2 != 0:
            df_html_output = df.iloc[[a]].to_html(na_rep = "", index = index, header = False, escape=escape)
             
            # change format of index
            df_html_output = df_html_output.replace('<th>'
                                                    ,'<th style = "background-color: ' + even_bg_color
                                                    + '; color: ' + even_color
                                                    + ';font-family: ' + font_family
                                                    + ';font-size: ' + str(font_size)
                                                    + ';text-align: ' + text_align
                                                    + ';padding: ' + padding
                                                    + ';width: ' + str(width) + '">')
             
            #change format of table
            df_html_output = df_html_output.replace('<td>'
                                                    ,'<td style = "background-color: ' + even_bg_color
                                                    + '; color: ' + even_color
                                                    + ';font-family: ' + font_family
                                                    + ';font-size: ' + str(font_size)
                                                    + ';text-align: ' + text_align
                                                    + ';padding: ' + padding
                                                    + ';width: ' + str(width) + '">')
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

    if conditions:
        for k in conditions.keys():
            try:
                conditions[k]['index'] = list(df.columns).index(k)
                width_body = ''
                w = 0
                for line in io.StringIO(body):
                    updated_body = False
                    if  w == conditions[k]['index']:
                        try:
                            if int(repr(line).split('>')[1].split('<')[0]) < conditions[k]['min']:
                                if 'color: black' in repr(line):
                                    width_body = width_body + repr(line).replace("color: black", 'color: ' + conditions[k]['min_color'])[1:]
                                elif 'color: white' in repr(line):
                                    width_body = width_body + repr(line).replace("color: white", 'color: ' + conditions[k]['min_color'])[1:]
                                else:
                                    width_body = width_body + repr(line).replace('">', '; color: ' + conditions[k]['min_color'] + '">')[1:]
                                updated_body = True
                            elif int(repr(line).split('>')[1].split('<')[0]) > conditions[k]['max']:
                                if 'color: black' in repr(line):
                                    width_body = width_body + repr(line).replace("color: black", 'color: ' + conditions[k]['max_color'])[1:]
                                elif 'color: white' in repr(line):
                                    width_body = width_body + repr(line).replace("color: white", 'color: ' + conditions[k]['max_color'])[1:]
                                else:
                                    width_body = width_body + repr(line).replace('">', '; color: ' + conditions[k]['max_color'] + '">')[1:]
                                updated_body = True
                        except:
                            pass
                    if not updated_body:
                        width_body = width_body + repr(line)[1:]

                    if str(repr(line))[:10] == "'      <td" or str(repr(line))[:10] == "'      <th":
                        if w == len(df.columns) -1:
                            w = 0
                        else:
                            w += 1
                body = width_body[:len(width_body)-1]
            except:
                pass




    if len(width_dict) == len(df.columns):
        width_body = ''
        w = 0
        if conditions:
            for line in body.split(r"\n'"):
                width_body = width_body + repr(line).replace("width: auto", 'width: ' + width_dict[w])[1:]
                if str(repr(line))[:10] == "'      <td" or str(repr(line))[:10] == "'      <th" :
                    if w == len(df.columns) -1:
                        w = 0
                    else:
                        w += 1
        else:
            for line in io.StringIO(body):
                width_body = width_body + repr(line).replace("width: auto", 'width: ' + width_dict[w])[1:]
                if str(repr(line))[:10] == "'      <td" or str(repr(line))[:10] == "'      <th" :
                    if w == len(df.columns) -1:
                        w = 0
                    else:
                        w += 1
        return width_body[:len(width_body)-1].replace("'", "")
    else:
        return body.replace(r"\n'", "")