import os
import subprocess, json, sys

test_folder = '../ttt'
report_name = 'report.json'
a = subprocess.run(['pytest', test_folder, '--json-report', f'--json-report-file={report_name}'])
ret0 = a.returncode
print(f'Tests succedeed with code {ret0}' if ret0 == 0 else f'Tests failed with code {ret0}')
if ret0 != 0:
    print('Parsing report...')
    with open(report_name, encoding='utf-8') as inp:
        report_json = json.load(inp)
        print(f"Passed tests: {report_json['summary']['passed']}", \
              f"Failed tests: {report_json['summary']['failed']}", sep='\n')
    print(f'You can find report in {os.getcwd() + '\\' + report_name}')
