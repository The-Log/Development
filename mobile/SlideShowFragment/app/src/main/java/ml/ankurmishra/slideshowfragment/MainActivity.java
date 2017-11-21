package ml.ankurmishra.slideshowfragment;

import android.content.Context;
import android.content.Intent;
import android.content.res.AssetManager;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.Bundle;
import android.provider.MediaStore;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.FragmentPagerAdapter;
import android.support.v4.app.FragmentTransaction;
import android.support.v4.view.ViewPager;
import android.util.Log;
import android.view.View;
import android.support.design.widget.NavigationView;
import android.support.v4.view.GravityCompat;
import android.support.v4.widget.DrawerLayout;
import android.support.v7.app.ActionBarDrawerToggle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

import java.io.ByteArrayOutputStream;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.List;

public class MainActivity extends AppCompatActivity
        implements NavigationView.OnNavigationItemSelectedListener, FragmentOne.FragmentOneInterface, FragmentTwo.FragmentTwoInterface, FragmentThree.FragmentThreeInterface{
    private static final String INTERNAL_STORAGE_FILE = "db.json";
    private SectionsPagerAdapter mSectionsPagerAdapter;
    private ViewPager mViewPager;
    static final int REQUEST_IMAGE_CAPTURE = 1;
    private String TAG = "TAG";
    private int index = 0;
    private Gson gson = new GsonBuilder().create();
    private SlideShowContainer ssc;

    private Fragment mActiveFragment;

    private FragmentOne mFragmentOne = FragmentOne.newInstance();
    private FragmentTwo mFragmentTwo = FragmentTwo.newInstance();
    private FragmentThree mFragmentThree = FragmentThree.newInstance();

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
                dispatchTakePictureIntent();
            }
        });

        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        ActionBarDrawerToggle toggle = new ActionBarDrawerToggle(
                this, drawer, toolbar, R.string.navigation_drawer_open, R.string.navigation_drawer_close);
        drawer.setDrawerListener(toggle);
        toggle.syncState();

        NavigationView navigationView = (NavigationView) findViewById(R.id.nav_view);
        navigationView.setNavigationItemSelectedListener(this);

        ssc = pullDB();
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
        pushDB(ssc);
        super.onPause();
    }
    public void onStop(){
        pushDB(ssc);
        super.onStop();
    }
    public void onRestart() {
        pushDB(ssc);
        super.onRestart();
    }
    public void onDestroy() {
        Log.i("Destroy", "App Killed");
        pushDB(ssc);
        super.onDestroy();
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
    @SuppressWarnings("StatementWithEmptyBody")
    @Override
    public boolean onNavigationItemSelected(MenuItem item) {
        // Handle navigation view item clicks here.
        int id = item.getItemId();

        if (id == R.id.nav_camera) {
            // Handle the camera action
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

    public class SectionsPagerAdapter extends FragmentPagerAdapter {

        public SectionsPagerAdapter(FragmentManager fm) {
            super(fm);
        }

        @Override
        public Fragment getItem(int position) {
            switch (position) {
                case 0 :
                    return FragmentOne.newInstance();
                case 1 :
                    return FragmentTwo.newInstance();
                case 2 :
                    return FragmentThree.newInstance();
                default :
                    return null;
            }
        }

        @Override
        public int getCount() {
            return 3;       // Show 3 total pages.
        }
    }
    public void setFragmentOneActive() {
        Log.i(TAG, "activity knows Fragment 1 is active!!");
        pushDB(ssc);
        mActiveFragment = mFragmentOne;
    }
    public void setFragmentTwoActive() {
        Log.i(TAG, "activity knows Fragment 2 is active!!");
        pushDB(ssc);
        mActiveFragment = mFragmentTwo;
    }
    public void setFragmentThreeActive() {
        Log.i(TAG, "activity knows Fragment 3 is active!!");
        pushDB(ssc);
        mActiveFragment = mFragmentThree;
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
    public SlideShowContainer pullDB(){
        String json = readInternalFile();
        if (json == null){
            json = getStringAsset("db.json");
        }
        Log.i("JSON", json);
        SlideShowContainer ssc = gson.fromJson(json, SlideShowContainer.class);
        Log.d("pullDB", ssc.toString());
        index = ssc.get(mViewPager.getCurrentItem()).getIndex();
        if (ssc.get(mViewPager.getCurrentItem()).getImages().size() > 0) {
            String imageName = ssc.get(mViewPager.getCurrentItem()).getImages().get(index);
            Bitmap bm = readInternalImageFile(imageName);
            ssc.get(mViewPager.getCurrentItem()).setIndex(index);
        }

        return ssc;
    }
    public void pushDB(SlideShowContainer ssc){
        Log.d("pushDB", ssc.toString());
        writeInternalFile(ssc.toString());
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

            List l = ssc.get(mViewPager.getCurrentItem()).getImages();
            String name = writeInternalImageFile(imageBitmap);
            l.add(name);
            //
            ssc.get(mViewPager.getCurrentItem()).setImages(l);
            writeInternalFile(ssc.toString());
            Log.d("onActivityResult", ssc.toString());
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
    public String writeInternalImageFile(Bitmap b, String s) {
        String imageFileName = s;

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
    public SlideShow getSlideShow(int i){
        pushDB(ssc);
        Log.i("SlideShowContainer", ssc.toString());
        return ssc.get(i);
    }
}
