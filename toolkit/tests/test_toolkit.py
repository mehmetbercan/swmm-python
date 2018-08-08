#
#  test_toolkit.py
#   
#  Created:    8/8/2018
#  Author:     Michael E. Tryby
#              US EPA - ORD/NRMRL
#  

import pytest

from swmm.toolkit import toolkit as smtk

from data import INPUT_FILE_EXAMPLE_1, REPORT_FILE_TEST, OUTPUT_FILE_TEST


def test_allocfree():
    _handle = smtk.alloc_project()
    assert(_handle != None)
    _handle = smtk.free_project(_handle)
    assert(_handle == None)

 
def test_run():
    _handle = smtk.alloc_project()
    smtk.run(_handle, INPUT_FILE_EXAMPLE_1, REPORT_FILE_TEST, OUTPUT_FILE_TEST)
    smtk.free_project(_handle)
    
    
def test_openclose():
    _handle = smtk.alloc_project()
    smtk.open(_handle, INPUT_FILE_EXAMPLE_1, REPORT_FILE_TEST, OUTPUT_FILE_TEST)
    smtk.close(_handle)
    smtk.free_project(_handle)

    
@pytest.fixture()
def handle(request):    
    _handle = smtk.alloc_project()
    smtk.open(_handle, INPUT_FILE_EXAMPLE_1, REPORT_FILE_TEST, OUTPUT_FILE_TEST)
    
    def close():
        smtk.close(_handle)
        smtk.free_project(_handle)
    
    request.addfinalizer(close)    
    return _handle    


def test_step(handle):
     
     smtk.start(handle, 0)
     
     while True:
         time = smtk.step(handle)
         
         if time == 0.:
             break

     smtk.end(handle)
     
     smtk.report(handle)

