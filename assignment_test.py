import assignment


def test_firstFive():
    assert assignment.firstFive("akumiitti") == "akumi"
    assert assignment.firstFive("saippuakauppias") == "saipp"


def test_lastFive():
    assert assignment.lastFive("akumiitti") == "iitti"
    assert assignment.lastFive("saippuakauppias") == "ppias"


def test_middleFour():
    assert assignment.middleFour("akumiitti") == "kumi"
    assert assignment.middleFour("saippuakauppias") == "aipp"


def test_everyOther():
    assert assignment.everyOther("akumiitti") == "kmit"
    assert assignment.everyOther("saippuakauppias") == "apukupa"


def test_backwards():
    assert assignment.backwards("akumiitti") == "ittiimuka"
    assert assignment.backwards("saippuakauppias") == "saippuakauppias"