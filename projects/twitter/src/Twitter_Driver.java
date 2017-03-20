//Miss Galanos
//version 12.8.2015
import twitter4j.*;       //set the classpath to lib\twitter4j-core-4.0.2.jar
import java.util.List;
import java.io.*;
import java.util.ArrayList;
import twitter4j.Query;
import twitter4j.QueryResult;
import twitter4j.Status;
import twitter4j.Twitter;
import twitter4j.TwitterException;
import twitter4j.TwitterFactory;

import javax.swing.*;
import java.util.Scanner;

public class Twitter_Driver {
    private static PrintStream consolePrint;

    public static void main(String[] args) throws TwitterException, IOException, InterruptedException {
        consolePrint = System.out;

        TJTwitter bigBird = new TJTwitter(consolePrint);

        // bigBird.tweetOut(message);
        // PART 2
        // Choose a public Twitter user's handle
        /*
        Scanner scan = new Scanner(System.in);
        consolePrint.print("Please enter a Twitter handle, do not include the @symbol --> ");
        String twitter_handle = scan.next();

        while (!twitter_handle.equals("done")) {
            // Print the most popular word they tweet
            bigBird.makeSortedListOfWordsFromTweets(twitter_handle);
            consolePrint.println("The most common word from @" + twitter_handle + " is: " + bigBird.mostPopularWord());
            consolePrint.println();
            consolePrint.print("Please enter a Twitter handle, do not include the @ symbol --> ");
            twitter_handle = scan.next();
        }
        */

        //PART 3
        bigBird.poularityOfTerms();
    }

}//end driver

class TJTwitter {
    private Twitter twitter;
    private PrintStream consolePrint;
    private List<Status> statuses;
    private List<String> sortedTerms;
    public TJTwitter(PrintStream console) {
        // Makes an instance of Twitter - this is re-useable and thread safe.
        twitter = TwitterFactory.getSingleton(); //connects to Twitter and performs authorizations
        consolePrint = console;
        statuses = new ArrayList<Status>();
        sortedTerms = new ArrayList<String>();
    }
    @SuppressWarnings("unchecked")
    /******************
     * Part 1
     *******************/
    public void tweetOut(String message) throws TwitterException, IOException {
        twitter.updateStatus(message);
    }
    @SuppressWarnings("unchecked")
    /******************  Part 2 *******************/
    public static void sort(List<String> strings) {
        String s = "";
        int j = 0;
        for (int i = 0; i < strings.size(); i++) {
            s = strings.get(i);
            j = i - 1;
            while (j >= 0 && strings.get(j).compareTo(s) > 0) {
                strings.set(j + 1, strings.get(j));
                j--;
            }
            strings.set(j + 1, s);
        }
    }
    public void makeSortedListOfWordsFromTweets(String handle) throws TwitterException, IOException {
        statuses.clear();
        sortedTerms.clear();
        PrintStream fileout = new PrintStream(new FileOutputStream("tweets.txt")); // Creates file for dedebugging purposes
        Paging page = new Paging(1, 200);
        int p = 1;
        while (p <= 10) {
            page.setPage(p);
            statuses.addAll(twitter.getUserTimeline(handle, page));
            p++;
        }
        int numberTweets = statuses.size();
        fileout.println("Number of tweets = " + numberTweets);

        fileout = new PrintStream(new FileOutputStream("garbageOutput.txt"));

        int count = 1;
        for (Status j : statuses) {
            fileout.println(count + ".  " + j.getText());
            count++;
        }

        //Makes a list of words from user timeline
        for (Status status : statuses) {
            String[] array = status.getText().split(" ");
            for (String word : array)
                sortedTerms.add(removePunctuation(word).toLowerCase());
        }
        // Remove common English words, which are stored in commonWords.txt
        sortedTerms = removeCommonEnglishWords(sortedTerms);
        sortedTerms = removeCommonEnglishWords(sortedTerms);
        for (int i = 0; i < sortedTerms.size(); i++) {
            if(sortedTerms.get(i).contains("@")){
                sortedTerms.remove(i);
            }
        }
        sortAndRemoveEmpties();
    }
    // Sort words in alpha order. You should use your old code from the Sort/Search unit.
    // Remove all empty strings ""
    @SuppressWarnings("unchecked")
    private void sortAndRemoveEmpties() {
        sort(sortedTerms);
        for (int i = 0; i < sortedTerms.size(); i++) {
            sortedTerms.remove("");
        }
    }
    // Removes common English words from list
    // Remove all words found in commonWords.txt  from the argument list.
    // The count will not be given in commonWords.txt. You must count the number of words in this method.
    // This method should NOT throw an exception. Use try/catch.
    @SuppressWarnings("unchecked")
    private List removeCommonEnglishWords(List<String> list) throws FileNotFoundException{
        Scanner infile = new Scanner(new BufferedReader(new FileReader
                ("/home/amishra/Copy/Computer Science/AP CS/Unit 5 Collections/src/commonWords.txt")));
        Scanner infile1 = new Scanner(new BufferedReader(new FileReader
                ("/home/amishra/Copy/Computer Science/AP CS/Unit 5 Collections/src/commonWords.txt")));
        int counter = 0;
        while(infile.hasNext()){
            counter++;
            infile.next();
        }
        //System.out.println(counter);
        String[] commonWords = new String[counter];
        infile.close();
        for (int i = 0; i < counter; i++) {
            commonWords[i] = infile1.next();
        }
        infile1.close();
        for (int i = 0; i < list.size(); i++) {
            for (int j = 0; j <commonWords.length; j++) {
                if(list.get(i).equalsIgnoreCase(commonWords[j])) {
                    list.remove(i);
                }
            }
        }
        return list;
    }

    //Remove punctuation - borrowed from previous lab
    //Consider if you want to remove the # or @ from your words. They could be interesting to keep (or remove).
    private String removePunctuation(String s) {
        String[] punctuation = {"," , "!", ".", "-", "_"};
        for (int i = 0; i < punctuation.length; i++) {
            s = s.replace(punctuation[i], "");
        }
        return s;
    }
    //Should return the most common word from sortedTerms.
    //Consider case. Should it be case sensitive? The choice is yours.
    @SuppressWarnings("unchecked")
    public String mostPopularWord() {
        int count = 0;
        int popCount = 0;
        String popWord = "";
        for (int i = 0; i < sortedTerms.size()-1; i++) {
            if(sortedTerms.get(i+1).equals(sortedTerms.get(i)))
                count++;
            if(!sortedTerms.get(i+1).equals(sortedTerms.get(i)))
                count = 0;
            if(count > popCount){
                popWord = sortedTerms.get(i);
                popCount = count;
            }
        }
        System.out.println("Count = " + popCount + " out of the last " +sortedTerms.size() + " tweets.");
        return popWord;
    }
     /******************
     * Part 3
     *******************/
     public void poularityOfTerms() throws TwitterException, IOException, InterruptedException {
         List<String> keyTerms = new ArrayList();
         String keyterm = JOptionPane.showInputDialog("Enter key topics you would like to see their popularity.\n" +
                 "If you would like to search up tweets on the 2016 Presidential Election Candidates, type \"Presidential Election.\"\n" +
                 "If you are finished type \"done.\"");
         while (!keyterm.equals("done")) {
             if(keyterm.equalsIgnoreCase("Presidential Election")){
                /* keyTerms.add("Hillary Clinton");
                 keyTerms.add("Bernie Sanders");
                 keyTerms.add("Donald Trump");
                 keyTerms.add("Ted Cruz");
                 keyTerms.add("John Kasich");*/
                 keyTerms.add("assassinate Trump");
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
         PrintStream tweets = new PrintStream(new FileOutputStream("popularityTweets.txt"));

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

    // A sample query to determine how many people in Arlington, VA tweet about the Miami Dolphins
    public void sampleInvestigate() {
        Query query = new Query("Miami Dolphins");
        query.setCount(100);
        query.setGeoCode(new GeoLocation(38.8372839, -77.1082443), 5, Query.MILES);
        try {
            QueryResult result = twitter.search(query);
            System.out.println("Count : " + result.getTweets().size());
            for (Status tweet : result.getTweets()) {
                System.out.println("@" + tweet.getUser().getName() + ": " + tweet.getText());
            }
        } catch (TwitterException e) {
            e.printStackTrace();
        }
        System.out.println();
    }

}