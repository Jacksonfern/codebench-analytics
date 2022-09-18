from cbTypes import Data
from components import Components
from os import path

class Filters:
    """
    Filter assessmentes by set of kinds.
    """

    @staticmethod
    def get(dataset_src, kinds = None):
        assessments = Components.getData(dataset_src, Data.ASSESSMENT)
        assessment_ids = []

        for assessment in assessments:
                filename = path.basename(assessment)
                fullpath = path.join(dataset_src, assessment)
                id = filename.split('.')[0]
                with open(fullpath, 'r') as file:
                    for line in file:
                        if line.startswith('---- type:'):
                            kind = line.split(':')[-1].strip()
                            if not kinds or kind in kinds:
                                assessment_ids.append(int(id))
                                break
        
        return assessment_ids

if __name__ == '__main__':
    d = Filters.get('/home/jackson/Documentos/UFAM/8_Periodo/TCC/Dataset/collection/2017-1')
    print(d)
