from openpyxl import load_workbook, Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.formatting.rule import ColorScaleRule
from base import Facade

class ExcelFacade(Facade):
  def __init__(self):
    super().__init__()
    

  def open(self):
    super().open('Abrir hoja de calculo', (('Documento de Excel (2007-posterior)', '*.xlsx'), ('Documento de Excel 2003', '*.xls')))
    self.src_file = load_workbook(self.path)


  def save(self, same_route, initialdir, **kwargs):
    super().save(same_route, 'Guardar fichero', '.xlsx', initialdir=initialdir)
    self.src_file.save(self.path)


  def custom_process(self, headers, data, **kwargs):
    def __format_cell__(cell):
      cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
      if 'Error' in str(cell.value):
        cell.font = Font(color='626262')
        cell.fill = PatternFill(fill_type='solid', start_color="CBCBCB", end_color="CBCBCB")
      elif 'Warning' in str(cell.value):
        cell.font = Font(color='AC9A00')
        cell.fill = PatternFill(fill_type='solid', start_color="FFF17C", end_color="FFF17C")
    
    sheetname = kwargs.get('sheetname', 'Hoja')
    ws = self.src_file[sheetname] if sheetname in self.src_file.sheetnames else self.src_file.create_sheet(sheetname)

    ws.append(headers)

    for row in data:
      ws.append(row)

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

    rg = f'B2:B{ws.max_row}'
    ws.conditional_formatting.add(rg, ColorScaleRule(**rules))

    
    for cell in list(ws['B']):
      __format_cell__(cell)
    
    return None
    

  
