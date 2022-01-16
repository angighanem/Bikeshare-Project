import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = " "
    while True:
        city = input('Which city would you like to explore ? Please choose Chicago, New York City or Washington.\n').lower()
        if city in CITY_DATA.keys():
            break
        else:
            print('Wrong input. Please choose one of the three cities. \n')
            question = input('Would you like to start over? (yes/no) \n')
            if question == 'yes':
                city = input('Okay then. Which city would you like to explore ? Please choose Chicago, New York City or Washington.\n').lower()
                break
            elif question == 'no':
                print('No problem.')
                break
            else:
                print('Wrong Entry. Please answer by yes or no.')
                question = input('Would you like to start over? (yes/no) \n').lower()
                city = input('Okay then. Which city would you like to explore ? Please choose Chicago, New York City or Washington.\n').lower()
                break
            break


    # get user input for month (all, january, february, ... , june)
    months = [ 'all', 'january', 'february', 'march', 'april', 'may', 'june']
    while True:
        answer = input('Would you like to explore a specific month? (yes/no).\n').lower()
        if answer == 'yes':
            month = input('Please choose a month from the following: January, February, March, April, May, June. \n').lower()
            if month in months:
                print('Thank you for your choice. You chose {}'.format(month.title()))
                break
            else:
                print('Please check your entry. Something is not right.')
                question = input('Would you like to start over? (yes/no) \n').lower()
                if question == 'yes':
                    print('\n Okay then.\n')
                    continue
                else:
                    print('No problem.')
                    break
        elif answer == 'no':
            print('You chose not to filter months; ALL months are included.')
            month = months[0]
            break
        else:
            print('Please check your entry. Something is not right.')
            question = input('Would you like to start over? (yes/no) \n').lower()
            if question == 'yes':
                print('Okay then.\n')
                continue
            else:
                print('No problem.')
                break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = [ 'all', 'monday', 'tuesday', 'wednseday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:
        answer = input('Would you like to explore a specific day? (yes/no).\n').lower()
        if answer == 'yes':
            day = input('Please choose a day from the following: Monday, Tuesday, Wednsday, Thursday, Friday, Saturday, Sunday. \n').lower()
            if day in days:
                print('Thank you for your choice. You chose {}'.format(day.title()))
                break
            else:
                print('Please check your entry. Something is not right.')
                question = input('Would you like to start over? (yes/no) \n').lower()
                if question == 'yes':
                    print('\n Okay then.\n')
                    continue
                else:
                    print('No problem.')
                    break
        elif answer == 'no':
            print('You chose not to filter days; ALL days are included.')
            day = days[0]
            break
        else:
            print('Please check your entry. Something is not right.')
            question = input('Would you like to start over? (yes/no) \n').lower()
            if question == 'yes':
                print('Okay then.\n')
                continue
            else:
                print('No problem.')
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1

        # filter by month to create the new dataframe
        df = df[df['month']== month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day.title()]

    return df

def filered_data_info(df):
    """Check the shape and Check the number of missing data in the selected data"""
    print('The shape of the selected data is {}.'.format(df.shape))
    missing_values_nb = df.isna().sum()
    print('The number of missing values in the filtered data by column is: {}'.format(missing_values_nb))

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if len(pd.unique(df['month'])) != 1 :
        popular_month = df['month'].mode()[0]
        print('Most Common Month:', popular_month)
        print('Here is a descriptive histogram of the frequency of bikeshare use from January to June.')
        df['month'].hist()
        plt.xlabel('Month')
        plt.ylabel('Frequency')
        plt.show()
    else:
        print('You chose to filter the data based on month, therefore your only available and most popular month is: ',df['month'].mode()[0])


    # display the most common day of week
    if len(pd.unique(df['day_of_week'])) != 1 :
        popular_day = df['day_of_week'].mode()[0]
        print('Most Common Day of the Week:', popular_day)
        print('Here is a descriptive histogram of the frequency of bikeshare use throughout the week.')
        df['day_of_week'].hist()
        plt.xlabel('Day of the Week')
        plt.ylabel('Frequency')
        plt.show()
    else:
        print('You chose to filter the data based on day of the week, therefore your only available and most popular day is: ',df['day_of_week'].mode()[0])


    # display the most common start hour
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % round(time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("The most popular start station from the data you chose is: " + popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("The most popular end station from the data you chose is: " + popular_end_station)

    # display most frequent combination of start station and end station trip
    combination = (df['Start Station'] + " --- " + df['End Station']).mode()[0]
    print("The most frequent combination of start station and end station trip is : " + str(combination.split(" --- ")))

    print("\nThis took %s seconds." % round(time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time in your chosen data is: {} hours'.format(round(total_travel_time/3600)))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time in your chosen data is: {} minutes'.format(round(mean_travel_time/60)))

    print("\nThis took %s seconds." % round(time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    users_types_count = df['User Type'].value_counts()
    print('The count of users by type in your chosen data is: {}'.format(users_types_count))

    # Display counts of gender
    if 'Gender' in df.columns:
        users_gender_count = df['Gender'].value_counts()
        print('The count of users by gender in your chosen data is: {}'.format(users_gender_count))
        print("Here is a descriptive histogram of the user's gender.")
        df['Gender'].hist()
        plt.xlabel('Gender')
        plt.ylabel('Frequency')
        plt.show()
    else:
        print("The city you chose does not provide info on the user's gender.")

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()[0]
        print('In your chosen data, the earliest year of birth is {} while the most recent recent year of birth is {}. The most common year of birth is {}.'.
        format(int(earliest_year),int(most_recent_year),int(most_common_year)))
        print("Here is a descriptive histogram of the user's year of birth.")
        df['Birth Year'].hist()
        plt.xlabel('Birth Year')
        plt.ylabel('Frequency')
        plt.show()
    else:
        print("The city you chose does not provide info on the user's birth year.")

    print("\nThis took %s seconds." % round(time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """When user confirms that he wants to see raw data, the first five rows are displayed.
        Fove more rows are displayed at each request.

    Args:
        df is the input needed i.e. a dataframe to extract the rows from.
    """
    row_num = 0
    answer = input('Would you like to see some raw data? (yes/no)\n').lower()
    while True:
        if answer == 'yes':
            pd.set_option('display.max_columns',200)
            print(df.iloc[row_num:row_num+5])
            cont = input('Would you like to see more data? (yes/no) \n').lower()
            row_num += 5
            if cont == 'yes':
                continue
            elif cont == 'no':
                print('Ok then. Thank you.')
                break
            else:
                print('Please check your entry. Possible answer is yes or no.')
                answer = input('Would you like to see some raw data? (yes/no) \n').lower()
                continue
        elif answer == 'no':
            print('Ok then. Thank you for your choice.')
            break
        else:
            print('Please check your entry. Possible answer is yes or no.')
            answer = input('Would you like to see some raw data? (yes/no) \n').lower()
            if answer == 'yes':
                print('Okay then.\n')
                continue
            else:
                print('No problem.')
                break
        print("\nThis took %s seconds." % round(time.time() - start_time))
        print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print("\n Let's first check the shape and the total number of missing values in the chosen dataset.\n")
        filered_data_info(df)
        print('\n The following is some statistics on time, stations, trips and users.\n')
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        print('\nBefore you leave,')
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart.lower() == 'no':
            break
        if restart.lower() =='yes':
            continue
        else:
            print('Please check your entry. Answer can be yes or no. \n')
            restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
            continue


if __name__ == "__main__":
	main()
