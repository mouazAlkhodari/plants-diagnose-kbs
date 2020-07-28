''' data shape '''
'''
{
    'PLANT_NAME':[
        {
            'name':'DISEASE_NAME',
            'name_ar':'DISEASE_NAME_AR',
            'details':'DISEASE_DETAILS',
            'link':'DISEASE_LINK',
            'symptoms':[
                {
                    'name':'SYMPTOM_NAME',
                    'CF':'CF_VALUE',
                    'question':'SYMPTOM_QUESTION'
                }
            ]
        }
    ]
}
'''


''' static data '''
Disease_Data = {
    'p1': [
        {
            'plant': 'p1',
            'name': 'D1',
            'symptoms': [
                {'name': 's1', 'CF': 0.3},
                {'name': 's2', 'CF': 0.2}
            ]
        },
        {
            'plant': 'p1',
            'name': 'D2',
            'symptoms': [
                {'name': 's1', 'CF': 0.3},
                {'name': 's3', 'CF': 0.5}
            ]
        }
    ],
    'p2': [
        {
            'plant': 'p2',
            'name': 'D1',
            'symptoms': [
                {'name': 's1', 'CF': 0.3},
                {'name': 's2', 'CF': 0.2},
                {'name': 's4', 'CF': 0.6}
            ]
        },
        {
            'plant': 'p2',
            'name': 'D3',
            'symptoms': [
                {'name': 's3', 'CF': 0.9},
                {'name': 's4', 'CF': 0.1}
            ]
        }
    ]
}

plants_Array = ['p1', 'p2']
