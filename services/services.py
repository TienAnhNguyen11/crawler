import datetime
from db.session import myDB


def get_list_type(area):
    if area.isupper() is not True:
        return {
            'code': 1,
            'description': 'City name is not valid!'
        }
    else:
        myCollection = myDB["type_gold"]
        data_resp = []
        final_data_resp = []
        for x in myCollection.find({'area': area}):
            remove_keys = ["_id", 'website']
            resp = {remove_key: x[remove_key] for remove_key in x if remove_key not in remove_keys}
            data_resp.append(resp)

        for i in data_resp:
            if i not in final_data_resp:
                final_data_resp.append(i)

        return {
            'area': area,
            'code': 0,
            'data': final_data_resp
        }


def get_daily_price(from_date, to_date, area, type_):
    myCollection = myDB["daily_price"]
    data_resp = []
    final_data_resp = []
    from_date = datetime.datetime.strptime(from_date, '%d%m%Y')
    to_date = datetime.datetime.strptime(to_date, '%d%m%Y')
    to_date += datetime.timedelta(days=1)
    filters = {'date_time': {'$gte': from_date, '$lte': to_date}}

    if type_ and area:
        filters['area'] = area
        filters['type'] = type_
        for data in myCollection.find(filters):
            remove_keys = ["_id"]
            resp = {remove_key: data[remove_key] for remove_key in data if remove_key not in remove_keys}
            data_resp.append(resp)

        for data in data_resp:
            if data not in final_data_resp:
                final_data_resp.append(data)

        return {
            'data': final_data_resp,
        }

    elif type_ and not area:
        filters['type'] = type_
        for data in myCollection.find(filters):
            remove_keys = ["_id"]
            resp = {remove_key: data[remove_key] for remove_key in data if remove_key not in remove_keys}
            data_resp.append(resp)

        for data in data_resp:
            if data not in final_data_resp:
                final_data_resp.append(data)

        return {
            'data': final_data_resp,
        }

    elif area and not type_:
        filters['area'] = area
        for data in myCollection.find(filters):
            remove_keys = ["_id"]
            resp = {remove_key: data[remove_key] for remove_key in data if remove_key not in remove_keys}
            data_resp.append(resp)

        for data in data_resp:
            if data not in final_data_resp:
                final_data_resp.append(data)

        return {
            'data': final_data_resp,
        }

    else:
        for data in myCollection.find({'date_time': {'$gte': from_date, '$lte': to_date}}):
            remove_keys = ["_id"]
            resp = {remove_key: data[remove_key] for remove_key in data if remove_key not in remove_keys}
            data_resp.append(resp)
        for data in data_resp:
            if data not in final_data_resp:
                final_data_resp.append(data)

        return {
            'data': final_data_resp,
        }


def get_realtime_price(from_date, to_date, type_):
    myCollection = myDB["realtime_price"]
    data_resp = []
    final_data_resp = []
    from_date = datetime.datetime.strptime(from_date, '%d%m%Y')
    to_date = datetime.datetime.strptime(to_date, '%d%m%Y')
    to_date += datetime.timedelta(days=1)

    filters = {'date_time': {'$gte': from_date, '$lte': to_date}}

    if type_:
        filters['type'] = type_
        for data in myCollection.find(filters):
            remove_keys = ["_id"]
            resp = {remove_key: data[remove_key] for remove_key in data if remove_key not in remove_keys}
            data_resp.append(resp)

        for data in data_resp:
            if data not in final_data_resp:
                final_data_resp.append(data)

        return {
            'data': final_data_resp,
        }

    else:
        for data in myCollection.find(filters):
            remove_keys = ["_id"]
            resp = {remove_key: data[remove_key] for remove_key in data if remove_key not in remove_keys}
            data_resp.append(resp)

        for data in data_resp:
            if data not in final_data_resp:
                final_data_resp.append(data)

        return {
            'data': final_data_resp,
        }