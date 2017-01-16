import twitter4j.*;
import twitter4j.Status;
import twitter4j.Twitter;
import twitter4j.TwitterException;
import twitter4j.TwitterFactory;
import java.util.List;
import java.io.*;
import java.util.ArrayList;

import javax.swing.*;

/**
 * Created by amishra on 1/1/16.
 */
public class TweeterTinkering4Keks {


    private static PrintStream consolePrint;

    public static void main(String[] args) throws TwitterException, IOException, InterruptedException {
        consolePrint = System.out;
        twitterFun tweet = new twitterFun(consolePrint);
        tweet.bot();
        // String select = JOptionPane.showInputDialog("Type in \"bot\" to automate messages.\nType in \"popular\" to search for terms popularity.\"\n" +
        //       "Otherwise type \"done.\"");
        //if(select.equals("popular"))
        //  tweet.poularityOfTerms();
        //if (select.equals("bot"))
            //tweet.bot();
        //if (select.equals("done")){
        // System.exit(1);
    }
       /* else{
            while (!select.equals("done")) {
                if(select.equals("popular"))
                    tweet.poularityOfTerms();
                if (select.equals("bot"))
                    tweet.bot();
                select = JOptionPane.showInputDialog("Type in \"bot\" to automate messages.\nType in \"popular\" to search for terms popularity.\"\n" +
                        "Otherwise type \"done.\"");
            }
        }
    }*/
}

class twitterFun {
    private Twitter twitter;
    private PrintStream consolePrint;
    private List<Status> statuses;
    private List<String> sortedTerms;

    public twitterFun(PrintStream console) {
        twitter = TwitterFactory.getSingleton();
        consolePrint = console;
        statuses = new ArrayList<Status>();
        sortedTerms = new ArrayList<String>();
    }
    /**Tweets for you**/
    @SuppressWarnings("unchecked")
    public void tweetOut(String message) throws TwitterException, IOException {
        twitter.updateStatus(message);
    }
    /*Tracks popularity of the terms you read.*/
    public void poularityOfTerms() throws TwitterException, IOException, InterruptedException {
        List<String> keyTerms = new ArrayList();
        String keyterm = JOptionPane.showInputDialog("Enter key topics you would like to see their popularity.\n" +
                "If you would like to search up tweets on the 2016 Presidential Election Candidates, type \"Presidential Election.\"\n" +
                "If you are finished type \"done.\"");
        while (!keyterm.equals("done")) {
            if(keyterm.equalsIgnoreCase("Presidential Election")){
                keyTerms.add("Hillary Clinton");
                keyTerms.add("Bernie Sanders");
                keyTerms.add("Martin O'Malley");
                keyTerms.add("Donald Trump");
                keyTerms.add("Ted Cruz");
                keyTerms.add("Ben Carson");
                keyTerms.add("Marco Rubio");
                keyTerms.add("Jeb Bush");
                keyTerms.add("Rand Paul");
                keyTerms.add("Chris Christie");
                break;
            }
            keyTerms.add(keyterm);
            keyterm = JOptionPane.showInputDialog("Enter key topics you would like to see their popularity. \n If you are finished type \"done.\"");
        }
        List<String> locationsNames = new ArrayList();
        locationsNames.add("Washington DC"); //Washington DC
        locationsNames.add("Orlando"); //Orlando
        locationsNames.add("Las Angeles"); //Las Angeles
        locationsNames.add("Las Vegas"); //Las Vegas
        locationsNames.add("Chicago"); //Chicago

        List<GeoLocation> locations = new ArrayList();
        locations.add(new GeoLocation(38, -77)); //Washington DC
        locations.add(new GeoLocation(38, -97)); //Orlando
        locations.add(new GeoLocation(34.053, -118.2642)); //Las Angeles
        locations.add(new GeoLocation(36.0781,-115.2124)); //Las Vegas
        locations.add(new GeoLocation(41.8776, -87.6272)); //Chicago

        PrintStream fileout = new PrintStream(new FileOutputStream("popularityByCity.txt"));
        PrintStream tweets = new PrintStream(new FileOutputStream("popularTweets.txt"));

        for (int i = 0; i < keyTerms.size(); i++) {
            int totalAppearanceOfKey = 0;
            for (int j = 0; j < locations.size(); j++) {
                Query query = new Query(keyTerms.get(i));
                query.setCount(900000000);
                query.setGeoCode(locations.get(j), 60, Query.MILES);
                try {
                    QueryResult result = twitter.search(query);
                    System.out.println("The number of tweets about " + keyTerms.get(i) + ": " + result.getTweets().size() + " in " + locationsNames.get(j));
                    fileout.println("The number of tweets about " + keyTerms.get(i) + ": " + result.getTweets().size() + " in " + locationsNames.get(j));
                    totalAppearanceOfKey = totalAppearanceOfKey + result.getTweets().size();
                    for (Status tweet : result.getTweets()) {
                        tweets.println("@" + tweet.getUser().getName() + ": " + tweet.getText());
                    }
                } catch (TwitterException e) {
                    e.printStackTrace();
                }
            }
            System.out.println(keyTerms.get(i) + " has " + totalAppearanceOfKey +" tweets");
            System.out.println();
            fileout.println();
        }
    }
    /*Sends various messages every 5 minutes. Bugged as of this moment. */
    public void bot() throws TwitterException, IOException, InterruptedException{
        Twitter twitter = TwitterFactory.getSingleton();
        List<String> usernames = new ArrayList<>();
        List<String> messages = new ArrayList();
        List<File> files =  new ArrayList<>();
        File dir = new File("/Volumes/Mac OSX SSD 120GB/Users/ankurM/Development/cs/AP CS/Unit 5 Collections/src/shillingEquipment/");
        File[] directoryListing = dir.listFiles();
        if (directoryListing != null) {
            for (File child : directoryListing) {
                files.add(child);
            }
        }
        else
            System.out.println("RIP!");

        usernames.add("hehexd");

        messages.add("I am a bot!");

        String username = usernames.get((int) (usernames.size() * Math.random()));
        String current = messages.get((int) (messages.size() * Math.random()));
        File randomFile = files.get((int) (files.size() * Math.random()));
        while (true) {
            System.out.println(".@" + username + " " + current);
            StatusUpdate statusUpdate = new StatusUpdate(".@" + username + " " + current);
            twitter.uploadMedia(randomFile);
            statusUpdate.setMedia(randomFile);
            twitter.updateStatus(statusUpdate);
            System.out.println("Please wait 2 min.");
            Thread.sleep(2 * 60 * 1000);
            username = usernames.get((int) (usernames.size() * Math.random()));
            current = messages.get((int) (messages.size() * Math.random()));
            randomFile = files.get((int) (files.size() * Math.random()));
        }
    }

}