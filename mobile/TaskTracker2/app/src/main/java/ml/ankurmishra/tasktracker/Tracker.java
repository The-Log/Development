package ml.ankurmishra.tasktracker;

import android.util.Log;

import java.util.Calendar;
import java.util.Date;

/**
 * Created by ankurM on 11/9/17.
 */

public class Tracker {
    private String task, duration, startTime, endTime;

    public Tracker() {
    }

    public Tracker(String task, String duration, String startTime, String endTime) {
        this.task = task;
        this.duration = duration;
        this.startTime = startTime;
        this.endTime = endTime;
    }

    public String getTask() {
        return task;
    }

    public void setTask(String name) {
        this.task = name;
    }

    public void setDuration(String duration) {
        this.duration = duration;
    }

    public String getDuration() {
        return duration;
    }

    @Override
    public String toString() {
        return "{" +
                "task:\'" + task + '\'' +
                ", duration:\'" + duration + "\'" +
                ", startTime:\'" + startTime + "\'" +
                ", endTime:\'" + endTime + "\'" +
                '}';
    }

    public String diffDates(Calendar startTime, Calendar endtime){
        if (endtime.before(startTime)){
            Date d = endtime.getTime();
            d.setDate(d.getDate() + 1);
            endtime.setTime(d);
            Log.i("Before", startTime.getTime().getDate() + "\t" + d.getDate());
        }
        // Get the represented date in milliseconds
        long millis1 = startTime.getTimeInMillis();
        long millis2 = endtime.getTimeInMillis();

        // Calculate difference in milliseconds
        long diff = millis2 - millis1;

        // Calculate difference in seconds
        long diffSeconds = diff / 1000;

        // Calculate difference in minutes
        long diffMinutes = diff / (60 * 1000);

        // Calculate difference in hours
        long diffHours = diff / (60 * 60 * 1000);

        // Calculate difference in days
        long diffDays = diff / (24 * 60 * 60 * 1000);

        return diffMinutes / 60 + ": " + diffMinutes % 60;
    }

    public String getStartTime() {
        return startTime;
    }

    public void setStartTime(String startTime) {
        this.startTime = startTime;
    }

    public String getEndTime() {
        return endTime;
    }

    public void setEndTime(String endTime) {
        this.endTime = endTime;
    }
}