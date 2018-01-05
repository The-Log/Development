package com.example.ankur.assignment9;

import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

/**
 * Created by ankurM on 11/18/17.
 */

public class SlideShowContainer {
    private List<SlideShow> slideShowList;

    public SlideShowContainer(List l){
        slideShowList=l;
    }
    public List<SlideShow> getList(){
        return slideShowList;
    }
    public void add(SlideShow m){
        slideShowList.add(m);
    }
    public SlideShow get(int i){
        return slideShowList.get(i);
    }
    public int size(){
        return slideShowList.size();
    }
    @Override
    public String toString() {
        String s = "{\"slideShowList\" : [";
        for (int i = 0; i < slideShowList.size(); i++) {
            s += slideShowList.get(i).toString();
            if (i + 1 < slideShowList.size())
                s += ", \n";
        }
        s +=  "]}";
        return s;
    }
}
