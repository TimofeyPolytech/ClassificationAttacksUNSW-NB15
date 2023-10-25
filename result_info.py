import json


def write_result_info(ip_src, ip_dst, src_port, dst_port, triggered_model, triggered_model_proba, name_of_file):
    data = {}
    count_data = 0
    for i in range(len(triggered_model)):
        if triggered_model[i] == 'Normal':
            i += 1
            continue
        data[count_data] = {
            'IP-source': str(ip_src[i]),
            'IP-destination': str(ip_dst[i]),
            'source port': str(src_port[i]),
            'destination port': str(dst_port[i]),
            'model_name': str(triggered_model[i]),
            'model_probability': str(triggered_model_proba[i]),
        }
        count_data += 1
    with open(name_of_file + '.json', 'w') as f:
        json.dump(data, f, indent=6)
