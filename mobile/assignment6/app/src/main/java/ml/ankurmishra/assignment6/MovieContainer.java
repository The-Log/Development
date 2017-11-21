package ml.ankurmishra.assignment6;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by ankurM on 11/14/17.
 */

public class MovieContainer {
    private List<Movie> movieList;

    public MovieContainer(ArrayList arrayList){
        movieList=arrayList;
    }
    public List<Movie> getList(){
        return movieList;
    }
    public void add(Movie m){
        movieList.add(m);
    }
    public Movie get(int i){
        return movieList.get(i);
    }
    public int size(){
        return movieList.size();
    }
}
