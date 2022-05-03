import sys
from pathlib import Path

JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []

AVI_VIDEO = []
MP4_VIDEO = []
MOV_VIDEO = []
MKV_VIDEO = []

DOC = []
DOCX = []
TXT = []
PDF = []
XLSX = []
PPTX = []

MP3_AUDIO = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []

ZIP_ARCHIVES = []
GZ_ARCHIVES = []
TAR_ARCHIVES = []

OTHER = []

REGISTER_EXTENSIONS = {
    'JPEG': JPEG_IMAGES,
    'PNG': PNG_IMAGES,
    'JPG': JPG_IMAGES,
    'SVG': SVG_IMAGES,
    'AVI': AVI_VIDEO,
    'MP4': MP4_VIDEO,
    'MOV': MOV_VIDEO,
    'MKV': MKV_VIDEO,
    'DOC': DOC,
    'DOCX': DOCX,
    'TXT': TXT,
    'PDF': PDF,
    'XLSX': XLSX,
    'PPTX': PPTX,
    'MP3': MP3_AUDIO,
    'OGG': OGG_AUDIO,
    'WAV': WAV_AUDIO,
    'AMR': AMR_AUDIO,
    'ZIP': ZIP_ARCHIVES,
    'GZ': GZ_ARCHIVES,
    'TAR': TAR_ARCHIVES
}

FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()


def get_extension(filename: str) -> str:
    # превращаем расширение файла в название папки .jpg -> JPG
    return Path(filename).suffix[1:].upper()


def scan(folder: Path) -> None:
    for item in folder.iterdir():
        # Если это папка то добавляем ее в список FOLDERS и преходим к следующему элементу папки
        if item.is_dir():
            # проверяем, чтобы папка не была той в которую мы складываем уже файлы
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'OTHER'):
                FOLDERS.append(item)
                #  сканируем эту вложенную папку - рекурсия
                scan(item)
            #  перейти к следующему элементу в сканируемой папке
            continue

        #  Пошла работа с файлом
        ext = get_extension(item.name)  # взять расширение
        fullname = folder / item.name  # взять полный путь к файлу
        if not ext:  # если у файла нет расширения добавить к неизвестным
            OTHER.append(fullname)
        else:
            try:
                # взять список куда положить полный путь к файлу
                container = REGISTER_EXTENSIONS[ext]
                EXTENSIONS.add(ext)
                container.append(fullname)
            except KeyError:
                # Если мы не регистрировали расширение в REGISTER_EXTENSIONS, то добавить в другое
                UNKNOWN.add(ext)
                OTHER.append(fullname)


if __name__ == '__main__':
    folder_for_scan = sys.argv[1]
    print(f'Start in folder {folder_for_scan}')

    scan(Path(folder_for_scan))
