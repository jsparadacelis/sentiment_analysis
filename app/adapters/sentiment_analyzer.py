import abc


class AbstractSentimentAnalyzer(abc.ABC):

    @abc.abstractmethod
    def analyze_text(text: str) -> str:
        raise NotImplementedError


class FakeSentimentAnalyzer(AbstractSentimentAnalyzer):

    def analyze_text(text: str) -> str:
        return "Just an example"
