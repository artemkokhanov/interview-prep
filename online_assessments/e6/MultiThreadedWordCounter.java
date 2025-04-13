import java.io.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.Collectors;

public class MultithreadedFileProcessor {
    // Thread-safe map to store unique word counts per line
    private static final ConcurrentHashMap<Integer, Integer> lineUniqueWordCounts = new ConcurrentHashMap<>();

    public static void countUniqueWordsConcurrently(Map<Integer, String> lines, int numThreads)
            throws InterruptedException, ExecutionException {
        // Create a fixed thread pool
        ExecutorService executor = Executors.newFixedThreadPool(numThreads);

        // List to keep track of Future objects
        List<Future<?>> futures = new ArrayList<>();

        // Submit a task for each line
        for (Map.Entry<Integer, String> entry : lines.entrySet()) {
            int lineNumber = entry.getKey();
            String textLine = entry.getValue();

            Future<?> future = executor.submit(() -> {
                countUniqueWords(lineNumber, textLine);
            });
            futures.add(future);
        }

        // Wait for all tasks to finish
        for (Future<?> future : futures) {
            future.get(); // ensures each task is complete
        }

        // Shutdown the pool
        executor.shutdown();
    }

    public static void countUniqueWords(int lineNumber, String textLine) {
        // Convert to lowercase and split on whitespace to get words
        String[] words = textLine.toLowerCase().split("\\s+");

        // Use a Set for uniqueness
        Set<String> uniqueWords = new HashSet<>(Arrays.asList(words));

        // Save the unique word count in our thread-safe map
        lineUniqueWordCounts.put(lineNumber, uniqueWords.size());
    }

    public static void main(String[] args) throws IOException, InterruptedException, ExecutionException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        // Read number of lines
        int numberOfLines = Integer.parseInt(bufferedReader.readLine().trim());
        Map<Integer, String> lines = new HashMap<>();

        // Read lines from standard input
        String line;
        int i = 1;
        while (i <= numberOfLines && (line = bufferedReader.readLine()) != null) {
            line = line.trim();
            if (!line.isEmpty()) {
                lines.put(i++, line);
            }
        }

        // Read number of threads
        int numberOfThreads = Integer.parseInt(bufferedReader.readLine().trim());

        // Track active threads before starting parallel computation
        int initialThreadCount = Thread.activeCount();

        // Perform the parallel processing
        countUniqueWordsConcurrently(lines, numberOfThreads);

        // Track active threads after tasks have started
        int duringThreadCount = Thread.activeCount();

        // Determine if multiple threads were used
        boolean usesThreads = (duringThreadCount - initialThreadCount) > 0;
        if (!usesThreads) {
            throw new IllegalStateException("Test Failed: The solution does not use threads for parallel computation.");
        }

        // Print the results sorted by line number
        List<String> results = lineUniqueWordCounts.entrySet()
                .stream()
                .sorted(Map.Entry.comparingByKey())
                .map(entry -> "Line " + entry.getKey() + " unique word count: " + entry.getValue())
                .collect(Collectors.toList());

        results.forEach(System.out::println);
        bufferedReader.close();
    }
}
