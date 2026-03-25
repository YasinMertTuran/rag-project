package mu.cse.rag.clean;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class JsonCorpusLoader {
    public static List<Chunk> loadCorpus(String filePath) {
        List<Chunk> corpus = new ArrayList<>();
        try {
            String content = new String(Files.readAllBytes(Paths.get(filePath)), StandardCharsets.UTF_8); //Reads file
            content = content.trim(); //Clears parentheses
            if (content.startsWith("[")) content = content.substring(1);
            if (content.endsWith("]")) content = content.substring(0, content.length() - 1);

            String[] rawObjects = content.split("(?<=\\}),\\s*"); //Splits by }, while keeping the }
            
            for (String obj : rawObjects) { //Iterate over each JSON object
                obj = obj.trim(); //Removes whitespaces
                if (obj.isEmpty()) continue;

                String docId = extractValue(obj, "docId"); //Extract values using regex
                String chunkIdStr = extractValue(obj, "chunkId"); //chunkId is string in JSON
                String title = extractValue(obj, "title"); //Extract title
                String text = extractValue(obj, "text"); //Extract text
                
                if (docId != null && chunkIdStr != null) { //If found something
                    try {
                        int id = Integer.parseInt(chunkIdStr.replaceAll("[^0-9]", "")); //chunkId to int
                        corpus.add(new Chunk(docId, id, title, text));
                    } catch (Exception e) { 
                        System.err.println(e.getMessage());
                    }
                }
            }
            
        } catch (IOException e) { //File read error
            System.err.println(e.getMessage());
        }
        return corpus;
    }

    private static String extractValue(String jsonObject, String key) { //Key values extractor
        try {
            Pattern pattern = Pattern.compile("\"" + key + "\"\\s*:\\s*(\"[^\"]*\"|\\d+)");
            Matcher matcher = pattern.matcher(jsonObject);
            
            if (matcher.find()) {
                String val = matcher.group(1);
                if (val.startsWith("\"")) {
                    return val.substring(1, val.length() - 1); //Remove quotes
                }
                return val; //Return directly if it's a number
            }
        } catch (Exception e) {
            System.err.println("extractValue error for key=" + key + ": " + e.getMessage());
            return null;
        }
        return null; //Return null if not found
    }
}