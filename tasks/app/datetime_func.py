def show_date_time():
    import datetime
    current_date = datetime.datetime.today().weekday()
    week = {
    "0": "Понедельник",
    "1": "Вторник",
    "2": "Среда",
    "3": "Четверг",
    "4": "Пятница",
    "5": "Суббота",
    "6": "Воскресение"
}
    html_text = f"""
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Текущий день недели: {week[str(current_date)]}<h1>

</body>
</html>

    """

    func = open('app/templates/datetime.html', 'w', encoding='utf-8')
    # Если не написать енкодинг в конце, то будет ошибка декодинга.
    func.write(html_text)
    func.close()
        
