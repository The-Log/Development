package com.example.ankur.assignment9;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by ankurM on 10/5/17.
 */

public class SlideShow {
    private String objectName;
    private List<String> images;
    private int index;

    public SlideShow () {
        objectName = "imageNames";
        images = new ArrayList<String>();
        index = 0;
    }
    public SlideShow (String n, List<String> l, int i) {
        objectName = n;
        images = l;
        index = i;
    }

    public String getObjectName() {
        return objectName;
    }

    public void setObjectName(String name) {
        this.objectName = name;
    }

    public int getIndex () {
        return index;
    }


    public List<String> getImages() {
        return images;
    }

    public void setImages(List<String> images) {
        this.images = images;
    }

    public void setIndex(int index) {
        this.index = index;
    }

    @Override
    public String toString() {
        return "{ssName: " + objectName + ",imageNames: " + images + ",index: " + index + "}";
    }
    public String ssNames(){
        String s = "";
        for (int i = 0; i < images.size(); i++) {
            s += images.get(i);
            if (i < images.size() - 1){
                s += ",";
            }
        }
        return s;
    }
}