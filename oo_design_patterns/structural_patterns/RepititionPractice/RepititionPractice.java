interface JsonLogger1 {
    void logMessage(String message);
}

class XmlLogger1 {
    public void log(String xmlMessage) {
        System.out.println(xmlMessage);
    }
}

class LoggerAdapter1 implements JsonLogger1 {
    private final XmlLogger1 xmlLogger1;

    public LoggerAdapter1(XmlLogger1 xmlLogger1) {
        this.xmlLogger1 = xmlLogger1;
    }

    @Override
    public void logMessage(String message) {
        xmlLogger1.log(message);
    }
}