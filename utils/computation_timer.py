import time
import sys

if sys.platform == "win32":
    # print("Using time.clock")
    timer = time.clock  # best on Windows
else:
    # print("Using time.time")
    timer = time.time  # normally best on Mac or Linux


def computation_timer(*func_dicts):
    """
    Function to time multiple alternative computations.

    Args:
        Any number of dicts each containing at least a 'func' key containing a 
        reference to a function to be timed.

    Returns:
        A list of the dicts provided as arguments with "running_time" and 
        "result" keys and corresponding values added. If an exception 
        occurs in the running of one of provided functions, it is returned as 
        the result for the corresponding dict with a running time of -1.
    """
    results = []
    for func_dict in func_dicts:
        result = func_dict
        time_0 = timer()
        try:
            result['result'] = func_dict['func']()
            time_1 = timer()
            result['running_time'] = time_1 - time_0
        except Exception as e:
            result['result'] = e
            result['running_time'] = -1
        results.append(result)
    return results
