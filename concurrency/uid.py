"""
Написать асинхронную функцию, которая будет делать следующее:
- формировать уникальный идентификатор (uuid)
- асинхронно спать 2 секунды
- после сна на экране должно появляться сообщение "функция <uuid> спать закончила!"

На основе написанной функции сформировать список или кортеж из 5 корутин и отдать их в работу ивент лупу с помощью
gather.

Написать аналог асинхронного запуска посредством цикла и функции ensure_future.

Что изменится, если в цикле вместо ensure_future использовать await для запуска очередной корутины?

Что изменится, если мы будем использовать sleep из модуля time?

Объясните полученные результаты.
"""

import asyncio
from uuid import uuid4


async def get_uid():
    uid = uuid4()
    await asyncio.sleep(2)
    print(f'Функция {uid} спать закончила!')


async def main():
    for i in range(5):
        asyncio.ensure_future(get_uid())

    aws = []
    for i in range(5):
        aws.append(get_uid())
    await asyncio.gather(*aws)


asyncio.run(main())


"""
Если цикл с ensure_future выполнить после цикла с gather, то от первого мы результата не увидим.
Если перед ensure_future поставить await6 то будем ждать выполнения каждой функции по 2 секунды.
Если использовать стандартный sleep, то функции будут работать синхронно.
"""