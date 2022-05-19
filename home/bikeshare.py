import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
   
# TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('which city you prefer to explore data for (chicago, new york city, washington)?').lower()
    while city not in CITY_DATA.keys():
        print('please, you have to insert valid data!')
        city = input('which city you prefer to explore data for (chicago, new york city, washington)?').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('which month you prefer to filter data for (january, february, ... , june) or (all) for filter all months?').lower()
        months = ['january', 'february', 'march' , 'april' , 'may' , 'june']
        if month != 'all' and month not in months:
            print('please, you have to insert valid month!')
        else:
            break
    # TfebruaryO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('which day of week you prefer to filter data for (monday, tuesday, ... sunday) or (all) for all days?').lower()
        days = ['saturday' ,'sunday' ,'monday' ,'tuesday' ,'wednesday' ,'thursday' ,'friday']
        if day != 'all' and day not in days:
                print('please, you have to insert valid day!')
        else:
            break
    
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['week_day'] = df['Start Time'].dt.day_name()
    if month != 'all':
        months = ['january', 'february', 'march' , 'april' , 'may' , 'june']
        month = months.index(month)+1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['week_day'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march' , 'april' , 'may' , 'june']
    month = df['month'].mode()[0]
    common_month = months[month-1] 
    print('The Most common Month is {}'.format(common_month))
  
    # TO DO: display the most common day of week
    day = df['week_day'].mode()[0]
    print('The Most Common Day Of Week is {}'.format(day))
    # TO DO: display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    start_hour = df['Hour'].mode()[0]
    print('The Most Common Start Hour is {}'.format(start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The Most Commonly Used Start Station is {}'.format(common_start_station))     
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The Most Commonly Used End Station is {}'.format(common_end_station))  

    # TO DO: display most frequent combination of start station and end station trip
    df['common_trip'] = ' From ' + df['Start Station'] + ' To ' + df['End Station']
    trip = df['common_trip'].mode()[0]
    print(' most frequent combination of start station and end station trip >>> {}'.format(trip))      
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()  
    print(' The Total Travel Time is {}'.format(total_travel_time))
    # TO DO: display mean travel time
    AVG_travel_time = df['Trip Duration'].mean()  
    print(' The Average Travel Time is {}'.format(AVG_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df ,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts = df['User Type'].value_counts()
    print('Counts Of User Types \n' , counts)     

    # TO DO: Display counts of gender
    if city != 'washington':
          counts_of_gender = df['Gender'].value_counts()
          print('Counts Of Gender \n' , counts_of_gender) 
          # TO DO: Display earliest, most recent, and most common year of birth
          earliest = df['Birth Year'].min()
          recent = df['Birth Year'].max()
          common_year = df['Birth Year'].mode()[0]
          print('The Earliest Year Of Birth is {}'.format(earliest))
          print('The Most Recent Year Of Birth is {}'.format(recent))
          print('The Most Common Year Of Birth is {}'.format(common_year))
          
          print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """display row data for user."""
    print('\n data is loading...\n')
   
    
    view_data = input("Would you like to view the first 5 rows of individual trip data? Enter yes or no?").lower()
    response =['yes' ,'no']
    start_loc = 0
    while view_data not in response:
        print('please enter (yes) if you want to see data or (no) if you didn\'t')
        view_data = input("Would you like to view the first 5 rows of individual trip data? Enter yes or no?").lower()
    if view_data == 'yes': 
        while True:
            print(df.iloc[start_loc: start_loc+5])
            start_loc += 5
            next_data = input("Do you want to see the next 5 rows of data?").lower()
            if next_data != 'yes':
                break
   
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df ,city)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
