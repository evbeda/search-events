from abc import abstractmethod


class GetContextMixin:

    @abstractmethod
    def get_context(self):
        pass
