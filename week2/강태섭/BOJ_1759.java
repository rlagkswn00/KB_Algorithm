package day99.practice;

import java.io.*;
import java.util.*;

public class BOJ_1759 {
	
	static int L, C;
	static boolean[] visited;
	static ArrayList<String> arrans;
	static ArrayList<String> words;
	static String[] mo = {"a","e","i","o","u"};

	
	
	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		
		L = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		visited = new boolean[C];
		arrans = new ArrayList<>();
		words = new ArrayList<>();

		// 단어 들어있는 배열 생성
		st = new StringTokenizer(br.readLine()," ");
		for(int i=0; i<C; i++) {
			words.add(st.nextToken());			
		}
		Collections.sort(words);
		dfs(0, 0, words);

	}

	public static void dfs(int n, int k, ArrayList<String> arr) {
	    if (arrans.size() == L) {
	        int vowelCount = 0;
	        for (String s : arrans) {
	            if (Arrays.asList(mo).contains(s)) vowelCount++;
	        }

	        // 모음이 1개 이상이고 자음이 2개 이상인 경우만 출력
	        if (vowelCount >= 1 && (arrans.size() - vowelCount) >= 2) {
	            Collections.sort(arrans);
	            for (String s : arrans) {
	                System.out.print(s);
	            }
	            System.out.println(); // 줄바꿈 추가
	        }
	        return;
	    }

	    if (k < C) {
	        visited[k] = true;
	        arrans.add(words.get(k));
	        dfs(n + 1, k + 1, arr);
	        arrans.remove(arrans.size() - 1); // 재귀 호출에서 제거된 문자 제거
	        visited[k] = false;
	        dfs(n, k + 1, arr);
	    }
	}

}
