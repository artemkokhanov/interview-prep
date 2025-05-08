class RepititionPractice {
    private static volatile RepititionPractice uniqueInstance = null;

    private RepititionPractice() {

    }

    public static RepititionPractice getInstance() {
        if (uniqueInstance == null) {
            synchronized (RepititionPractice.class) {
                if (uniqueInstance == null) {
                    uniqueInstance = new RepititionPractice();
                }
            }
        }
        return uniqueInstance;
    }
}