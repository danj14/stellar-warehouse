import re
import decimal

"""
    Inspired by Jinja
    https://jinja.palletsprojects.com/en
"""

class PgPyLite:
    def __init__(self, record, query_buffer):
        self.param = '{{.*}}'
        self.type_splitter = ' as '
        self.query_buffer = query_buffer
        self.record = record
        self.parameters = [
           p.replace('{{', '').replace('}}', '').split(self.type_splitter) for p in re.findall(self.param, query_buffer)
        ]

    def convert_parameters(self, drop_missing):
        if drop_missing:
            check_keys = [k[0] for k in self.parameters]
            drop_keys = [k for k in self.record.keys() if k not in check_keys]
            for key in drop_keys:
                del self.record[key]

        for param in self.parameters:
            conversion = param[1]
            parameter = param[0]
            if parameter not in self.record:
                return f'{param} is not included in the provided record!'
            value = self.record[parameter]
            # strings -> add literal quotes
            if conversion == 'str':
                self.record[parameter] = f"'{str(value)}'"
            # integers -> simple int()
            elif conversion == 'int':
                self.record[parameter] = int(value)
            # decimals -> are six place precision (real)
            elif conversion == 'real':
                decimal.getcontext().prec = 6
                self.record[parameter] = decimal.Decimal(value) + decimal.Decimal(0)
            # bool -> return true/false (lower case)?
            elif conversion == 'bool':
                self.record[parameter] = value.lower()

    def executable_query(self):
        # loop through params and replace them in query buffer
        # return re.sub(self.param, blehvar, self.query_buffer, count=0)
        # self.query_string = re.sub(self.param, 'poop', query_buffer, count=0)
        # print(self.query_string)
        query = self.query_buffer
        for key, value in self.record.items():
            parameter_pattern = '{{' + key + ' .*}}'
            query = re.sub(parameter_pattern, str(value), query, count=0)
        return query
