import pandas as pd

data = pd.read_csv('movies_dataset.csv')

# check dataset
# print(data.head())

# check the detail of datset
# detail = data.describe()
# print(detail)

# check the information of dataset
# info = data.info()
# print(info)
print('=== Genre Option ===')
print('Genre Option : ',data['genre'].unique())
genre = data['genre'].dropna().unique()
print('=== Movie recomendation Interface ===')
while True:
    i = 0
    user = input("\nEnter your favourite genre (or 'exit' to quit): ")

    if user.lower() == 'exit':
            print('Good Bye !')
            break
    
    rating = float(input("Enter the minimum rating : "))

    recomended = data[(data['genre'].str.lower() == user.lower()) &  (data['rating'] >= rating)]
    recomended = recomended.sort_values(by='rating', ascending=False)
  
    if len(recomended) == 0:
        print('No movies found.')
    else: 
        print('\n === Movie recomended ===')
        for i, (_, movie) in enumerate(recomended.iterrows(), start=1):
            print(f'\n{i}.{movie['name']}')
            print(f'Rating : {movie['rating']}')
            print(f'Year : {movie['year']}')
        avg_rating = recomended['rating'].mean() 
        print(f'average recomendation ratings:{avg_rating}')
