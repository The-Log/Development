package ml.ankurmishra.tasktracker;

import android.app.TimePickerDialog;
import android.content.Context;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.TimePicker;

import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;

/**
 * Created by ankur on 1/18/18.
 */

class SetTime implements View.OnFocusChangeListener, TimePickerDialog.OnTimeSetListener {

    private EditText editText;
    private Calendar myCalendar;
    private Context ctx;
    public SetTime(EditText editText, Context ctx){
        this.editText = editText;
        this.ctx = ctx;
        this.editText.setOnFocusChangeListener(this);
        this.myCalendar = Calendar.getInstance();

    }

    @Override
    public void onFocusChange(View v, boolean hasFocus) {
        // TODO Auto-generated method stub
        if(hasFocus){
            int hour = myCalendar.get(Calendar.HOUR_OF_DAY);
            int minute = myCalendar.get(Calendar.MINUTE);
            new TimePickerDialog(ctx, this, hour, minute, true).show();
        }
    }

    @Override
    public void onTimeSet(TimePicker view, int hourOfDay, int min) {
        String minute = "" + min;
        Date d = myCalendar.getTime();
        d.setHours(hourOfDay);
        d.setMinutes(min);
        myCalendar.setTime(d);
        if (min < 10){
            minute = "0" + min;
        }
        String time = hourOfDay + ":" + minute + " AM";
        if (hourOfDay > 12){
            hourOfDay = hourOfDay - 12;
            time = hourOfDay + ":" + minute + " PM";
        }
        if (hourOfDay == 12){
            time = hourOfDay + ":" + minute + " PM";
        }
        if(hourOfDay == 0){
            time = 12 +":" + minute + " AM";
        }
        Log.i("Tag", "onTimeSet: " + time);
        this.editText.setText(time);
    }
    public Calendar getCalendarDate(){
        System.out.println("Date: " + myCalendar.getTime());
        return myCalendar;
    }

}