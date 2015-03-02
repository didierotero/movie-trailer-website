import fresh_tomatoes
import media

black_swan = media.Movie("Black Swan",
                         "A psychological thriller set in the world of New York City ballet, BLACK SWAN stars Natalie Portman as Nina, a featured dancer who finds herself locked in a web of competitive intrigue with a new rival at the company (Mila Kunis). A Fox Searchlight Pictures release by visionary director Darren Aronofsky (THE WRESTLER), BLACK SWAN takes a thrilling and at times terrifying journey through the psyche of a young ballerina whose starring role as the duplicitous swan queen turns out to be a part for which she becomes frighteningly perfect.",
                         "https://upload.wikimedia.org/wikipedia/en/thumb/6/68/Black_Swan_poster.jpg/225px-Black_Swan_poster.jpg",
                         "https://www.youtube.com/watch?v=5jaI1XOB-bs")

devil_wears_prada = media.Movie("The Devil Wears Prada",
                                "Andrea 'Andy' Sachs (Anne Hathaway) is an aspiring journalist fresh out of Northwestern University. Despite her ridicule for the shallowness of the fashion industry, she lands a job 'a million girls would kill for,' junior personal assistant to Miranda Priestly (Meryl Streep), the icy editor-in-chief of Runway fashion magazine. Andy plans to put up with Miranda's bizarre and humiliating treatment for one year in hopes of getting a job as a reporter or writer somewhere else.",
                                "https://upload.wikimedia.org/wikipedia/en/thumb/1/18/The_Devil_Wears_Prada_cover.jpg/220px-The_Devil_Wears_Prada_cover.jpg",
                                "https://www.youtube.com/watch?v=XTDSwAxlNhc")

little_miss_sunshine = media.Movie("Little Miss Sunshine",
                                   "When Olive learns she has qualified for the 'Little Miss Sunshine' beauty contest that is being held in Redondo Beach, California in two days, she is ecstatic. However, money is tight and due to various logistical issues, the only way to make the trip is if the entire household goes. Despite Richard, Dwayne, and Frank not wanting to go, they all band together to support Olive and embark upon the 800-mile road trip in their antiquated yellow Volkswagen T2 Microbus.",
                                   "https://upload.wikimedia.org/wikipedia/en/thumb/1/16/Little_miss_sunshine_poster.jpg/220px-Little_miss_sunshine_poster.jpg",
                                   "https://www.youtube.com/watch?v=wvwVkllXT80")

lawrence_of_arabia = media.Movie("Lawrence of Arabia",
                                 "A british officer's journey to the middle east",
                                 "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Lawrence_of_arabia_ver3_xxlg.jpg/220px-Lawrence_of_arabia_ver3_xxlg.jpg",
                                 "https://www.youtube.com/watch?v=zmr1iSG3RTA")

truman_show = media.Movie("The Truman Show",
                          "The Truman Show is a 1998 American satirical comedy-drama film directed by Peter Weir and written by Andrew Niccol. The cast includes Jim Carrey as Truman Burbank, as well as Laura Linney, Noah Emmerich, Ed Harris and Natascha McElhone. The film chronicles the life of a man who is initially unaware that he is living in a constructed reality television show, broadcast 24-hours-a-day to billions of people across the globe. Truman becomes suspicious of his perceived reality and embarks on a quest to discover the truth about his life.",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/c/cd/Trumanshow.jpg/220px-Trumanshow.jpg",
                          "https://www.youtube.com/watch?v=c3gI9ms8Fdc")

kill_bill = media.Movie("Kill Bill",
                        "The Bride wakens from a four-year coma. The child she carried in her womb is gone. Now she must wreak vengeance on the team of assassins who betrayed her - a team she was once part of.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/c/cf/Kill_bill_vol_one_ver.jpg/220px-Kill_bill_vol_one_ver.jpg",
                        "https://www.youtube.com/watch?v=7kSuas6mRpk")

matrix = media.Movie("The Matrix",
                     "Thomas Anderson is Neo is a young software engineer and part-time hacker who is singled out by some mysterious figures who want to introduce him into the secret of 'the matrix'. The cops also seem to be after him, and he takes a chance on discovering what he has always suspected: that the world is not quite what it seems to be and a sinister conspiracy is at work.",
                     "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")

magic_hour = media.Movie("The Magic Hour",
                         "According to photography experts, 'the golden hour, sometimes called the 'magic hour', is roughly the first hour of light after sunrise, and the last hour of light before sunset, although the exact duration varies between seasons. During these times the sun is low in the sky, producing a soft, diffused light which is much more flattering than the harsh midday sun.'",
                         "https://upload.wikimedia.org/wikipedia/en/thumb/6/63/The_Magic_Hour.png/220px-The_Magic_Hour.png",
                         "https://www.youtube.com/watch?v=ov69jI6mZT4")

movies = [black_swan, devil_wears_prada, little_miss_sunshine, lawrence_of_arabia, truman_show, kill_bill, matrix, magic_hour]
fresh_tomatoes.open_movies_page(movies)
