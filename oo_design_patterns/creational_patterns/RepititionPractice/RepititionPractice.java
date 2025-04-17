class ReptitionPractice {
    private static volatile ReptitionPractice INSTANCE = null;

    private ReptitionPractice() {}

    public static ReptitionPractice getInstance() {
        if (INSTANCE == null) {
            synchronized (ReptitionPractice.class) {
                if (INSTANCE == null) {
                    INSTANCE = new ReptitionPractice();
                }
            }
        }
        return INSTANCE;
    }
}