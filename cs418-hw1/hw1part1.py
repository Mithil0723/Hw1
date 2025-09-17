import pandas as pd
import numpy as np

# 2% credit
def extract_hour(time):
    """
    Extracts hour information from military time
    
    Args: 
        time (float64): series of time given in military format.  
          Takes on values in 0.0-2359.0 due to float64 representation.
    
    Returns:
        array (float64): series of input dimension with hour information.  
          Should only take on integer values in 0-23
    """
    hour = (time // 100).astype(float)
    hour = hour.where((hour >= 0) & (hour <= 23), np.nan)
    return hour

# 2% credit
def extract_mins(time):
    """
    Extracts minute information from military time
    
    Args: 
        time (float64): series of time given in military format.  
          Takes on values in 0.0-2359.0 due to float64 representation.
    
    Returns:
        array (float64): series of input dimension with minute information.  
          Should only take on integer values in 0-59
    """
    minutes = time % 100
    minutes = minutes.where((minutes >= 0) & (minutes <= 59), np.nan)
    return minutes

# 2% credit
def convert_to_minofday(time):
    """
    Converts HH:MM:SS time to minute of day
    
    Args:
        time: series of time given as strings in HH:MM:SS format.  
          
    
    Returns:
        array (float64): series of input dimension with minute of day
    
    Example: 13:03 is converted to 783.0
    """
    dt = pd.to_datetime(time, format='%H:%M:%S', errors='coerce')
    minofday = dt.dt.hour * 60 + dt.dt.minute
    return minofday.astype(float)

# 3%credit
def assigned_scheduled_times(arrival_times, scheduled_times):
    """
    Calculates delay times y - x
    
    Args:
        arrival_times: series of scheduled times 
        scheduled_times: series of actual arrival times
    
    Returns:
        arrival_scheduled_times: pandas dataframe with two columns viz., arrival times and corresponding scheduled time
    """
    arrival_s = arrival_times.sort_values().rename("Arrival Times")
    scheduled_s = scheduled_times.sort_values().rename("Scheduled Times")

    merged = pd.merge_asof(
        left=arrival_s.to_frame(),
        right=scheduled_s.to_frame(),
        left_on="Arrival Times",
        right_on="Scheduled Times",
        direction="nearest",
    )
    return merged

# 3% credit
def calc_delay(assigned_scheduled_times):
    """
    Calculates delay times y - x
    
    Args:
        assigned_scheduled_times: pandas dataframe with two columns viz., arrival times and corresponding scheduled time
    
    Returns: 
        pandas series of input dimension with delay time
    """
    df = assigned_scheduled_times
    if 0 in df.columns and 1 in df.columns and len(df.columns) == 2:
        return df[1] - df[0]
    else:
        return df['Arrival Times'] - df['Scheduled Times']
