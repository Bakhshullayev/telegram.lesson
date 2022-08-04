from loader import dp
from aiogram.types import ContentType, Message
from pathlib import Path

dowload_path = Path().joinpath("downloads", "categories")
dowload_path.mkdir(parents=True, exist_ok=True)


@dp.message_handler(content_types=ContentType.DOCUMENT)
async def get_document(message: Message):
    await message.document.download(destination=dowload_path)
    doc_id = message.document.file_id
    await message.answer("Siz hujjat yubordingiz"
                         "file_id", doc_id)


@dp.message_handler(content_types=ContentType.VIDEO)
async def get_video(message: Message):
    await message.video.download(destination=dowload_path)

    await message.answer("Siz video yubordingiz", message.video.file_id)

''
@dp.message_handler(content_types=ContentType.PHOTO)
async def get_photo(message: Message):
    await message.photo[-1].download(destination=dowload_path)
    await message.answer("Siz rasm yubordingiz", message.photo[-1].file_id)
