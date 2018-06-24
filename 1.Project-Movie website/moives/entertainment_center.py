import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his torys that come to life",
                        "https://movie.douban.com/photos/photo/2296481800/#title-anchor",
                        "http://www.youtube.com/xx")
#print toy_story.storyline
#toy_story.show_trailer()



kung_fu_panda = media.Movie("Kung Fu Panda",
                        "A story of Kung Fu Panda",
                        "https://movie.douban.com/photos/photo/2296481800/#title-anchor",
                        "http://www.iqiyi.com/v_19rrluo3zo.html")
#kung_fu_panda.show_trailer()

#movies = [toy_story, kung_fu_panda]
#fresh_tomatoes.open_movies_page(movies)

print media.Movie.VAILD_RATINGS
print media.Movie.__doc__
print media.Movie.__name__
print media.Movie.__module__
