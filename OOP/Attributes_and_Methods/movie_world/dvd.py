class DVD:
    months = {
        '1': 'January', '2': 'February', '3': 'March', '4': 'April',
        '5': 'May', '6': 'June', '7': 'July', '8': 'August', '9': 'September',
        '10': 'October', '11': 'November', '12': 'December'
    }

    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = int(id)
        self.creation_year = int(creation_year)
        self.creation_month = creation_month
        self.age_restriction = int(age_restriction)
        self.is_rented = False

    def __repr__(self):
        status = None
        if self.is_rented:
            status = 'rented'
        else:
            status = 'not rented'
        output = f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age " \
                 f"restriction {self.age_restriction}. Status: {status}"
        return output

    @classmethod
    def from_date(cls, id, name, date, age_restriction):
        date = date.split('.')
        year = date[2]
        month_num = date[1]
        month = DVD.months[month_num]
        return cls(name, id, year, month, age_restriction)
