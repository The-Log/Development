package com.example.ankur.assignment9;

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

        return mRootView;
    }

    @Override
    public void onClick(View v) {
        switch (v.getId()) {
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
