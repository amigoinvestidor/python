import datetime

def AnbimaDates(DDMMAAAA):
    """
    Retorna o dia útil anterior à data informada (DDMMAAAA), excluindo sábados, domingos e feriados.

    Exemplo:
        >>> from anbima import AnbimaDates
        >>> AnbimaDates("01012025")
        '31122024'
    """
    dt = datetime.datetime.strptime(DDMMAAAA, "%d%m%Y").date()
    y = dt.year

    # Algoritmo da Páscoa (Meeus/Jones/Butcher)
    a = y % 19
    b = y // 100
    c = y % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    mEaster = (h + l - 7 * m + 114) // 31
    dEaster = ((h + l - 7 * m + 114) % 31) + 1
    Easter = datetime.date(y, mEaster, dEaster)

    # Feriados móveis baseados na Páscoa
    Carnival1 = Easter - datetime.timedelta(days=48)
    Carnival2 = Easter - datetime.timedelta(days=47)
    GoodFriday = Easter - datetime.timedelta(days=2)
    CorpusChristi = Easter + datetime.timedelta(days=60)

    # Feriados nacionais
    AnbimaDatesHolidays = {
        datetime.date(y, 1, 1): "Confraternização Universal",
        Carnival1: "Carnaval (Segunda-feira)",
        Carnival2: "Carnaval (Terça-feira)",
        GoodFriday: "Paixão de Cristo",
        datetime.date(y, 4, 21): "Tiradentes",
        datetime.date(y, 5, 1): "Dia do Trabalho",
        CorpusChristi: "Corpus Christi",
        datetime.date(y, 9, 7): "Independência do Brasil",
        datetime.date(y, 10, 12): "Nossa Sr.a Aparecida - Padroeira do Brasil",
        datetime.date(y, 11, 2): "Finados",
        datetime.date(y, 11, 15): "Proclamação da República",
        datetime.date(y, 11, 20): "Dia da Consciência Negra",
        datetime.date(y, 12, 25): "Natal",
    }

    # Encontrar o dia útil anterior
    prevBizDate = dt - datetime.timedelta(days=1)
    while prevBizDate.weekday() >= 5 or prevBizDate in AnbimaDatesHolidays:
        prevBizDate -= datetime.timedelta(days=1)

    return prevBizDate.strftime("%d%m%Y")