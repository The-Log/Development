package ml.ankurmishra.assignment9;

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
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

/**
 * Created by ankur on 12/12/17.
 */

public class FragmentOne extends Fragment implements View.OnClickListener {
    private View mRootView;
    private FragmentOneInterface mCallback;
    private TextView mTextView;
    private Button mButton;
    private int mClickCounter = 0;
    public TextView mLabel;
    private MovieContainer movieContainer;
    public RecyclerView mRecyclerView;
    private MoviesAdapter mAdapter;

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
        mTextView = (TextView) mRootView.findViewById(R.id.mname);

        mRecyclerView = (RecyclerView) mRootView.findViewById(R.id.recycler_view);
        Gson gson = new GsonBuilder().create();
        movieContainer = gson.fromJson(mCallback.getStringAsset("db.json"), MovieContainer.class);
        Log.i("lol","mc" + movieContainer.getList());

        mAdapter = new MoviesAdapter(movieContainer.getList());
        RecyclerView.LayoutManager mLayoutManager = new LinearLayoutManager(this.getActivity());
        mRecyclerView.setLayoutManager(mLayoutManager);
        mRecyclerView.setItemAnimator(new DefaultItemAnimator());
        mRecyclerView.setAdapter(mAdapter);
        mCallback.prepareMovieData();
        mAdapter.notifyDataSetChanged();

        return mRootView;
    }

    @Override
    public void onClick(final View view) {
        int i = mRecyclerView.getChildAdapterPosition(view);
        Movie m =  movieContainer.get(i);
        mCallback.setMovie(movieContainer.get(i));
        Log.d("FragmentOne", m.toString());
    }

    public interface FragmentOneInterface {
        String getStringAsset(String s);
        void prepareMovieData();
        void setMovie(Movie m);
        void setFragmentOneActive();
    }
}

