import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():

    print('Hello! Let\'s explore some US bikeshare data!')
    
    # getting user input for city (chicago, new york city, washington)
    
    while True:
        city = input("Please choose a city from  'chicago', 'new york city' or 'washington' : ").lower()
        if city.lower() in CITY_DATA:
            break
        else:
            print("Please select a city from the list \n")
            
    # getting user input for month 
    
    months= ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month= input("Please choose a month from  'january', 'february', 'march', 'april', 'may', 'june', 'all' : ")
        if month.lower() in months:
            break
        else:    
            print("Please select a month from the list \n")

    # getting user input for day of week 
    
    days= ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while True:
        day= input("Please choose a day from  'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all': ")
        if day.lower() in days:
            break
        else:    
            print("Please select a day from the list \n")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):

    # loading data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # converting the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extracting month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filtering by month if applicable
    if month.lower() != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month.lower()) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filtering by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print("\nCalculating The Most Frequent Times of Travel...\n")
    start_time = time.time()

    # displaying the most common month
    
    common_month= df['month'].mode()[0]
    print("The most common month is: " ,common_month)

    # displaying the most common day of week
    
    common_day= df['day_of_week'].mode()[0]
    print("The most common day is: " ,common_day)

    # displaying the most common start hour
    
    common_hour= df['hour'].mode()[0]
    print("The most common start hour is: " ,common_hour)

    print("\nThis took %s seconds." % round((time.time() - start_time),3))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()

    # displaying most commonly used start station
    
    common_start_station= df['Start Station'].mode()[0]
    print("The most common start station is: " ,common_start_station)

    # displaying most commonly used end station
    
    common_end_station= df['End Station'].mode()[0]
    print("The most common end station is: " ,common_end_station)

    # displaying most frequent combination of start station and end station trip
   
    common_start_end = (df['Start Station'] + '--->' + df['End Station']).mode()[0]
    print("The most common combination of start station and end station is: " , common_start_end.split('--->'))

    
    print("\nThis took %s seconds." % round((time.time() - start_time),3))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # displaying total travel time
    
    total_travel_time= round(df['Trip Duration'].sum(),1)
    print("Total travel Time is: {} seconds " .format(total_travel_time))

    # displaying mean travel time
    mean_travel_time= round(df['Trip Duration'].mean(),1)
    print("Mean travel Time is: {} seconds ".format(mean_travel_time))

    print("\nThis took %s seconds." % round((time.time() - start_time),3))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Displaying counts of user types
    print("User Types counts are: ")
    counts_of_users= df['User Type'].value_counts()
    print(counts_of_users)

    # Displaying counts of gender
    
    try:
        counts_of_gender = df['Gender'].value_counts()
        print("Gender counts are:")
        print(counts_of_gender)
    except:
        print("Gender column not found")
    
    # Displaying earliest, most recent, and most common year of birth
    
    try:
        earliest_birth_year = df['Birth Year'].min()
        print("The earliest birth year is: " ,int(earliest_birth_year))
    
        recent_birth_year = df['Birth Year'].max()
        print("The most recent birth year is: " ,int(recent_birth_year))
    
        common_birth_year = df['Birth Year'].mode()[0]
        print("The most common birth year is: " ,int(common_birth_year))
    except:
        print("Birth year column not found")
    
    
    print("\nThis took %s seconds." % round((time.time() - start_time),3))
    print('-'*40)

    
    
def display_raw_data(df):
    print("Raw data is here")
    i = 0
    raw = input("Do you want to show 5 rows of it ? ('yes','no')").lower()
    pd.set_option('display.max_columns',200)
    while True:
        if raw=='no':
            break
        elif raw =='yes':
            print(df.iloc[i:i+5])
            i += 5
            raw = input("5 more rows of raw data ? ('yes','no')").lower()
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()

    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        while True:
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() == 'yes':
                break
            elif restart.lower() == 'no':
                return
            else:
                print("\nYour input is invalid. Please enter only 'yes' or 'no'\n")
            
            



if __name__ == "__main__":
	main()
