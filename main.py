from cbTypes import Resource
from code_metrics import SolutionMetrics
from collector.actions import ActionCollector
from collector.code_metrics_extractor import Solution
from collector.executions import ExecutionCollector
from filters import Filters
from parser.actions import ActionsParser
from parser.executions import ExecutionParser
from utils import save

# TODO: make dataset extractor more interactive.
# 1. Prompt to select options
# 2. Input dataset source
# 3. Organize elements (maybe model is a good solution)

def generate_assessments():
    srcs = (
        '/home/jackson/Documentos/UFAM/8_Periodo/TCC/Dataset/collection/2017-1',
        '/home/jackson/Documentos/UFAM/8_Periodo/TCC/Dataset/collection/2017-2',
        '/home/jackson/Documentos/UFAM/8_Periodo/TCC/Dataset/collection/2018-1',
        '/home/jackson/Documentos/UFAM/8_Periodo/TCC/Dataset/collection/2018-2',
        '/home/jackson/Documentos/UFAM/8_Periodo/TCC/Dataset/collection/2019-1',
        '/home/jackson/Documentos/UFAM/8_Periodo/TCC/Dataset/collection/2019-2',
        '/home/jackson/Documentos/UFAM/8_Periodo/TCC/Dataset/collection/2021-1',
    )
    kinds = ['exam']
    assessments = set()

    for src in srcs:
        data = Filters.get(src, kinds)
        for id in data:
            assessments.add(id)

    save('output/data', 'assessments', [{ 'id': id } for id in assessments], ['id'])

def main():
    srcs = (
        '/home/jackson/Documentos/UFAM/8_Periodo/TCC/Dataset/collection/2017-1',
        '/home/jackson/Documentos/UFAM/8_Periodo/TCC/Dataset/collection/2017-2',
        '/home/jackson/Documentos/UFAM/8_Periodo/TCC/Dataset/collection/2018-1',
        '/home/jackson/Documentos/UFAM/8_Periodo/TCC/Dataset/collection/2018-2',
        '/home/jackson/Documentos/UFAM/8_Periodo/TCC/Dataset/collection/2019-1',
        '/home/jackson/Documentos/UFAM/8_Periodo/TCC/Dataset/collection/2019-2',
        '/home/jackson/Documentos/UFAM/8_Periodo/TCC/Dataset/collection/2021-1',
    )
    kinds = ['exam']

    data = ExecutionParser(
        *srcs,
        resource=Resource.EXECUTIONS
    )

    src = data.collect(kinds=kinds)
    ExecutionCollector.collect(src)

    parser = ActionsParser(
        *srcs,
        resource=Resource.CODEMIRRORS
    )
    src = parser.collect(kinds=kinds)
    ActionCollector.collect(src)

def generate_code_metrics():
    src = '/home/jackson/Documentos/UFAM/8_Periodo/TCC/Dataset/codigos_solucao.csv'
    res = Solution.extract_from_professor(src)
    # for key, value in res.items():
    #     print(key, value)
        # print('*****************-*******************')
    # print(res.items(), sep='\n')
    # dict_sols = [ vars(code) for code in res ]
    csv_fields = list(vars(SolutionMetrics()).keys())
    save('output/data', 'code_metrics_professor.csv', res, ['question_id', *csv_fields])

if __name__ == '__main__':
    # main()
    generate_assessments()
    # generate_code_metrics()