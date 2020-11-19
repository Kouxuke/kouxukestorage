import xlrd

class Getdata():
    def __init__(self,filename):

        self.data=xlrd.open_workbook(filename)
        self.table = self.data.sheet_by_index(0)
        self.keys=self.table.row_values(0)
        self.rownum=self.table.nrows
    def login_data(self):
        if self.rownum<1:
            print("总行数小于一")
        else:
            result=[]
            for line in range(self.rownum):
                shuju=self.table.row_values(line)
                result.append(shuju)
                print(shuju)
            return result