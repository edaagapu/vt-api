from openpyxl import load_workbook, Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from tkinter import filedialog as FileDialog
from openpyxl.formatting.rule import ColorScaleRule

def open_workbook():
  route = FileDialog.askopenfilename(title='Abrir hoja de calculo',filetypes=(('Documento de Excel (2007-posterior)', '*.xlsx'), ('Documento de Excel 2003', '*.xls')))
  return load_workbook(route)


def modificate_fields(wb: Workbook, fields: list|tuple, sheetname=None, rules: list|tuple = []):
  if sheetname:
    ws = wb[sheetname] if sheetname in wb.sheetnames else wb.create_sheet(sheetname)
  else:
    ws = wb.active
  
  for row in fields:
    ws.append(row)


def save_workbook(wb: Workbook, route=None):
  if not route:
    route = FileDialog.asksaveasfilename(title='Guardar fichero', defaultextension='.xlsx')
  wb.save(route)


def result_format_center(cell):
  cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
  if 'Error' in str(cell.value):
    cell.font = Font(color='626262')
    cell.fill = PatternFill(fill_type='solid', start_color="CBCBCB", end_color="CBCBCB")


def format_workbook(ws, rg=None, **rules):
  list(map(result_format_center, list(ws['B'])))
  ws.conditional_formatting.add(rg, ColorScaleRule(**rules))

if __name__ == '__main__':
  wb = open_workbook()
  rules = {
    'start_type': 'percentile',
    'start_value': 0,
    'start_color': 'A2FFA2',
    'mid_type': 'percentile',
    'mid_value': 80,
    'mid_color': 'FFA2A2',
    'end_type': 'percentile',
    'end_value': 100,
    'end_color': 'FFA2A2'
  }
  ws = wb.active
  rg = f'B2:B{ws.max_row}'
  
  format_workbook(ws, rg=rg, **rules)
  save_workbook(wb)
