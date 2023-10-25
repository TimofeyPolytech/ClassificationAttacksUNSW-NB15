def data_preproc(data):
    data.columns = ['srcip', 'sport', 'dstip', 'dsport', 'proto', 'state', 'dur', 'sbytes', 'dbytes', 'sttl', 'dttl',
                    'sloss', 'dloss', 'service', 'sload', 'dload', 'spkts', 'dpkts', 'swin', 'dwin', 'stcpb', 'dtcpb',
                    'smean', 'dmean', 'trans_depth', 'response_body_len', 'sjit', 'djit', 'stime', 'ltime', 'sinpkt',
                    'dinpkt', 'tcprtt', 'synack', 'ackdat', 'is_sm_ips_ports', 'ct_state_ttl', 'ct_flw_http_mthd',
                    'is_ftp_login', 'ct_ftp_cmd', 'ct_srv_src', 'ct_srv_dst', 'ct_dst_ltm', 'ct_src_ltm',
                    'ct_src_dport_ltm', 'ct_dst_sport_ltm', 'ct_dst_src_ltm', 'attack_cat', 'label']

    src_ip = data['srcip']
    dst_ip = data['dstip']
    src_port = data['sport']
    dst_port = data['dsport']

    new_data = data[['sttl', 'smean', 'sbytes', 'dmean', 'proto', 'dload', 'ct_srv_dst', 'ct_dst_src_ltm', 'ct_srv_src',
                     'sloss', 'service', 'trans_depth', 'ackdat', 'ct_flw_http_mthd', 'synack', 'dwin', 'dbytes',
                     'sload', 'ct_state_ttl', 'dur', 'dttl', 'ct_dst_sport_ltm', 'dloss', 'tcprtt',
                     'response_body_len', 'sjit', 'sinpkt', 'ct_src_dport_ltm', 'djit', 'ct_dst_ltm', 'stcpb', 'dpkts',
                     'state', 'swin', 'dinpkt', 'spkts', 'dtcpb', 'ct_src_ltm']]

    return new_data, src_ip, dst_ip, src_port, dst_port
