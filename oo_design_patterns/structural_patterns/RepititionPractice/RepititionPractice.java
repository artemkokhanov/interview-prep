//interface JsonLogger {
//    void logMessage(String message);
//}
//
//class LoggerAdapter implements JsonLogger {
//    private final XmlLogger xmlLogger;
//
//    public LoggerAdapter(XmlLogger xmlLogger) {
//        this.xmlLogger = xmlLogger;
//    }
//
//    public void logMessage(String message) {
//        xmlLogger.log(message);
//    }
//}
//
//class XmlLogger {
//    public void log(String message) {
//        System.out.println(message);
//    }
//}
//
//class RepititionMain {
//    public static void main(String[] args) {
//        XmlLogger xmlLogger = new XmlLogger();
//
//        JsonLogger logger = new LoggerAdapter(xmlLogger);
//
//        logger.logMessage("<message>hello</message>");
//    }
//}