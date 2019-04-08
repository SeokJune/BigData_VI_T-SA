/**
 * @KeywordCount
 * @Title: 드라이버 클래스(맵과 리듀스를 등록하는 일 수행)
 * @author: Lee_yun_Hyuck
 * @Create_at: 2019-04-06
 * @Modifier: Lee_yun_Hyuck
 * @Modify_on: 2019-04-09
 * @text: 주석 추가, 클래스명 변경
 */
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;

public class KeywordCount {
	public static void main(String[] args) throws Exception {
    	//초기 환경 설정을 해주기 위한 Configuration객체 생성. 
        Configuration conf = new Configuration();
        //입, 출력에 대한 파일 경로가 입력이 되지 않았을 경우. 오류 문구.
        if (args.length != 2) {
            System.out.println("Usage: KeywordCount <input> <output>");
            System.exit(2);
            ;
        }
        //맵리듀스 잡을 실행하기 위한 잡 객체 생성
        @SuppressWarnings("deprecation")
		Job job = new Job(conf, "KeywordCount");
        
       //WordCount.class에 드라이버 정보가 들어 있으므로 맵리듀스 잡에서 사용하는 라이브러리 파일지정.
        //맵과 리듀스에 맞는 클래스 지정.
        job.setJarByClass(KeywordCount.class);
        job.setMapperClass(KeywordCountMapper.class);
        job.setReducerClass(KeywordCountReducer.class);
        
        //job에서 사용할 맵, 리듀스 클래스 설정  
        job.setInputFormatClass(TextInputFormat.class);
        job.setOutputFormatClass(TextOutputFormat.class);
        
        //맵,리듀스 모두 입,출력 데이터가 텍스트 파일이므로 다음과 같이 설정을 해준다. 
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);
        
        //입출력 경로 지정
        //addInputPath을 통해 여러 파일 사용 가능.
        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));
        
        //잡 실행
        job.waitForCompletion(true);
    }
}
