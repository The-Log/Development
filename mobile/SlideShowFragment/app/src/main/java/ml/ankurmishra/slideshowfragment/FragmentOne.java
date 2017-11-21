package ml.ankurmishra.slideshowfragment;

import android.content.res.AssetManager;
import android.graphics.Bitmap;
import android.support.v4.app.Fragment;
import android.content.Context;
import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;

import com.google.gson.Gson;

import java.util.List;
/*
 * Created by ankurM on 11/16/17.
 */

public class FragmentOne extends Fragment implements View.OnClickListener {
    private View mRootView;
    private FragmentOneInterface mCallback;
    private TextView mTextView;
    private Button mButton;
    private Gson gson;
    private int mClickCounter = 0;
    private EditText mET;
    private SlideShow ss;
    public ImageView mIV;
    public TextView mLabel;

    public FragmentOne() {
    }

    public static FragmentOne newInstance() {
        FragmentOne fragment = new FragmentOne();
        return fragment;
    }

    @Override
    public void onAttach(Context context) {
        super.onAttach(context);
        try {
            mCallback = (FragmentOneInterface) context;
            if (this.getUserVisibleHint()) {
                // NOTIFY ACTIVITY THAT THIS IS THE ACTIVE FRAGMENT
                mCallback.setFragmentOneActive();
            }

        } catch (ClassCastException e) {
            throw new ClassCastException(context.toString()
                    + " must implement FragmentOneInterface");
        }
    }

    @Override
    public void setUserVisibleHint(boolean isVisibleToUser) {
        super.setUserVisibleHint(isVisibleToUser);

        if (isVisibleToUser) {
            Log.i("setUserVisibleHint", "fragment visibility: true");
            try {
                mCallback.setFragmentOneActive();
            } catch (Exception e) {
                // errors callback not created yet
            }
        }
        else {
            Log.i("setUserVisibleHint", "fragment visibility: false");
        }
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        mRootView = inflater.inflate(R.layout.fragment_one, container, false);
        mTextView = (TextView) mRootView.findViewById(R.id.tv_01);
        mET = (EditText) mRootView.findViewById(R.id.et1);

        ss = mCallback.getSlideShow(0);
        Log.i("onCreateViewF1", ss.toString());
        mIV = (ImageView) mRootView.findViewById(R.id.iv);
        mIV.setOnClickListener(this);
        mLabel = (TextView) mRootView.findViewById(R.id.label);

        if (ss.getImages().size() > 0) {
            int index = ss.getIndex();
            index = (index + 1) % ss.getImages().size();
            String imageName = ss.getImages().get(index);
            Bitmap bm = mCallback.readInternalImageFile(imageName);
            mIV.setImageBitmap(bm);
            mLabel.setText(imageName);
        }

        mTextView.setText("This is a Fragment 1");
        mButton = (Button) mRootView.findViewById(R.id.button1);
        mButton.setOnClickListener(this);

        return mRootView;
    }

    @Override
    public void onClick(View v) {
        switch (v.getId()) {
            case R.id.button1:
                Log.i("button1", mET.getText().toString());
                String newName = mET.getText().toString();
                int i = ss.getIndex();
                if (newName.length() > 2 && ss.getImages().size() > 0) {
                    newName = newName.replaceAll(" ", "_");
                    List l = ss.getImages();
                    String oldName = (String) l.get((i) % ss.getImages().size());
                    mCallback.writeInternalImageFile(mCallback.readInternalImageFile(oldName), newName);
                    l.set((i) % ss.getImages().size(), newName);
                    ss.setImages(l);
                    mET.setText(""); mLabel.setText(newName);

                }
                break;
            case R.id.iv:
                int index = ss.getIndex();
                if (ss.getImages().size() > 0){
                    index = (index + 1) % ss.getImages().size();
                    String imageName = ss.getImages().get(index);
                    Bitmap bm = mCallback.readInternalImageFile(imageName);
                    ss.setIndex(index);
                    mIV.setImageBitmap(bm);
                    mLabel.setText(imageName);
                }
                break;
            default:
        }
    }

    public interface FragmentOneInterface {
        Bitmap readInternalImageFile(String fname);
        String writeInternalImageFile(Bitmap b, String s);
        SlideShow getSlideShow(int i);
        void setFragmentOneActive();
    }
}
