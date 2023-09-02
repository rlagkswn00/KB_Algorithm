package day99.practice;

import java.io.*;
import java.util.*;

public class BOJ_2527_2 {

	static int max;
	static int[][] arr;
	static ArrayList<Integer> xarr = new ArrayList<>();
	static ArrayList<Integer> yarr = new ArrayList<>();

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		for (int c = 0; c < 4; c++) {
			st = new StringTokenizer(br.readLine());

			int x1 = Integer.parseInt(st.nextToken());
			int y1 = Integer.parseInt(st.nextToken());
			int x2 = Integer.parseInt(st.nextToken());
			int y2 = Integer.parseInt(st.nextToken());

			xarr.add(x1);
			xarr.add(x2);
			yarr.add(y1);
			yarr.add(y2);

			int x3 = Integer.parseInt(st.nextToken());
			int y3 = Integer.parseInt(st.nextToken());
			int x4 = Integer.parseInt(st.nextToken());
			int y4 = Integer.parseInt(st.nextToken());

			xarr.add(x3);
			xarr.add(x4);
			yarr.add(y3);
			yarr.add(y4);

			// max x, y 찾기
			int X = Collections.max(xarr);
			int Y = Collections.max(yarr);

			arr = new int[X + 5][Y + 5];

			// for1
			for (int i = x1; i <= x2; i++) {
				for (int j = y1; j <= y2; j++) {
					arr[i][j] = 1;
				}
			}

			// for2
			boolean temp = false;
			
			loop1:
			for (int i = x3; i <= x4; i++) {
				for (int j = y3; j <= y4; j++) {

					if (arr[i][j] == 1) {
						arr[i][j] = 2;
					} else {
						arr[i][j] = 1;
					}

					if (arr[i-1][j-1] == 2) {
						if (arr[i][j] == 2) {
							temp = true;
							System.out.println("a");
							break loop1;
						} else if (arr[i - 1][j] == 2 || arr[i][j - 1] == 2) {
							temp = true;
							System.out.println("b");
							break loop1;
						} else {
							temp = true;
							System.out.println("c");
							break loop1;
						}
					} // 공통부분 있는 경우

				}
			}
			
			if(!temp) {System.out.println("d");}

		} // for0

	}
}
