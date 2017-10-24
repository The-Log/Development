package ml.ankurmishra.assignment4;

import android.content.Context;
import android.content.SharedPreferences;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity implements View.OnClickListener  {

    private  int[] sessionCounter = {0,0,0,0,0,0,0};
    private  int[] lifeTimeCounter = {0,0,0,0,0,0,0};
    private View mView;
    private final static String PREFERENCES_FILE = "lifetimeCounter";
    private SharedPreferences sharedPref;
    private TextView TVonCreateCounter, TVonStartCounter, TVonResumeCounter, TVonStopCounter ,TVonRestartCounter, TVonPauseCounter, TVonDestroyCounter;
    private Button button;
    private SharedPreferences.Editor prefsEditor;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);


        setContentView(R.layout.main_activity);

        TVonCreateCounter = (TextView)findViewById(R.id.onCreateCounter);

        TVonResumeCounter = (TextView)findViewById(R.id.onResumeCounter);
        TVonStartCounter = (TextView)findViewById(R.id.onStartCounter);
        TVonPauseCounter = (TextView)findViewById(R.id.onPauseCounter);
        TVonStopCounter = (TextView)findViewById(R.id.onStopCounter);
        TVonRestartCounter = (TextView)findViewById(R.id.onRestartCounter);
        TVonDestroyCounter = (TextView)findViewById(R.id.onDestroyCounter);
        TVonResumeCounter = (TextView)findViewById(R.id.onResumeCounter);

        Context context = MainActivity.this;
        sharedPref = context.getSharedPreferences(PREFERENCES_FILE, Context.MODE_PRIVATE);
        lifeTimeCounter[0] = sharedPref.getInt("oCreatec", 0);

        TVonResumeCounter.setText("Session onResumeCounter: "+ sessionCounter[1] +" \n Global onResumeCounter: "+lifeTimeCounter[1]+" \n");
        lifeTimeCounter[1] = sharedPref.getInt("oResumec", 0);
        TVonResumeCounter.setText("Session onResumeCounter: "+ sessionCounter[1] +" \n Global onResumeCounter: "+lifeTimeCounter[1]+" \n");
        lifeTimeCounter[2] = sharedPref.getInt("oStartc", 0);
        TVonStartCounter.setText("Session onStartCounter: "+ sessionCounter[2] +" \n Global onStartCounter: "+lifeTimeCounter[2]+" \n");
        lifeTimeCounter[3]= sharedPref.getInt("oPausec", 0);
        TVonPauseCounter.setText("Session onPause Counter: "+ sessionCounter[3] +" \n Global onPause Counter: "+lifeTimeCounter[3]+" \n");
        lifeTimeCounter[4] = sharedPref.getInt("oStopc", 0);
        TVonStopCounter.setText("Session onStop Counter: "+ sessionCounter[4] +" \n Global onStop Counter: "+lifeTimeCounter[4]+" \n");
        lifeTimeCounter[5] = sharedPref.getInt("oRestartc", 0);
        TVonRestartCounter.setText("Session onRestartCounter: "+ sessionCounter[5] +" \n Global onRestartCounter: "+lifeTimeCounter[5]+" \n");
        lifeTimeCounter[6] = sharedPref.getInt("oDestroyc", 0);
        TVonDestroyCounter.setText("Session OnDestroy Counter: "+ sessionCounter[6] +" \n Global OnDestroy Counter: "+lifeTimeCounter[6]+" \n");

        button = (Button) findViewById(R.id.bttn);
        button.setOnClickListener(this);

        prefsEditor = sharedPref.edit();

        sessionCounter[0] ++;
        lifeTimeCounter[0]++;
        TVonCreateCounter.setText("Session onCreateCounter: "+ sessionCounter[0] +" \n Global onCreateCounter: "+lifeTimeCounter[0]+" \n");
        prefsEditor.putInt("oCreatec", lifeTimeCounter[0]);

        prefsEditor.commit();


    }
    public void onResume(){

        super.onResume();
        sessionCounter[1] ++;
        lifeTimeCounter[1]++;
        TVonResumeCounter.setText("Session onResumeCounter: "+ sessionCounter[1] +" \n Global onResumeCounter: "+lifeTimeCounter[1]+" \n");
        prefsEditor.putInt("oResumec", lifeTimeCounter[1]);
        prefsEditor.commit();

    }
    public void onStart(){
        sessionCounter[2] ++;
        lifeTimeCounter[2]++;
        Log.i("lol", "onStart: " + lifeTimeCounter[2]);
        TVonStartCounter.setText("Session onStartCounter: "+ sessionCounter[2] +" \n Global onStartCounter: "+lifeTimeCounter[2]+" \n");
        prefsEditor.putInt("oStartc", lifeTimeCounter[2]);
        prefsEditor.commit();


        super.onStart();
    }
    public void onPause(){
        sessionCounter[3] ++;
        lifeTimeCounter[3]++;
        TVonPauseCounter.setText("Session onPause Counter: "+ sessionCounter[3] +" \n Global onPause Counter: "+lifeTimeCounter[3]+" \n");
        prefsEditor.putInt("oPausec", lifeTimeCounter[3]);
        prefsEditor.commit();


        super.onPause();
    }
    public void onStop(){
        sessionCounter[4] ++;
        lifeTimeCounter[4]++;
        TVonStopCounter.setText("Session onStop Counter: "+ sessionCounter[4] +" \n Global onStop Counter: "+lifeTimeCounter[4]+" \n");
        prefsEditor.putInt("oStopc", lifeTimeCounter[4]);
        prefsEditor.commit();


        super.onStop();

    }
    public void onRestart() {
        sessionCounter[5] ++;
        lifeTimeCounter[5]++;
        TVonRestartCounter.setText("Session onRestartCounter: "+ sessionCounter[5] +" \n Global onRestartCounter: "+lifeTimeCounter[5]+" \n");
        prefsEditor.putInt("oRestartc", lifeTimeCounter[5]);
        prefsEditor.commit();


        super.onRestart();
    }
    public void onDestroy() {
        sessionCounter[6] ++;
        lifeTimeCounter[6]++;
        TVonDestroyCounter.setText("Session OnDestroy Counter: "+ sessionCounter[6] +" \n Global OnDestroy Counter: "+lifeTimeCounter[6]+" \n");
        prefsEditor.putInt("oDestroyc", lifeTimeCounter[6]);
        prefsEditor.commit();


        super.onDestroy();
    }
    @Override
    public void onClick(View view) {
        for (int i = 0 ; i < 7; i++){
            sessionCounter[i] = 0;
            lifeTimeCounter[i] = 0;
        }

        prefsEditor.putInt("oCreatec", lifeTimeCounter[0]);
        prefsEditor.putInt("oResumec", lifeTimeCounter[1]);
        prefsEditor.putInt("oStartc", lifeTimeCounter[2]);
        prefsEditor.putInt("oPausec", lifeTimeCounter[3]);
        prefsEditor.putInt("oStopc", lifeTimeCounter[4]);
        prefsEditor.putInt("oRestartc", lifeTimeCounter[5]);
        prefsEditor.putInt("oDestroyc", lifeTimeCounter[6]);

        TVonCreateCounter.setText("Session onCreateCounter: "+lifeTimeCounter[0] +" \n Global onCreateCounter: "+lifeTimeCounter[0]+" \n");
        TVonResumeCounter.setText("Session onResumeCounter: "+ sessionCounter[1] +" \n Global onResumeCounter: "+lifeTimeCounter[1]+" \n");
        TVonStartCounter.setText("Session onStartCounter: "+ sessionCounter[2] +" \n Global onStartCounter: "+lifeTimeCounter[2]+" \n");
        TVonPauseCounter.setText("Session onPause Counter: "+ sessionCounter[3] +" \n Global onPause Counter: "+lifeTimeCounter[3]+" \n");
        TVonStopCounter.setText("Session onStop Counter: "+ sessionCounter[4] +" \n Global onStop Counter: "+lifeTimeCounter[4]+" \n");
        TVonRestartCounter.setText("Session onRestartCounter: "+ sessionCounter[5] +" \n Global onRestartCounter: "+lifeTimeCounter[5]+" \n");
        TVonDestroyCounter.setText("Session OnDestroy Counter: "+ sessionCounter[6] +" \n Global OnDestroy Counter: "+lifeTimeCounter[6]+" \n");

    }
}