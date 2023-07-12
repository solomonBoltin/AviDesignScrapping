

def build_table(product_description):
    table_rows = ""
    for name, value in product_description:
        table_rows += f"<tr><th>{name}</th><td>{value}</td></tr>"
    html_code = f"""
        <style>
            table {{
              font-family: arial, sans-serif;
              border-collapse: collapse;
              width: 100%;
            }}
            
            td, th {{
              border: 1px solid #dddddd;
              text-align: left;
              padding: 8px;
            }}
        </style>
        <table>
            {table_rows}
        </table>
        """
    return html_code
