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
import kr.co.shineware.nlp.komoran.model.Token;
 
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
            KomoranResult analyzeResultList = komoran.analyze(token);            
            List<Token> tokens = analyzeResultList.getTokenList();
            Iterator<Token> itrs = tokens.iterator();
            
            word.set(itrs.next().getMorph());
            context.write(word, one);
        }
    }
}