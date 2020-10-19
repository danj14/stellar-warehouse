"""
    Inspired by Jinja
    https://jinja.palletsprojects.com/en
"""
import re
import decimal

parameter = '{{.*}}'
data_type_splitter = ' as '
query_parameters = lambda query_buffer: [p.replace('{{','').replace('}}','')
                                       .split(data_type_splitter) for p in re.findall(parameter, query_buffer)]
query_parameter_list = []

def cast_parameters(drop_missing, record):
    if drop_missing:
        check_keys = [k[0] for k in query_parameter_list]
        drop_keys = [k for k in record.keys() if k not in check_keys]
        for k in drop_keys:
            del record[k]

    for p in query_parameter_list:
        attribute = p[0]
        cast_type = p[1]
        if attribute not in record:
            return f'{attribute} is not included in the provided record.'
        record_value = record[attribute]
        if cast_type == 'str':
            record[attribute] = f"'{str(record_value)}'"
        elif cast_type == 'int':
            record[attribute] = int(record_value)
        # decimals -> are six place precision (real)
        elif cast_type == 'real':
            decimal.getcontext().prec = 6
            record[attribute] = decimal.Decimal(record_value) + decimal.Decimal(0)
        # bool -> return true/false (lower case)?
        elif cast_type == 'bool':
            record[attribute] = record_value.lower()

def generate_query(query, record):
    # TODO: a separate loop or some way to determine returning multiple queries to execute (for array/objects)
    for k, v in record.items():
        param_pattern = '{{' + k + ' .*}}'
        query = re.sub(param_pattern, str(v), query, count=0)
    print(type(query))
    # return query
