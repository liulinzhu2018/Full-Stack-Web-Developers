import media
import fresh_tomatoes

paddington = media.Movie(
                        "Paddington 2",
                        "Paddington, now happily settled with the Brown family in Windsor Gardens, has become a popular member of the community, spreading joy and marmalade wherever he goes.",
                        "https://gss1.bdstatic.com/-vo3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike180%2C5%2C5%2C180%2C60/sign=8400dbb7bb51f819e5280b18bbdd2188/f603918fa0ec08faec2f4e3b52ee3d6d55fbda7b.jpg",
                        "https://www.youtube.com/watch?v=7QTRrCIQn_Q&list=PLHPTxTxtC0iZEKQEv9bTwCuQoRJWDOtPQ")

titanic = media.Movie(
                        "Titanic",
                        "Titanicis a 1997 American epic romantic disaster film directed, written, co-produced, and co-edited by James Cameron. It is a fictionalized account of the sinking of the RMS Titanic. Its stars Leonardo DiCaprio and Kate Winslet as members of different social classes who fall in love aboard the ship during its ill-fated maiden voyage.",
                        "https://gss0.bdstatic.com/-4o3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike92%2C5%2C5%2C92%2C30/sign=8d2708eddd2a6059461de948495d5ffe/4034970a304e251f49e200dcad86c9177f3e53f9.jpg",
                        "https://www.youtube.com/watch?v=jIhicnTgArM")

tt = media.Movie(
                "21(2008)",
                "Academy Award Winner Kevin Spacey (The Usual Suspects) and young Hollywood super star Kate Boswoth (Superman Returns) star in this clever & adreniline filled heist film.",
                "https://gss2.bdstatic.com/-fo3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike80%2C5%2C5%2C80%2C26/sign=78d19381ac773912d02b8d339970ed7d/d1a20cf431adcbeff8dbab3aa9af2edda3cc9f1b.jpg",
                "https://www.youtube.com/watch?v=JWZvmcYuZLs")

movies = [paddington, tt, titanic]
fresh_tomatoes.open_movies_page(movies)

print media.Movie.VAILD_RATINGS
print media.Movie.__doc__
print media.Movie.__name__
print media.Movie.__module__
