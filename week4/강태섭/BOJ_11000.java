import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;
 
 
public class Main {
    static int n;
    static int max;
    static PriorityQueue<Integer> queue = new PriorityQueue<>();
    static int [][]time;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n= Integer.parseInt(br.readLine());
        time = new int[n+1][2];
 
        for(int i=1; i<=n; i++){
            String[] s = br.readLine().split(" ");
            time[i][0]=Integer.parseInt(s[0]);
            time[i][1]=Integer.parseInt(s[1]);
        }
        Arrays.sort(time, (a,b) ->{
            if(a[0]>b[0]){
                return 1;
            }
            else if(a[0]==b[0]){
                return a[1]-b[1];
            }
            else{
                return -1;
            }
        });
 
        queue.add(time[1][1]);
        for(int i=2; i<=n; i++){
            if(queue.peek() <=time[i][0]){
                queue.poll();
            }
            queue.add(time[i][1]);
        }
        System.out.println(queue.size() );
    }
}