package com.example.notes;

import android.view.View;
import android.widget.LinearLayout;
import android.widget.TextView;

import androidx.recyclerview.widget.RecyclerView;

public class NotesAdapter extends RecyclerView.Adapter<NotesAdapter.NoteViewHolder> {
    public static class NoteViewHolder extends RecyclerView.ViewHolder {
        LinearLayout containerView;
        TextView textView;

        NoteViewHolder(View v) {
            super(v);
            containerView = v.findViewById(R.id.note_row);
            textView = v.findViewById(R.id.note_row_text);
        }
    }
}
