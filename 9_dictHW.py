#
def main():
    movie_ratings = {'IT 2' : 8, 'Howls Moving Castle' : 10, 'The Creator' : 4, 'Willy Wonka' : 0,
                    'Aqua Man' : 7, 'Home' : 9, 'Holes' : 6, 'Oppenheimer' : 10, 'Steven Universe' : 6,
                    'Spider Man No Way Home' : 5, 'Toy Story' : 8, 'Scary Movie' : 3, 'Space Jam' : 9}

    movie = input('Enter a movie title: ')

    recommend_movie(movie_ratings, movie)

def recommend_movie(movie_ratings, movie):
    if(movie in movie_ratings and movie_ratings[movie] >= 8):
        print(f'I recommend {movie} - rated {movie_ratings[movie]}/10')
    else:
        print(f'I recommend these movies:')
        for k, v in movie_ratings.items():
            if v >= 8:
                print(f'{k} - rated {v}/10')
                

if __name__ == "__main__":
    main()
