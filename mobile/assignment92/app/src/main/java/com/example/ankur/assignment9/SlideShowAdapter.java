package com.example.ankur.assignment9;

/**
 * Created by ankurM on 11/9/17.
 */

import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;
import java.util.List;

public class SlideShowAdapter extends RecyclerView.Adapter<SlideShowAdapter.MyViewHolder> {

    private List<SlideShow> SlideShowsList;

    public class MyViewHolder extends RecyclerView.ViewHolder {
        public TextView ssName, imageNames;

        public MyViewHolder(View view) {
            super(view);
            ssName = (TextView) view.findViewById(R.id.name);
            imageNames = (TextView) view.findViewById(R.id.images);
        }
    }


    public SlideShowAdapter(List<SlideShow> SlideShowsList) {
        this.SlideShowsList = SlideShowsList;
    }

    @Override
    public MyViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        View itemView = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.slideshow_list_row, parent, false);

        return new MyViewHolder(itemView);
    }

    @Override
    public void onBindViewHolder(MyViewHolder holder, int position) {
        SlideShow SlideShow = SlideShowsList.get(position);
        holder.ssName.setText(SlideShow.getObjectName());
        holder.imageNames.setText(SlideShow.ssNames());
    }

    @Override
    public int getItemCount() {
        return SlideShowsList.size();
    }
}
