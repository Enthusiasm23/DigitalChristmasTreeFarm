package view;

import javax.swing.*;

public class MyFrame extends JFrame {

    MyPanel p;

    MyFrame() throws Exception {
        p = new MyPanel();
        add(p);
        setSize(800, 600);
        setTitle("Merry Christmas");
        setVisible(true);
        validate();
        setDefaultCloseOperation(MyFrame.EXIT_ON_CLOSE);
    }
}
