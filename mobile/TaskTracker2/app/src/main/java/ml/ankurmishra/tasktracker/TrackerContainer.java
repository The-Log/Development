package ml.ankurmishra.tasktracker;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by ankurM on 11/14/17.
 */

public class TrackerContainer {
    private List<Tracker> trackerList;

    public TrackerContainer(ArrayList arrayList){
        trackerList =arrayList;
    }
    public List<Tracker> getList(){
        return trackerList;
    }
    public void add(Tracker m){
        trackerList.add(m);
    }
    public Tracker get(int i){
        return trackerList.get(i);
    }
    public int size(){
        return trackerList.size();
    }
    public String toString() {
        String s = "{\"trackerList\" : [";
        for (int i = 0; i < trackerList.size(); i++) {
            s += trackerList.get(i).toString();
            if (i + 1 < trackerList.size())
                s += ", \n";
        }
        s +=  "]}";
        return s;
    }
}
