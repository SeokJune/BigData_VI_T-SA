/**
 * @KeywordCountMapper
 * @Title: 매퍼 클래스(맵에서 선별한 데이터(key, value)를 같은 키를 기준으로 더하는 작업 수행 )
 * @author: Lee_yun_Hyuck
 * @Create_at: 2019-04-06
 * @Modifier: Lee_yun_Hyuck
 * @Modify_on: 2019-04-09
 * @text: 주석 추가, 클래스 명 변경
 */

import java.io.IOException;
import java.util.Iterator;
import java.util.List;
import java.util.StringTokenizer;
 
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

import kr.co.shineware.nlp.komoran.constant.DEFAULT_MODEL;
import kr.co.shineware.nlp.komoran.core.Komoran;
import kr.co.shineware.nlp.komoran.model.KomoranResult;
 
public class KeywordCountMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
    private final static IntWritable one = new IntWritable(1);
    private Text word = new Text();
 
    @Override
    protected void map(LongWritable key, Text value, Mapper<LongWritable, Text, Text, IntWritable>.Context context)
            throws IOException, InterruptedException {
        StringTokenizer itr = new StringTokenizer(value.toString(), " \t\n\r,.'\"-=%…()[]{}“▷+ⓒ!?:;#\'");
        
        
        while(itr.hasMoreTokens()) {
        	  String token = itr.nextToken();
        	  Komoran komoran = new Komoran(DEFAULT_MODEL.FULL);
        	  komoran.setUserDic("/home/vi/eclipse-workspace/KeywordCount/src/dic.user");
            KomoranResult analyzeResultList = komoran.analyze(token);            
            List<String> tokens = analyzeResultList.getMorphesByTags("NP","NNP","NNG");
            Iterator<String> itrs = tokens.iterator();
        	  
            while(itrs.hasNext()) {
            String ktr = itrs.next().trim();
            if(ktr.getBytes().length > (byte)3 && ktr.getBytes().length < (byte)16) {
                word.set(ktr);
                context.write(word, one);
            	}
            }
        }
    }
}