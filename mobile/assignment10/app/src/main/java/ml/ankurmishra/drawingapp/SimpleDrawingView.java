package ml.ankurmishra.drawingapp;

import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.graphics.Path;
import android.graphics.Point;
import android.util.AttributeSet;
import android.view.MotionEvent;
import android.view.View;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by ankur on 12/12/17.
 */

public class SimpleDrawingView extends View {
    private final int paintColor = Color.RED;
    // defines paint and canvas
    private Paint drawPaint;
    private Path path = new Path();
    private List<Point> circlePoints;

    public SimpleDrawingView(Context context, AttributeSet attrs) {
        super(context, attrs);
        setupPaint(); // same as before
        circlePoints = new ArrayList<Point>();
    }

    // Setup paint with color and stroke styles
    private void setupPaint() {

        drawPaint = new Paint();
        drawPaint.setColor(paintColor);
        drawPaint.setAntiAlias(true);
        drawPaint.setStyle(Paint.Style.STROKE);
        drawPaint.setStrokeJoin(Paint.Join.ROUND);
        drawPaint.setStrokeCap(Paint.Cap.ROUND);
        drawPaint.setStrokeWidth(5);
        drawPaint.setStyle(Paint.Style.STROKE);
    }

    public boolean onTouchEvent(MotionEvent event) {
        float pointX = event.getX();
        float pointY = event.getY();
        // Checks for the event that occurs
        switch (event.getAction()) {
            case MotionEvent.ACTION_DOWN:
                // Starts a new line in the path
                path.moveTo(pointX, pointY);
                break;
            case MotionEvent.ACTION_MOVE:
                // Draws line between last point and this point
                path.lineTo(pointX, pointY);
                break;
            default:
                return false;
        }

        postInvalidate(); // Indicate view should be redrawn
        return true; // Indicate we've consumed the touch
    }

    protected void onDraw(Canvas canvas) {
        canvas.drawPath(path, drawPaint);
    }
}
