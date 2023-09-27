"""搜索引擎

"""

class SearchEngineBase:
    """搜索引擎基础类"""
    def __init__(self):
        pass

    def add_corpus(self, file_path):
        """负责读取文件内容，将文件路径作为 ID，连同内容一起送到 process_corpus 中。"""
        with open(file_path, 'r', encoding=str) as fin:
            text = fin.read()
        self.process_corpus(file_path, text)

    def process_corpus(self, file_path, text):
        """需要对内容进行处理，然后文件路径为 ID ，将处理后的内容存下来。处理后的内容，就叫做索引（index）。"""
        raise Exception('process_corpus not implemented.')

    def search(self, query):
        """给定一个询问，处理询问，再通过索引检索，然后返回。"""
        raise Exception('search not implemented.')


class SimpleEngine(SearchEngineBase):
    """简单搜索引擎"""
    def __init__(self):
        super(SimpleEngine, self).__init__()
        self.__id_to_texts = {}

    def process_corpus(self, file_path, text):
        self.__id_to_texts[file_path] = text

    def search(self, query):
        results = []
        for file_path, text in self.__id_to_texts.items():
            if query in text:
                results.append(file_path)
        return results


def main(search_engine):
    """查询"""
    for file_path in ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt']:
        search_engine.add_corpus(file_path)

    while True:
        query = input()
        results = search_engine.search(query)
        print(f'found {len(results)} result(s):')
        for result in results:
            print(result)


if __name__ == '__main__':
    search_engine = SimpleEngine()
    main(search_engine)
