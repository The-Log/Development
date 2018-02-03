package ml.ankurmishra.tasktracker;

/**
 * Created by ankurM on 11/16/17.
 */


/* ------------------------*/
/*    FILE VERSION 4.0     */
/* ------------------------*/

import android.content.Context;
import android.graphics.Bitmap;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.RatingBar;
import android.widget.TextView;

import java.time.Period;
import java.time.temporal.ChronoUnit;
import java.util.Calendar;
import java.util.Date;

public class FragmentTwo extends Fragment {
    private View mRootView;
    private FragmentTwoInterface mCallback;
    private Tracker tracker;
    private EditText taskName, startTime, endTime;
    private Context ctx;
    private SetTime setStartTime, setEndTime;
    private ImageView mImageView;

    public FragmentTwo() {
    }

    public static FragmentTwo newInstance() {
        FragmentTwo fragment = new FragmentTwo();
        return fragment;
    }

    @Override
    public void setUserVisibleHint(boolean isVisibleToUser) {
        super.setUserVisibleHint(isVisibleToUser);

        if (isVisibleToUser) {
            Log.i("setUserVisibleHint", "fragment visibility: true");

            // ATTEMPT TO TELL ACTIVITY THAT THIS FRAGMENT IS ACTIVE, BUT IT WILL FAIL
            // IF onAttach HAS NOT BEEN CALLED YET.
            // - FOR THAT REASON, WE CALL setFragmentTwoActive IN ON ATTACH, if and only if
            // THE FRAGMENT IS ACTIVE
            try {
                mCallback.setFragmentTwoActive();

                Calendar st = setStartTime.getCalendarDate();
                Calendar et = setEndTime.getCalendarDate();
                String duration = diffDates(st, et);
                tracker.setTask(taskName.getText().toString());
                tracker.setDuration(duration);
                tracker.setStartTime(startTime.getText().toString());
                tracker.setEndTime(endTime.getText().toString());
                mCallback.setTracker(tracker);

                tracker = mCallback.getTracker();
                taskName.setText(tracker.getTask());
                startTime.setText(tracker.getStartTime());
                endTime.setText(tracker.getEndTime());
            } catch (Exception e) {
                // errors callback not created yet
            }
        }
        else {
            Log.i("setUserVisibleHint", "fragment visibility: false");
        }

    }

    @Override
    public void onAttach(Context context) {
        super.onAttach(context);
        ctx = context;
        Log.i("onAttach", "onAttach");

        try {
            mCallback = (FragmentTwoInterface) context;
            if (this.getUserVisibleHint()) {
                // NOTIFY ACTIVITY THAT THIS IS THE ACTIVE FRAGMENT
                mCallback.setFragmentTwoActive();

            }

        } catch (ClassCastException e) {
            throw new ClassCastException(context.toString()
                    + " must implement FragmentTwoInterface");
        }
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


    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        mRootView = inflater.inflate(R.layout.fragment_two, container, false);
        taskName = (EditText) mRootView.findViewById(R.id.mname);

        mImageView = (ImageView) mRootView.findViewById(R.id.miv);



        startTime = (EditText) mRootView.findViewById(R.id.start);
        setStartTime = new SetTime(startTime, ctx);

        endTime = (EditText) mRootView.findViewById(R.id.end);
        setEndTime = new SetTime(endTime, ctx);

        tracker = mCallback.getTracker();
        Log.i("onCreateViewF2", tracker.toString());
        taskName.setText(tracker.getTask());
        return mRootView;
    }

    public void passBitmap(Bitmap b){
        mImageView.setImageBitmap(b);
    }

    public void setTracker(Tracker t){
        tracker = t;
        taskName.setText(tracker.getTask());
        taskName.setText(tracker.getTask());
        startTime.setText(tracker.getStartTime());
        endTime.setText(tracker.getEndTime());
    }

    public interface FragmentTwoInterface {
        void setFragmentTwoActive();
        Tracker getTracker();
        void setTracker(Tracker t);
    }
}