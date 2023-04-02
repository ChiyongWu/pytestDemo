from common.logger import logger
import pytest, time


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


def pytest_terminal_summary(terminalreporter):
    """
    收集测试结果
    """

    _PASSED = len([i for i in terminalreporter.stats.get('passed', []) if i.when != 'teardown'])
    _ERROR = len([i for i in terminalreporter.stats.get('error', []) if i.when != 'teardown'])
    _FAILED = len([i for i in terminalreporter.stats.get('failed', []) if i.when != 'teardown'])
    _SKIPPED = len([i for i in terminalreporter.stats.get('skipped', []) if i.when != 'teardown'])
    _TOTAL = terminalreporter._numcollected
    _TIMES = time.time() - terminalreporter._sessionstarttime

    logger.info(f"成功用例数: {_PASSED}")
    logger.error(f"异常用例数: {_ERROR}")
    logger.error(f"失败用例数: {_FAILED}")
    logger.warning(f"跳过用例数: {_SKIPPED}")
    logger.info("用例执行时长: %.2f" % _TIMES + " s")

    try:
        _RATE = round(_PASSED / _TOTAL * 100, 2)
        logger.info("用例成功率: %.2f" % _RATE + " %")
    except ZeroDivisionError:
        logger.info("用例成功率: 0.00 %")