from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance: Queue):
    file_lines = [
        instance.search(i)['nome_do_arquivo'] for i in range(len(instance))]
    if path_file not in file_lines:
        data = txt_importer(path_file)
        meta_data = {
            'nome_do_arquivo': path_file,
            'qtd_linhas': len(data),
            'linhas_do_arquivo': data
        }
        instance.enqueue(meta_data)
        print(meta_data, file=sys.stdout)
    return None


def remove(instance):
    if len(instance) == 0:
        print('Não há elementos', file=sys.stdout)
        return None
    file = instance.dequeue()
    print(
        f'Arquivo {file["nome_do_arquivo"]} removido com sucesso',
        file=sys.stdout)


def file_metadata(instance, position):
    try:
        queue = instance.search(position)
        print(queue, file=sys.stdout)
    except IndexError:
        print('Posição inválida', file=sys.stderr)
