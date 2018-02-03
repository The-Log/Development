package ml.ankurmishra.tasktracker;

import android.app.Activity;
import android.app.DialogFragment;
import android.content.Context;
import android.content.DialogInterface;
import android.os.Bundle;
import android.util.DisplayMetrics;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import java.util.Calendar;
import java.util.Date;

import javax.xml.datatype.Duration;

import static android.view.ViewGroup.LayoutParams.WRAP_CONTENT;
/**
 * Created by ankur on 1/22/18.
 */

public class DFrag extends DialogFragment {

    private final String LOG_TAG = DFrag.class.getSimpleName();
    private EditText taskName, startTime, endTime;
    private DFragInterface mCallback;
    private Tracker tracker;
    private Context ctx;

    // onCreate --> (onCreateDialog) --> onCreateView --> onActivityCreated
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        Log.v(LOG_TAG, "onCreateView");

        View dialogView = inflater.inflate(R.layout.dialog_content, container, false);

        taskName = (EditText) dialogView.findViewById(R.id.mname);

        startTime = (EditText) dialogView.findViewById(R.id.start);
        final SetTime setStartTime = new SetTime(startTime, ctx);

        endTime = (EditText) dialogView.findViewById(R.id.end);
        final SetTime setEndTime = new SetTime(endTime, ctx);
        // "Got it" button
        Button buttonPos = (Button) dialogView.findViewById(R.id.pos_button);
        buttonPos.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Calendar st = setStartTime.getCalendarDate();
                Calendar et = setEndTime.getCalendarDate();
                String duration = diffDates(st, et);
                tracker = new Tracker();
                tracker.setTask(taskName.getText().toString());
                tracker.setDuration(duration);

                tracker.setStartTime(startTime.getText().toString());
                tracker.setEndTime(endTime.getText().toString());

                System.out.println("Duration: " + duration);
                System.out.println("Tracker: " + tracker.toString());

                showToast(tracker.toString());
                dismiss();
            }
        });


        // "Cancel" button
        Button buttonNeg = (Button) dialogView.findViewById(R.id.neg_button);
        buttonNeg.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                showToast("neg_button");
                // If shown as dialog, cancel the dialog (cancel --> dismiss)
                if (getShowsDialog())
                    getDialog().cancel();
                    // If shown as Fragment, dismiss the DialogFragment (remove it from view)
                else
                    dismiss();
            }
        });

        return dialogView;
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
        System.out.println(diffMinutes/60 + ":" +diffMinutes%60);
        String hour = "" + (diffMinutes / 60);
        String minutes = "" +(diffMinutes % 60);
        if(diffMinutes % 60 < 10){
            minutes = 0 + minutes;
        }
        return  hour + ":" + minutes;
    }

    @Override
    public void onAttach(Context context) {
        super.onAttach(context);
        ctx = context;
        try {
            mCallback = (DFrag.DFragInterface) context;
            if (this.getUserVisibleHint()) {
                // NOTIFY ACTIVITY THAT THIS IS THE ACTIVE FRAGMENT
            }

        } catch (ClassCastException e) {
            throw new ClassCastException(context.toString() + " must implement FragmentOneInterface");
        }
        Log.i("onAttach", "onAttach");
    }

    // If shown as dialog, set the width of the dialog window
    // onCreateView --> onActivityCreated -->  onViewStateRestored --> onStart --> onResume
    @Override
    public void onResume() {
        super.onResume();
        Log.v(LOG_TAG, "onResume");
        if (getShowsDialog()) {
            // Set the width of the dialog to the width of the screen in portrait mode
            DisplayMetrics metrics = getActivity().getResources().getDisplayMetrics();
            int dialogWidth = Math.min(metrics.widthPixels, metrics.heightPixels);
            getDialog().getWindow().setLayout(dialogWidth, WRAP_CONTENT);
        }
    }


    private void showToast(String buttonName) {
        Toast.makeText(getActivity(), "Clicked on \"" + buttonName + "\"", Toast.LENGTH_SHORT).show();
    }

    // If dialog is cancelled: onCancel --> onDismiss
    @Override
    public void onCancel(DialogInterface dialog) {
        Log.v(LOG_TAG, "onCancel");
    }

    // If dialog is cancelled: onCancel --> onDismiss
    // If dialog is dismissed: onDismiss
    @Override
    public void onDismiss(DialogInterface dialog) {
        mCallback.addTracker(tracker);
    }
    public interface DFragInterface {
        void addTracker(Tracker tracker);
    }
}
