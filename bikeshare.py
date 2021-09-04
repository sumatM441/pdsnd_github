import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

CITIES = ['chicago', 'new york', 'washington']
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June']
CITY_VAL = '0'
#print("CITY_VAL--------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<",CITY_VAL)


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
        city = input('Would you like to see data for Chicago, New York, or Washington?').lower()
        CITY_VAL = city
        print("----------------------------CITY_VAL --------------------------",city)
        if city in CITIES:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Which month? January, February, March, April, May,June,or all months?').title()
        if month in MONTHS:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = int(input('Which day? Please type your response as an integer  (e.g., 1=Sunday).'))
        if day in [1,2,3,4,5,6,7]:
            break
    
    if day == 1:
       day = 'Saturday'
    if day == 2:
       day = 'Sunday'
    if day == 3:
       day = 'Monday'
    if day == 4:
       day = 'Tuesday'
    if day == 5:
       day = 'Wednesday'
    if day == 6:
       day = 'Thursday'
    if day == 7:
       day = 'Friday'
    # to check that if statement works correctly        
    #print("day is ============",day)
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        #months = ['january', 'february', 'march', 'april', 'may', 'june']
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].value_counts().idxmax()
    print('The most common month is: ', most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].value_counts().idxmax()
    print('The most common day of week is: ', most_common_day)
    

    # TO DO: display the most common start hour
    most_common_start_hour = df['hour'].value_counts().idxmax()
    print('The most common start hour is: ', most_common_start_hour)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print("The most commonly used start station: ", most_common_start_station)
    

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print("The most commonly used end station :", most_common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most commonly used start station and end station : {}, {}"\
            .format(most_common_start_end_station[0], most_common_start_end_station[1]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time: ',total_travel_time )

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time: ',mean_travel_time )


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, CITY_VAL):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Counts of user types:\n")
    user_counts = df['User Type'].value_counts()
    print(user_counts)
    
    # in case the user choose the cities that have a gender and a birthday
    if CITY_VAL in ['chicago', 'new york']:
        # TO DO: Display counts of gender
        print("Counts of gender:\n")
        gender_counts = df['Gender'].value_counts()
        print(gender_counts)


        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_bth_year = df['Birth Year'].min()
        print(' The earliest year of birth is:\n', earliest_bth_year)
    
        most_recent_bth_year = df['Birth Year'].max()
        print(' The most recent year of birth is:\n', most_recent_bth_year)
    
        most_common_bth_year = df['Birth Year'].idxmax()
        print(' The most common year of birth is:\n', most_common_bth_year)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while (view_data != 'no'):
        #print(df.iloc[0:start_loc]) 
        #print(df.iloc[start_loc, start_loc+5]) 
        print(df.head(start_loc))
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        #print(df)
        display_data(df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
