package day99.practice;

import java.io.*;
import java.util.*;

public class BOJ_1406_0829 {

	static int N, CS;
	static ArrayList<String> list = new ArrayList<>();

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		String str = br.readLine();
		
		// 커서 위치 초기화
		CS = str.length()+1;				
		
		// 초기 String 배열로 이동
		for (char c : str.toCharArray()) {
			list.add(String.valueOf(c));
		}

		// 명령어 횟수 입력
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());

		// 명령어 로직 구현
		for (int i = 1; i <= N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			String cmd1 = st.nextToken();
			if ("L".equals(cmd1) && CS != 0) {
				CS--;
			} else if ("D".equals(cmd1) && CS != list.size() + 1) {
				CS++;
			} else if ("B".equals(cmd1) && CS != 0) {
				list.remove(CS - 1);
			} else if ("P".equals(cmd1) && CS == 0) {
				list.add(CS, st.nextToken());
			} else if ("P".equals(cmd1) && CS != 0 && CS!=list.size()+1) {
				list.add(CS, st.nextToken());
			} else if ("P".equals(cmd1) && CS==list.size()+1) {
				list.add(st.nextToken());
			}
		}
		System.out.println(list);
	}

}
