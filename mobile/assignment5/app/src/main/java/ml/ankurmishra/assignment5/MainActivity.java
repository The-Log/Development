package ml.ankurmishra.assignment5;

import android.content.Context;
import android.content.Intent;
import android.content.res.AssetManager;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.Bundle;
import android.provider.MediaStore;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
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
import java.io.ByteArrayOutputStream;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.List;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

public class MainActivity extends AppCompatActivity implements NavigationView.OnNavigationItemSelectedListener,View.OnClickListener {
    private final String INTERNAL_STORAGE_FILE = "db.json";
    private EditText mTV1;
    private ImageView mIV1;
    private Button mBttn;
    private FloatingActionButton mFAB;
    private int i = 0;
    static final int REQUEST_IMAGE_CAPTURE = 1;
    private SlideShow ss = new SlideShow();
    private Gson gson;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        ActionBarDrawerToggle toggle = new ActionBarDrawerToggle(
                this, drawer, toolbar, R.string.navigation_drawer_open, R.string.navigation_drawer_close);
        drawer.setDrawerListener(toggle);
        toggle.syncState();

        NavigationView navigationView = (NavigationView) findViewById(R.id.nav_view);
        navigationView.setNavigationItemSelectedListener(this);

        mTV1 = (EditText)findViewById(R.id.tv1);
        mBttn = (Button)findViewById(R.id.bttn);
        mIV1 = (ImageView)findViewById(R.id.iv);
        mFAB = (FloatingActionButton)findViewById(R.id.fab);

        mIV1.setOnClickListener(this);
        mTV1.setOnClickListener(this);
        mBttn.setOnClickListener(this);
        mFAB.setOnClickListener(this);
        pullDB();

        if(ss.getImages().size() > 0) {
            i = ss.getIndex();
            String imageName = ss.getImages().get(i % ss.getImages().size());
            mTV1.setText(imageName);
            Log.i("nCreate",imageName);
            Bitmap imageBitmap = readInternalImageFile(imageName);
            mIV1.setImageBitmap(imageBitmap);
        }
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
        super.onPause();
    }
    public void onStop(){
        pushDB();
        super.onStop();
    }
    public void onRestart() {
        pushDB();
        super.onRestart();
    }
    public void onDestroy() {
        Log.i("Destroy", "App Killed");
        pushDB();
        super.onDestroy();
    }
    public void pullDB(){
        String json = readInternalFile();
        if (json == null){
            writeInternalFile("{\n" +
                    "\t\"objectName\": \"images\",\n" +
                    "\t\"images\": [\n"+ "\t],\n" +
                    "\tindex: 0\n" +
                    "}");
            json = readInternalFile();
        }
        Log.i("JSON", json);
        gson = new GsonBuilder().create();
        ss = gson.fromJson(json, SlideShow.class);
        Log.d("pullDB", "Images: " + ss.toString());
    }
    public void pushDB(){
        Log.d("pushDB", ss.toString());
        writeInternalFile(ss.toString());
        String json = readInternalFile();
        Log.d("db.json", json);
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
    private void dispatchTakePictureIntent() {
        Intent takePictureIntent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
        if (takePictureIntent.resolveActivity(getPackageManager()) != null) {
            startActivityForResult(takePictureIntent, REQUEST_IMAGE_CAPTURE);
        }
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
    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        if (requestCode == REQUEST_IMAGE_CAPTURE && resultCode == RESULT_OK) {
            Bundle extras = data.getExtras();
            Bitmap imageBitmap = (Bitmap) extras.get("data");
            List l = ss.getImages();
            String name = writeInternalImageFile(imageBitmap);
            l.add(name);
            ss.setImages(l);
            mIV1.setImageBitmap(imageBitmap);
            mTV1.setText(name);
            writeInternalFile(ss.toString());
            Log.d("onActivityResult", ss.toString());
        }
    }
    @Override
    public void onClick(View v) {
        switch (v.getId()) {
            case R.id.fab:
                dispatchTakePictureIntent();
//                Log.d("clickFAB", ss.toString());
                break;
            case R.id.bttn:
                String newName = mTV1.getText().toString();
                if (newName.length() > 2 && ss.getImages().size() > 0) {
                    Log.i("bttn", newName);
                    List l = ss.getImages();
                    String oldName = (String) l.get((i - 1) % ss.getImages().size());
                    writeInternalImageFile(readInternalImageFile(oldName), newName);
                    l.set((i - 1) % ss.getImages().size(), newName);
                    ss.setImages(l);
                }
                break;
            case R.id.iv:
                if(ss.getImages().size() > 0) {
                    String imageName = ss.getImages().get(i % ss.getImages().size());
                    mTV1.setText(imageName);
                    Bitmap imageBitmap = readInternalImageFile(imageName);
                    mIV1.setImageBitmap(imageBitmap);
                    ss.setIndex(i % ss.getImages().size());
                    Log.i("IV", imageName);
                    i++;
                }
                break;
            case R.id.tv1:
                break;
            default:
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
}
