package ml.ankurmishra.drawingapp;

import android.support.v4.app.Fragment;
import android.graphics.Bitmap;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

/**
 * Created by ankur on 12/14/17.
 */

public class DrawingFragment extends Fragment {
    private View mRootView;
    private DrawingFragmentInterface mCallback;

    public DrawingFragment() {
    }

    public static DrawingFragment newInstance() {
        DrawingFragment fragment = new DrawingFragment();
        return fragment;
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        mRootView = inflater.inflate(R.layout.dfragment, container, false);

        return mRootView;
    }
    public interface DrawingFragmentInterface {
        Bitmap readInternalImageFile(String fname);
        String writeInternalImageFile(Bitmap b);
    }
}
