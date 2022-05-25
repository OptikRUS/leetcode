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
    aws = []
    for i in range(5):
        aws.append(get_uid())
    await asyncio.gather(*aws)

    future_aws = []
    for i in range(5):
        future_aws.append(asyncio.ensure_future(get_uid()))
    await asyncio.gather(*future_aws)

asyncio.run(main())
