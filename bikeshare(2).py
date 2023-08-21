import time
import pandas as pd
import numpy as np

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

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

    while True:
        city = input("\nSelect the name of the city to view the data: Chicago, New York City, or Washington?\n").lower()
        if city not in CITY_DATA:
            print("Sorry, this is an invalid city name. Please try again.")
            continue
        else:
            break
        
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("\nSelect a month: January, February, March, April, May, June, or type 'all' if you have no preference?\n").lower()
        if month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            print("Sorry, this is an invalid month name. Please try again.")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    while True:
        day = input("\nSelect a day: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or type 'all' if you have no preference.\n").lower()
        if day not in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']:
            print("Sorry, this is an invalid day name. Please try again.")
            continue
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
    
    # load data file from text file into a dataframe
    file_name = CITY_DATA[city]
    df = pd.read_csv(file_name)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # create a new column by extracting the months and days from Start Time 
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month
    if month != 'all':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        if month.title() not in months:  
            print("Sorry, this is an invalid month name. Please try again.")
            return None  # Return or handle the invalid input
        month = months.index(month.title()) + 1
        df = df[df['month'] == month]

    # filter by day of week
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    print('The most common month is:', months[popular_month - 1])

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('The most common day: ', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most common start hour is: ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Start_Station = df['Start Station'].value_counts().idxmax()
    print('The most commonly used start station is: ', Start_Station)


    # TO DO: display most commonly used end station
    End_Station = df['End Station'].value_counts().idxmax()
    print('\nThe most commonly used end station:', End_Station)


    # TO DO: display most frequent combination of start station and end station trip
    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('\nThe most commonly used combination of start station and end station trip:', Start_Station, " & ", End_Station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_Travel_Time = df['Trip Duration'].sum()
    print('The Total travel time is', Total_Travel_Time/86400, " Days")

    # TO DO: display mean travel time
    Mean_Travel_Time = df['Trip Duration'].mean()
    print('The Mean travel time is', Mean_Travel_Time/60, " Minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

 # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types:\n', user_types)

    # TO DO: Display counts of gender
    try:
      gender_types = df['Gender'].value_counts()
      print('\nThe gender types is\n', gender_types)
    except KeyError:
      print("\nGender Types:\nThere is no data available for this month.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
      Earliest_Year = df['Birth Year'].min()
      print('\nThe most earliest year is:', Earliest_Year)
    except KeyError:
      print("\nEarliest Year:\nThere is no data available for this month.")

    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('\nThe most recent year is:', Most_Recent_Year)
    except KeyError:
      print("\nMost Recent Year:\nThere is no data available for this month.")

    try:
      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print('\nThe most common year is:', int(Most_Common_Year))
    except KeyError:
      print("\nMost Common Year:\nThere is no data available for this month.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        # Display raw data upon user request
        show_raw_data = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n')
        start_idx = 0
        while show_raw_data.lower() == 'yes':
            print(df.iloc[start_idx:start_idx+5])
            start_idx += 5
            show_raw_data = input('\nWould you like to see more 5 lines of raw data? Enter yes or no.\n')

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
