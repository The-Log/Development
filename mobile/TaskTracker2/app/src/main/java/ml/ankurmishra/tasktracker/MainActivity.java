package ml.ankurmishra.tasktracker;

import android.content.Context;
import android.content.Intent;
import android.content.res.AssetManager;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.Bundle;
import android.provider.MediaStore;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.NavigationView;
import android.support.design.widget.Snackbar;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.FragmentPagerAdapter;
import android.support.v4.app.FragmentTransaction;
import android.support.v4.view.GravityCompat;
import android.support.v4.view.ViewPager;
import android.support.v4.widget.DrawerLayout;
import android.support.v7.app.ActionBarDrawerToggle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

import java.io.ByteArrayOutputStream;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;


public class MainActivity extends AppCompatActivity implements NavigationView.OnNavigationItemSelectedListener, FragmentOne.FragmentOneInterface, FragmentTwo.FragmentTwoInterface, TrackerAdapter.MoviesAdapterInterface, DFrag.DFragInterface {

    private static final int REQUEST_IMAGE_CAPTURE = 1;
    private TrackerContainer trackerContainer = new TrackerContainer(new ArrayList<Tracker>());
    private Tracker pm;
    private Tracker mTrackerAdapter;
    private SectionsPagerAdapter mSectionsPagerAdapter;
    private ViewPager mViewPager;
    private Gson gson = new GsonBuilder().create();
    private String INTERNAL_STORAGE_FILE = "db.json";
    private FragmentTwo mfragmentTwo;
    private FragmentOne mfragmentOne;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        mSectionsPagerAdapter = new SectionsPagerAdapter(getSupportFragmentManager());
        mViewPager = (ViewPager) findViewById(R.id.container);
        mViewPager.setAdapter(mSectionsPagerAdapter);

        FloatingActionButton fab = (FloatingActionButton) findViewById(R.id.fab);
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                DFrag dialogFrag = new DFrag();
                android.app.FragmentManager fm = getFragmentManager();
                dialogFrag.show(fm, getString(R.string.dialog_tag));
            }
        });

        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        ActionBarDrawerToggle toggle = new ActionBarDrawerToggle(
                this, drawer, toolbar, R.string.navigation_drawer_open, R.string.navigation_drawer_close);
        drawer.addDrawerListener(toggle);
        toggle.syncState();

        NavigationView navigationView = (NavigationView) findViewById(R.id.nav_view);
        navigationView.setNavigationItemSelectedListener(this);
    }
    public void onResume(){
        super.onResume();
        pullDB();
    }
    public void onStart(){
        super.onStart();
        pullDB();
    }
    public void onPause(){
        pushDB();
        writeInternalFile(trackerContainer.toString());
        super.onPause();
    }
    public void onStop(){
        pushDB();
        writeInternalFile(trackerContainer.toString());
        super.onStop();
    }
    public void onRestart() {
        pushDB();
        writeInternalFile(trackerContainer.toString());
        super.onRestart();
    }
    public void onDestroy() {
        Log.i("Destroy", "App Killed");
        pushDB();
        writeInternalFile(trackerContainer.toString());
        super.onDestroy();
    }
    public void pullDB(){
        String json = readInternalFile();
        if (json == null){
            json = getStringAsset("db.json");
        }
        Log.i("JSON", json);
        trackerContainer = gson.fromJson(json, TrackerContainer.class);
        Log.d("pullDB", trackerContainer.toString());
    }

    public TrackerContainer getTrackerContainer(){
        String json = readInternalFile();
        if (json == null){
            json = getStringAsset("db.json");
            Log.i("Empty Json", "getTrackerContainer: " + json);
        }
        trackerContainer = gson.fromJson(json, TrackerContainer.class);
        Log.i("getTrackerContainer", trackerContainer.toString());
        return trackerContainer;
    }

    public void pushDB(){
        Log.d("pushDB", trackerContainer.toString());
        writeInternalFile(trackerContainer.toString());
    }

    public String readInternalFile() {
        Context context = getApplicationContext();
        ByteArrayOutputStream result = new ByteArrayOutputStream();
        try {
            FileInputStream fis;
            fis = context.openFileInput(INTERNAL_STORAGE_FILE);
            byte[] buffer = new byte[1024];
            int length;
            while ((length = fis.read(buffer)) != -1) {
                result.write(buffer, 0, length);
            }
            return result.toString("UTF-8");

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }
    public void writeInternalFile(String s) {
        Context context = getApplicationContext();
        try {
            FileOutputStream fos;
            fos = context.openFileOutput(INTERNAL_STORAGE_FILE, Context.MODE_PRIVATE);
            Log.i("WriteInternalFile", s );
            fos.write(s.getBytes());
            fos.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    @Override
    public void onBackPressed() {
        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        if (drawer.isDrawerOpen(GravityCompat.START)) {
            drawer.closeDrawer(GravityCompat.START);
        } else {
            super.onBackPressed();
        }
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }

    public void prepareTrackerData() {
        Gson gson = new GsonBuilder().create();
        trackerContainer = getTrackerContainer();
        Log.i("","" + trackerContainer);
        pm = trackerContainer.get(0);
    }

    @Override
    public void setTracker(Tracker m) {
        pm = m;
    }

    @Override
    public void setFragmentOneActive() {

    }

    @Override
    public TrackerContainer getContainer() {
        return trackerContainer;
    }

    @Override
    public void setFragmentTwoActive() {

    }

    @Override
    public Tracker getTracker() {
        return pm;
    }

    @Override
    public void setCurrentItem(Tracker currentItem) {
        pm = currentItem;
        System.out.println(pm);
        mfragmentTwo.setTracker(pm);
    }

    public void dispatchTakePictureIntent() {
        Intent takePictureIntent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
        if (takePictureIntent.resolveActivity(getPackageManager()) != null) {
            startActivityForResult(takePictureIntent, REQUEST_IMAGE_CAPTURE);
        }
    }

    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        if (requestCode == REQUEST_IMAGE_CAPTURE && resultCode == RESULT_OK) {
            Bundle extras = data.getExtras();
            Bitmap imageBitmap = (Bitmap) extras.get("data");

            String name = writeInternalImageFile(imageBitmap);

            mfragmentTwo.passBitmap(imageBitmap);
        }
    }

    public Bitmap readInternalImageFile(String fname) {
        Context context = getApplicationContext();
        try {
            FileInputStream fis;
            fis = context.openFileInput(fname);
            Bitmap b = BitmapFactory.decodeStream(fis);
            return b;
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        return null;
    }

    public String writeInternalImageFile(Bitmap b) {
        String timeStamp = new SimpleDateFormat("yyyyMMdd_HHmmss").format(new Date());
        String imageFileName = "JPEG_" + timeStamp + "_";

        Context context = getApplicationContext();
        try {
            FileOutputStream fos;
            fos = context.openFileOutput(imageFileName, Context.MODE_PRIVATE);
            b.compress(Bitmap.CompressFormat.JPEG, 100, fos);
            return imageFileName;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }
    
    @Override
    public void addTracker(Tracker tracker) {
        mfragmentOne.updateData(tracker);
    }

    public class SectionsPagerAdapter extends FragmentPagerAdapter {

        public SectionsPagerAdapter(FragmentManager fm) {
            super(fm);
        }

        @Override
        public Fragment getItem(int position) {
            switch (position) {
                case 0 :
                    mfragmentOne = FragmentOne.newInstance();
                    return mfragmentOne;
                case 1 :
                    mfragmentTwo =FragmentTwo.newInstance();
                    return mfragmentTwo;
                default :
                    return null;
            }
        }

        @Override
        public int getCount() {
            return 2;       // Show 2 total pages.
        }
    }

    public String getStringAsset(String filename) {
        AssetManager assetManager = getAssets();
        ByteArrayOutputStream result = new ByteArrayOutputStream();

        try {
            InputStream ins = assetManager.open(filename);
            byte[] buffer = new byte[1024];
            int length;
            while ((length = ins.read(buffer)) != -1) {
                result.write(buffer, 0, length);
            }
            return result.toString("UTF-8");

        } catch (IOException e) {
            e.printStackTrace();
        }

        return null;
    }

    @SuppressWarnings("StatementWithEmptyBody")
    @Override
    public boolean onNavigationItemSelected(MenuItem item) {
        // Handle navigation view item clicks here.
        int id = item.getItemId();

        if (id == R.id.nav_camera) {
            dispatchTakePictureIntent();
        } else if (id == R.id.nav_gallery) {

        } else if (id == R.id.nav_slideshow) {

        } else if (id == R.id.nav_manage) {

        } else if (id == R.id.nav_share) {

        } else if (id == R.id.nav_send) {

        }

        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        drawer.closeDrawer(GravityCompat.START);
        return true;
    }
}
