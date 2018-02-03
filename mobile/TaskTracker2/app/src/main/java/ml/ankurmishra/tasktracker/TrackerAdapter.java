package ml.ankurmishra.tasktracker;

/**
 * Created by ankurM on 11/9/17.
 */

import android.content.Context;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;
import android.widget.Toast;

import java.util.List;

public class TrackerAdapter extends RecyclerView.Adapter<TrackerAdapter.MyViewHolder> {

    private List<Tracker> moviesList;
    private MoviesAdapterInterface mCallback;
    private Context context;
    public Tracker currentItem;

    public class MyViewHolder extends RecyclerView.ViewHolder {
        public TextView title, duration;
        public int pos = 0;
        private Context context;

        public MyViewHolder(View view, Context context) {
            super(view);
            this.context = context;

            title = (TextView) view.findViewById(R.id.title);
            duration = (TextView) view.findViewById(R.id.duration);
            view.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    pos = getAdapterPosition();

                    // check if item still exists
                    if (pos != RecyclerView.NO_POSITION) {
                        currentItem = moviesList.get(pos);
                        Toast.makeText(v.getContext(), "You clicked " + currentItem.getTask(), Toast.LENGTH_SHORT).show();
                        mCallback.setCurrentItem(currentItem);
                    }
                }
            });
        }

    }


    public TrackerAdapter(List<Tracker> moviesList) {
        this.moviesList = moviesList;
        currentItem = moviesList.get(0);
    }

    @Override
    public MyViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        View itemView = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.movie_list_row, parent, false);
        context = parent.getContext();
        mCallback = (MoviesAdapterInterface) context;
        return new MyViewHolder(itemView, context);
    }

    @Override
    public void onBindViewHolder(MyViewHolder holder, int position) {
        Tracker tracker = moviesList.get(position);
        holder.title.setText(tracker.getTask());
        holder.duration.setText("" + tracker.getDuration());

    }



    @Override
    public int getItemCount() {
        return moviesList.size();
    }

    public interface MoviesAdapterInterface {
        void setCurrentItem(Tracker currentItem);
    }
}