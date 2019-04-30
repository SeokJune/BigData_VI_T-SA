/**
 * @HashtagCount
 * @Title: 드라이버 클래스(맵과 리듀스를 등록하는 일 수행)
 * @author: Lee_yun_Hyuck
 * @Create_at: 2019-04-28
 */

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;


public class HashtagCount {
	public static void main(String[] args) throws Exception {
		//하둡 실행(hdfs-site, core-site)에 필요한 conf 객체 생성
		Configuration conf = new Configuration();
		//잡 실행을 위한 잡 객체 생성
		Job job = Job.getInstance(conf, "HashtagCount");
		//잡 실행에 필요한 사용자 라이브러리 파일 지정
		job.setJarByClass(HashtagCount.class);
		//잡에서 사용할 클래스들 설정
		job.setMapperClass(HashtagCountMapper.class);
		job.setCombinerClass(HashtagCountReducer.class);
		job.setReducerClass(HashtagCountReducer.class);
		//매퍼와 리듀서 클래스의 출력 데이터의 키와 값 타입 설정
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(IntWritable.class);
		//입출력 데이터 경로 설정.
		//첫 번째 인자는 입력 파라미터, 두 번째 인자는 출력 파라미터
		FileInputFormat.addInputPath(job, new Path(args[0]));
		FileOutputFormat.setOutputPath(job, new Path(args[1]));
		//실행에 필요한 경로와 같은 깂들이 정상적으로 들어간다면, 잡 실행
		System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
