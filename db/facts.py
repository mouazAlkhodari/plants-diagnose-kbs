from custom_facts import Disease

fact = Disease(**{
    "state": "INITIAL",
    "plant": "ملفوف - Cabbage",
    "name": "نقص النيتروجين \nNitrogen Deficiency in cabbage\n",
    "link": "https://www.al-hakem.com/نقص-النيتروجين-على-الملفوف-و-القرنبيط/",
    "details": "",
    "symptoms": {
        "smaller leaves": {
            "question": "what about smaller leaves?", "name": "smaller leaves",
            "nameAr": "أوراق أصغر من الأوراق الطبيعية", "CF": 0.5
        },
        "yellowish-green leaves": {
            "question": "what about yellowish-green leaves?", "name": "yellowish-green leaves",
            "nameAr": "أوراق لونها أخضر باهت مصفر", "CF": 0.2
        },
        "The leg is thin and solid": {
            "question": "what about The leg is thin and solid?", "name": "The leg is thin and solid",
            "nameAr": "الساق تكون رقيقة وصلبة", "CF": 0.6
        },
        "slow growth": {
            "question": "what about slow growth?", "name": "slow growth",
            "nameAr": "النمو ببطء", "CF": 0.4
        }
    }
})


