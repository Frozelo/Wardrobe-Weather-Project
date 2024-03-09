def parse_optimal_temperature(value):
    min_temp, max_temp = map(float, value.split(':'))
    return {'min_temp': min_temp, 'max_temp': max_temp}


def get_request_params(request, params=(), source='POST'):
    request_params = {}
    source_data = getattr(request, source, {})

    for param in params:
        if param in source_data:
            if param == 'optimal_temperature':
                request_params[param] = parse_optimal_temperature(source_data[param])
            else:
                request_params[param] = source_data[param]

    return request_params
