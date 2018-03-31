import fresh_tomatoes
import media

clockwork_orange = media.Movie("A Clockwork Orange", "In the future, a sadistic gang leader is imprisoned and volunteers for a conduct-aversion experiment, but it doesn't go as planned.",\
                        "https://upload.wikimedia.org/wikipedia/en/thumb/4/48/Clockwork_orangeA.jpg/220px-Clockwork_orangeA.jpg", \
                        "https://www.youtube.com/watch?v=FI1204n6GZw", "1971")

troy = media.Movie("Troy", "A battle for Troy",\
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b8/Troy2004Poster.jpg/220px-Troy2004Poster.jpg",\
                     "https://www.youtube.com/watch?v=QpikTTSOHXc", "2004")

limitless = media.Movie("Limitless", "A struggling writer tries a new drug and becomes a genious",\
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/17/Limitless_Poster.jpg/220px-Limitless_Poster.jpg",\
                        "https://www.youtube.com/watch?v=SS5SPPwrcT8", "2011")

inception = media.Movie("Inception", "Corporate spys that uses experimental technology to infiltrate the subconscious of their targets",\
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",\
                        "https://www.youtube.com/watch?v=8hP9D6kZseM", "2010")


jumanji_2 = media.Movie("Jumanji 2", "Four students find a multiplayer video game 'jumanji', when they start playing it they get stuck in the game", \
                        "https://upload.wikimedia.org/wikipedia/en/d/dc/Jumanji_Welcome_to_the_Jungle.png", \
                        "https://www.youtube.com/watch?v=eA5WqfKsbZg", "2017")


source_code = media.Movie("Source Code", "U.S. Army pilot gets put in a mission to find a bomber", \
                          "https://upload.wikimedia.org/wikipedia/en/thumb/e/e5/Source_Code_Poster.jpg/220px-Source_Code_Poster.jpg", \
                          "https://www.youtube.com/watch?v=t5roJgHV_lA", "2011")


movies = [clockwork_orange, troy, limitless, inception, jumanji_2, source_code]
fresh_tomatoes.open_movies_page(movies)
