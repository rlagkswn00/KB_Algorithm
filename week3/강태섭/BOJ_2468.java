package day99.practice;

import java.io.*;

import java.util.*;

public class Main {
	static int n;
	static int[][] map;
	static boolean[][] checked;
	static int[] dx = {1, 0, -1, 0};
	static int[] dy = {0,- 1, 0, 1};
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		
		map = new int[n][n];
		
		int maxHeight=0;
		for(int i=0; i<n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for(int j=0; j<n; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
				if(map[i][j] > maxHeight) {
					maxHeight =map[i][j];
				}
			}
		}
		
		int max =0;
		// 1. 모든 지역 탐색
		for(int height=0; height<maxHeight+1; height++) {
			checked = new boolean[n][n];
			int cnt=0;
			for(int i=0; i<n; i++) {
				for(int j=0; j<n; j++) {
					// 2. 안전 영역 탐지
					if(!checked[i][j] && map[i][j] > height){
						cnt+=bfs(i,j,height); // 해당 안전영역 탐색 시작
					}
					
				}
			}
			max = Math.max(max, cnt);
		}
		System.out.println(max);
    }
    static int bfs(int x, int y, int height) {
		Queue<int[]> q = new LinkedList<>();
		q.add(new int[]{x,y});
		checked[x][y] = true;
		
		while(!q.isEmpty()) {
			int[] pos = q.poll();
			int px = pos[0];
			int py = pos[1];
			
			for(int i=0; i<4; i++) {
				int nx = px +dx[i];
				int ny = py +dy[i];
				
				if(nx<0 || ny<0 || nx>n-1 || ny >n-1) continue;
				if(checked[nx][ny]) continue;
				if(map[nx][ny]> height) {
					checked[nx][ny] = true;
					q.add(new int[] {nx,ny});
				}
			}
		}
		return 1;
    }}