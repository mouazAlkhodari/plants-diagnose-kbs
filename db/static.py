''' data shape '''
'''
{
    'PLANT_NAME':[
        {
            'name':'DISEASE_NAME',
            'details':'DISEASE_DETAILS',
            'link':'DISEASE_LINK',
            'symptoms':[
                {
                    'name':'SYMPTOM_NAME',
                    'CF':'CF_VALUE'
                }
            ]
        }
    ]
}
'''


''' static data used in case there is any error'''
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
    ],
    'الملفوف(Cabbage)': [
        {
            'name': 'نقص النيتروجين Nitrogen Deficiency in cabbage',
            'link': 'https://www.al-hakem.com/نقص-النيتروجين-على-الملفوف-و-القرنبيط/',
            'symptoms': [
                {'name': 'أوراق أصغر من الأوراق الطبيعية',   'CF': 0.3},
                {'name': 'أوراق لونها أخضر باهت مصفر',      'CF': 0.9},
                {'name': 'الساق تكون رقيقة وصلبة',          'CF': 0.5},
                {'name': 'النمو ببطء',                       'CF': 0.2},
            ]
        }
    ]
}

plants_Array = ['الملفوف(Cabbage)', 'p2']
