url = input("Nhập url: ")

# Sample url: https://example.com/api?user=john&age=25&role=admin
# https://example.com/api

def extract_params(url):
    index = url.find('?')
    if index == -1 or index == len(url) - 1:
        return "Không có query parameters"
    query_string = url[index + 1:]
    query_params = query_string.split('&')
    result = {}

    for query_param in query_params:
        if '=' in query_param:
            key, value = query_param.split('=')
            result[key] = value
    return result

print(extract_params(url))