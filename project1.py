import logging

logging.basicConfig(filename='mylog.log', level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

logging.info('This is an informational message')
logging.warning('This is a warning message')
logging.error('This is an error message')

def read_log_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def process_log_lines(lines):
    processed_data = []
    for line in lines:
        processed_data.append(line.strip())
    return processed_data

def analyze_data(data):
    analysis_result = {}
    for item in data:
        if item in analysis_result:
            analysis_result[item] += 1
        else:
            analysis_result[item] = 1
    return analysis_result

def main():
    file_path = 'mylog.log'
    lines = read_log_file(file_path)
    processed_data = process_log_lines(lines)
    analysis_result = analyze_data(processed_data)
    print(analysis_result)

if __name__ == "__main__":
    main()
