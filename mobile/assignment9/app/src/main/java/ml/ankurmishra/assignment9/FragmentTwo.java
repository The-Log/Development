package ml.ankurmishra.assignment9;

/**
 * Created by ankurM on 11/16/17.
 */


/* ------------------------*/
/*    FILE VERSION 4.0     */
/* ------------------------*/

import android.content.Context;
import android.graphics.Bitmap;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.RatingBar;
import android.widget.TextView;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

import java.util.List;

public class FragmentTwo extends Fragment {
    private View mRootView;
    private FragmentTwoInterface mCallback;
    private TextView mTextView;
    private Movie m;
    private RatingBar simpleRatingBar;

    public FragmentTwo() {
    }

    public static FragmentTwo newInstance() {
        FragmentTwo fragment = new FragmentTwo();
        return fragment;
    }

    @Override
    public void setUserVisibleHint(boolean isVisibleToUser) {
        super.setUserVisibleHint(isVisibleToUser);

        if (isVisibleToUser) {
            Log.i("setUserVisibleHint", "fragment visibility: true");

            // ATTEMPT TO TELL ACTIVITY THAT THIS FRAGMENT IS ACTIVE, BUT IT WILL FAIL
            // IF onAttach HAS NOT BEEN CALLED YET.
            // - FOR THAT REASON, WE CALL setFragmentTwoActive IN ON ATTACH, if and only if
            // THE FRAGMENT IS ACTIVE
            m.setRating(simpleRatingBar.getRating());

            try {
                mCallback.setFragmentTwoActive();
                m = mCallback.getMovie();
                if (m != null) {
                    mTextView.setText(m.getTitle());
                    simpleRatingBar.setRating(m.getRating());
                    Log.i("Frag2", m.toString());
                }
            } catch (Exception e) {
                // errors callback not created yet
            }
        }
        else {
            Log.i("setUserVisibleHint", "fragment visibility: false");
        }

    }

    @Override
    public void onAttach(Context context) {
        super.onAttach(context);
        Log.i("onAttach", "onAttach");

        try {
            mCallback = (FragmentTwoInterface) context;
            if (this.getUserVisibleHint()) {
                // NOTIFY ACTIVITY THAT THIS IS THE ACTIVE FRAGMENT
                mCallback.setFragmentTwoActive();

            }

        } catch (ClassCastException e) {
            throw new ClassCastException(context.toString()
                    + " must implement FragmentTwoInterface");
        }
    }


    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        mRootView = inflater.inflate(R.layout.fragment_two, container, false);
        mTextView = (TextView) mRootView.findViewById(R.id.mname);
        simpleRatingBar = (RatingBar) mRootView.findViewById(R.id.rating); // initiate a rating bar
        m = mCallback.getMovie();
        Log.i("onCreateViewF2", m.toString());
        mTextView.setText(m.getTitle());
        simpleRatingBar.setRating(m.getRating());
        return mRootView;
    }


    public interface FragmentTwoInterface {
        void setFragmentTwoActive();
        Movie getMovie();
    }
}