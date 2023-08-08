package day99.practice;

import java.io.*;
import java.util.*;

public class BOJ_9095 {
	
	static int n, cnt, T;

	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
	
		T = Integer.parseInt(br.readLine());
		
		for(int i=0; i<T; i++) {
			n = Integer.parseInt(br.readLine());
			cnt=0;
			dfs(0);
			System.out.println(cnt);
		}

	}

	public static void dfs(int k) {
		
		if(n==k) {
			cnt++;
			return;
		}else if(n<k){
			return;
		}else{
		dfs(k+1);
		dfs(k+2);
		dfs(k+3);
		}
	}
}
