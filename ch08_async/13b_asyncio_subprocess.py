"""
    13b_asyncio_subprocess.py   -   creates a list of coroutines based on multiple
                                    commands to execute from the operating system
                                    Schedules all coroutines using gather + run_until_complete().
                                    Displays results at the end.
"""
import time
import platform
import asyncio


async def run_process(cmd):
    process = await asyncio.create_subprocess_exec(*cmd, stdout=asyncio.subprocess.PIPE)
    pid = process.pid
    print('Started pid: {0}'.format(pid))

    stdout, _ = await process.communicate()
    status = ('successful' if process.returncode == 0 else 'failed')
    print('Pid: {0} {1}, Cmd: ({2})'.format(process.pid, status, cmd))

    return stdout.decode().strip()


def add_tasks_to_loop(tasks, loop):
    commands = asyncio.gather(*tasks)
    results = loop.run_until_complete(commands)
    loop.close()
    return results

loop = asyncio.get_event_loop()
if platform.system() == 'Windows':
    loop = asyncio.ProactorEventLoop()
    asyncio.set_event_loop(loop)


if platform.system() == 'Windows':
    commands = [
        ['hostname'],
        ['ping', '-n', '2', 'www.google.com']
    ]
else:
    commands = [
        ['hostname'],
        ['ping', '-c', '2', 'www.google.com']
    ]

if __name__ == '__main__':
    start = time.time()
    tasks = []
    for command in commands:
        tasks.append(run_process(command))                      # creates a list of coroutines
    results = add_tasks_to_loop(tasks, loop)
    print('Results:', results)
    end = time.time()
    print('Execution time: {0:.3f} secs'.format(end - start))
