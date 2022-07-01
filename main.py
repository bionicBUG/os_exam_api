from fastapi import FastAPI
from fastapi.responses import FileResponse

api = FastAPI()

@api.get("/fork_pid")
def fork():
    return FileResponse(
        'fork_pid.cpp',
        media_type='text'
    )

@api.get("/wait")
def wait():
    return FileResponse(
        'wait.cpp',
        media_type='text'
    )

@api.get("/ms")
def ms():
    return FileResponse(
        'message_sharing.cpp',
        media_type='text'
    )

@api.get("/queue")
def ms():
    return FileResponse(
        'queue.cpp',
        media_type='text'
    )


@api.get("/pipe")
def ms():
    return FileResponse(
        'pipe.c',
        media_type='text'
    )

@api.get("/semaphore")
def ms():
    return FileResponse(
        'semaphore.cpp',
        media_type='text'
    )


@api.get("/odd_even")
def ms():
    return FileResponse(
        'odd_even.cpp',
        media_type='text'
    )

@api.get("/monitor")
def ms():
    return FileResponse(
        'monitor.cpp',
        media_type='text'
    )

@api.get("/insert_sort")
def ms():
    return FileResponse(
        'insert_sort.c',
        media_type='text'
    )

@api.get("/dining")
def ms():
    return FileResponse(
        'dining.c',
        media_type='text'
    )

@api.get("/fcfs")
def ms():
    return FileResponse(
        'fcfs.c',
        media_type='text'
    )

@api.get("/prior")
def ms():
    return FileResponse(
        'prior.cpp',
        media_type='text'
    )

@api.get("/rr")
def ms():
    return FileResponse(
        'rr.cpp',
        media_type='text'
    )

@api.get("/srtf")
def ms():
    return FileResponse(
        'srtf.cpp',
        media_type='text'
    )