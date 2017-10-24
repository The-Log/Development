package ml.ankurmishra.assignment3;

import android.graphics.Color;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.SeekBar;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity implements View.OnClickListener, SeekBar.OnSeekBarChangeListener {
    private Button bttnUpdate;
    private TextView tvhello;
    private SeekBar sb1;
    private EditText et1;
    private int j = 0;
    private String[] array = {"blue","red","green","black"};

    public static final String TAG = "default";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main4);

        et1 = (EditText) findViewById(R.id.et1);
        tvhello = (TextView) findViewById(R.id.tvhello);
        sb1 = (SeekBar) findViewById(R.id.sb1);
        bttnUpdate = (Button) findViewById(R.id.bttnUpdate);

        bttnUpdate.setOnClickListener(this);
        sb1.setOnSeekBarChangeListener(this);
        tvhello.setOnClickListener(this);
    }
    @Override
    public void onClick(View v) {
        switch (v.getId()) {
            case R.id.bttnUpdate :
                String result = et1.getText().toString();
                tvhello.setText("Hello " + result);
                break;
            case R.id.tvhello:
                j++;
                Log.i("tvhello", "i got heres " + array[j%4]);
                tvhello.setBackgroundColor(Color.parseColor(array[j%4]));
                break;
        }

    }
    @Override
    public void onProgressChanged(SeekBar seekBar, int i, boolean b) {
        tvhello.setTextSize(i);
    }

    @Override
    public void onStartTrackingTouch(SeekBar seekBar) {

    }

    @Override
    public void onStopTrackingTouch(SeekBar seekBar) {

    }
}








//        tvcharles = (TextView) findViewById(R.id.tvcharles);
//        tvsice = (TextView) findViewById(R.id.tvsice);
//        tv3 = (TextView) findViewById(R.id.tv3);
//        tv4 = (TextView) findViewById(R.id.tv4);
//
//        tvcharles.setOnClickListener(this);
//        tvsice.setOnClickListener(this);
//        tv3.setOnClickListener(this);
//        tv4.setOnClickListener(this);

//        mbttn = (Button) findViewById(R.id.button);
//        mbttn.setOnClickListener(this);

  /*
        yesterdays code
            if (tv1.getText() == "boshal") {
                tv1.setText("the god himself");
            }
            else{
                tv1.setText("boshal");
            }
        */
        /*
        Part 2
        switch (v.getId()) {
            case R.id.tv1 :
                Log.i(TAG,"TextView1Pressed");
                break;
            case R.id.tv2 :
                Log.i(TAG,"TextView2Pressed");
                break;
            case R.id.button :
                Toast.makeText(MainActivity.this, "boshal", Toast.LENGTH_SHORT).show();
                break;
            default :
                Log.i(TAG,"Something else");

        }
        */
         /*
        part 3
        switch (v.getId()) {
            case R.id.tvcharles :
                array[0]++;
                Log.i("tvcharles","tvcharles was pressed");
                Toast.makeText(MainActivity.this, "You clicked me " + array[0] + " times" , Toast.LENGTH_SHORT).show();
                break;
            case R.id.tvsice :
                array[1]++;
                Log.i("tvsice","tvsice was pressed");
                Toast.makeText(MainActivity.this, "You clicked me " + array[1] + " times", Toast.LENGTH_SHORT).show();
                break;
            case R.id.tv3 :
                array[2]++;
                Log.i("tv3","tv3 was pressed");
                Toast.makeText(MainActivity.this, "You clicked me " + array[2] + " times", Toast.LENGTH_SHORT).show();
                break;
            case R.id.tv4 :
                array[3]++;
                Log.i("tv4","tv4 was pressed");
                Toast.makeText(MainActivity.this, "You clicked me " + array[3] + " times", Toast.LENGTH_SHORT).show();
                break;
            default :
                Log.i(TAG,"Something else was clicked");
        }*/
