package ml.ankurmishra.tasktracker;

import android.content.Context;
import android.graphics.Bitmap;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.support.v7.widget.DefaultItemAnimator;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

/**
 * Created by ankur on 12/12/17.
 */

public class FragmentOne extends Fragment {
    private View mRootView;
    private FragmentOneInterface mCallback;
    private TextView mTextView;
    private Button mButton;
    private int mClickCounter = 0;
    public TextView mLabel;
    private TrackerContainer trackerContainer;
    public RecyclerView mRecyclerView;
    public TrackerAdapter mAdapter;
    private Tracker currentItem ;

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
            trackerContainer = mCallback.getContainer();

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
        mTextView = (TextView) mRootView.findViewById(R.id.mname);

        mRecyclerView = (RecyclerView) mRootView.findViewById(R.id.recycler_view);
        Gson gson = new GsonBuilder().create();
        trackerContainer = mCallback.getTrackerContainer();
        Log.i("lol","mc" + trackerContainer.getList());

        mAdapter = new TrackerAdapter(trackerContainer.getList());
        currentItem = mAdapter.currentItem;
        RecyclerView.LayoutManager mLayoutManager = new LinearLayoutManager(this.getActivity());
        mRecyclerView.setLayoutManager(mLayoutManager);
        mRecyclerView.setItemAnimator(new DefaultItemAnimator());
        mRecyclerView.setAdapter(mAdapter);
        mCallback.prepareTrackerData();
        mAdapter.notifyDataSetChanged();


        return mRootView;
    }
    public void updateData(Tracker tracker){
        trackerContainer.add(tracker);
        mAdapter.notifyDataSetChanged();
    }

    public interface FragmentOneInterface {
        String getStringAsset(String s);
        void prepareTrackerData();
        void setTracker(Tracker m);
        void setFragmentOneActive();
        TrackerContainer getContainer();
        TrackerContainer getTrackerContainer();
    }
}

