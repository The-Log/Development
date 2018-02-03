package ml.ankurmishra.assignment9;

/**
 * Created by ankurM on 11/9/17.
 */

public class Movie {
    private String title, genre, year;
    private float rating;

    public Movie() {
    }

    public Movie(String title, String genre, String year, int rating) {
        this.title = title;
        this.genre = genre;
        this.year = year;
        this.rating = rating;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String name) {
        this.title = name;
    }

    public String getYear() {
        return year;
    }

    public void setYear(String year) {
        this.year = year;
    }

    public String getGenre() {
        return genre;
    }

    public void setGenre(String genre) {
        this.genre = genre;
    }

    public void setRating(float rating) {
        this.rating = rating;
    }

    public float getRating() {
        return rating;
    }

    @Override
    public String toString() {
        return "{" +
                "title:'" + title + '\'' +
                ", genre:'" + genre + '\'' +
                ", year:'" + year + '\'' +
                ", rating:" + rating +
                '}';
    }
}