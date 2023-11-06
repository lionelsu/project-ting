from ting_file_management.queue import Queue


def report_word_ocurr(word, instance: Queue, include_content=False):
    word_occurrences_in_files = list()
    word = word.casefold()

    for file_index in (range(len(instance))):
        file_data = instance.search(file_index)['linhas_do_arquivo']
        lines_with_word = {
            line: content for line, content in enumerate(
                file_data) if word in content.casefold()}

        if lines_with_word:
            ocurrences_lines = [
                {"linha": line + 1, "conteudo": content}
                if include_content else {"linha": line + 1}
                for line, content in lines_with_word.items()]
            word_occurrences_in_files.append({
                "palavra": word,
                "arquivo": instance.search(file_index)['nome_do_arquivo'],
                "ocorrencias": ocurrences_lines
            })

    return word_occurrences_in_files


def exists_word(word, instance: Queue, include_content=False):
    return report_word_ocurr(word, instance, include_content)


def search_by_word(word, instance):
    return exists_word(word, instance, True)
