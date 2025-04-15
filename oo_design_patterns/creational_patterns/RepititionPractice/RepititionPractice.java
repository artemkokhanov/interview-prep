class RepititionPractice {
    private static volatile RepititionPractice INSTANCE = null;

    private RepititionPractice() {
    }

    public static RepititionPractice getInstance() {
        if (INSTANCE == null) {
            synchronized (RepititionPractice.class) {
                if (INSTANCE == null) {
                    INSTANCE = new RepititionPractice();
                }
            }
        }
        return INSTANCE;
    }
}