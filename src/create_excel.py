import openpyxl


class ExcelWriter:
    def write_to_excel(self, flats):
        filename='flats_to_rent_edinburgh.xlsx'
        excel = openpyxl.Workbook()
        sheet = excel.active
        sheet.title = "Flats to rent in Edinburgh"
        sheet.append(["Number", "Area", "Address", "Postcode", "Rent", "No of Bedrooms", "Estage Agent"])

        for flat in flats:
            sheet.append([
                flat["number"],
                flat["area"],
                flat["address"],
                flat["postcode"],
                flat["rent"],
                flat["no_of_rooms"],
                flat["estate_agent"]
            ])
        excel.save(filename)
        