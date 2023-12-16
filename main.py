import asyncio

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

stickerpack = [
    r"CAACAgIAAxkBAAEIfWBkL-mba2XI9A8YDCnq9RfpaLvP7AACLhAAAlrQgUgIvOZTf2b2xi8E",
    r"CAACAgIAAxkBAAEIfWJkL-m0mAHAGXOjq8RyTXL_KJVBpQACqhAAAol8gEh_KDETWzwMoS8E",
    r"CAACAgIAAxkBAAEIfWRkL-m3FgzL3nfml_hIVJmv9jte_gACZhMAAkSZgEic77gNT5yfcy8E",
    r"CAACAgIAAxkBAAEIfWZkL-m5_sTAGkxw0jbZea-X6-VewQACwhMAAhFPgUitYgUXV6XhNS8E",
    r"CAACAgIAAxkBAAEIfWhkL-m7K56RLCP50seBOrMs_YNNmAAC-Q8AAkizgUg1oPltMoqHDC8E",
    r"CAACAgIAAxkBAAEIfWpkL-m9CxBagEu7pvs0VhCoK8xMLgACvREAAj6deUhXRIpi8ND4lS8E",
    r"CAACAgIAAxkBAAEIfWxkL-m_6JQqNlX5swO2e7lpe34JWgACthUAAlnPgUgr9A1ygKcCRy8E",
    r"CAACAgIAAxkBAAEIfW5kL-nCq8wxCX8pJTZRh_aP7-I7XgAC0xAAAnxFgUiGdee3rCqq8S8E",
    r"CAACAgIAAxkBAAEIfXBkL-nENNa4wvbhMd8hIxftdjVC9AACyRAAAj9igUhZh24PjIvL3S8E",
    r"CAACAgIAAxkBAAEIfXJkL-nGPYw2Sanz5ExyNQvC0wd3RQACVxEAAgg9gEhH7Fkjt--PiS8E",
    r"CAACAgIAAxkBAAEIfXRkL-nIPXjFxyKBWWw41FOpVKalXQACWBEAAq3FeUgci-WzxbxyKS8E",
    r"CAACAgIAAxkBAAEIfXZkL-nJX12GlUqfziSou3N56YJ-oAAC7BEAAgrKeUirYZDwzJ0lPS8E",
    r"CAACAgIAAxkBAAEIfXhkL-nL7LLRaOneouaSc_J0Xun1-wACnRAAAqfteUjaUWYZjYhLHy8E",
    r"CAACAgIAAxkBAAEIfXpkL-nNnEp-UNTty28JmRF6YLsifQADEgAC5GaASGHKEVWl9aL-LwQ",
    r"CAACAgIAAxkBAAEIfXxkL-nQFBujEtHzpiFjbMJM1ezQFAACvBEAAk9kgEincSdKyTbwii8E",
    r"CAACAgIAAxkBAAEIfX5kL-nSHiZfF-i5RZvTwo1a2e1rnwACCA8AAh7deUjP85EpAAEqSLgvBA",
    r"CAACAgIAAxkBAAEIfYBkL-nUa_xDBL0_PpbwIVdU6Z4_9AACwxAAAiT-gUg4rv5-pK24Di8E",
    r"CAACAgIAAxkBAAEIfYJkL-nW7-ttW52Xj07PC2pfwvPh5QACehMAApkzeEiF9LtCQAXLBS8E",
    r"CAACAgIAAxkBAAEIfYRkL-nY5A1PE_Hqr3-1I-82uOqZAQACmhAAAg2zgEimqztzXZrPaC8E",
    r"CAACAgIAAxkBAAEIfYZkL-naZYLKk60W8s-KOX-oJHXgZgACVBIAAnvmgUi0ZiwT3vKe-C8E",
    r"CAACAgIAAxkBAAEIfYhkL-ncX_90Jpg7JLIlS4PM7Gm5_gACzhUAAo0NgUiRVq5vwqu_ci8E",
    r"CAACAgIAAxkBAAEIfYpkL-neaCpaMa8JCx2IV9k6vNbOmgACwhAAAsS0eUi7TAh9IQEofy8E",
    r"CAACAgIAAxkBAAEIfYxkL-nh31hPJUIQJqMjGVXk3keyGQACoA8AAqa1eEiMC9j3RVeMQi8E",
    r"CAACAgIAAxkBAAEIfY5kL-nj_Y3-2ei3ZsxGfhcnFPfkrwAClREAAlFgeEiCBWpR-era_i8E",
    r"CAACAgIAAxkBAAEIfZBkL-nlz3Cm3F4krustY_zrHqyCFwACihYAAsSUgUizj25gJ7ZOhS8E",
    r"CAACAgIAAxkBAAEIfZJkL-nn2CQMZkPvQqBGdnBUgC9n5wACKBAAAobFgUjkFnLCWmwPRS8E",
    r"CAACAgIAAxkBAAEIfZRkL-nplvGcYXpuOUkg81FStlbAgQACKRAAAjTkgEgtLWdO0MDWWy8E",
    r"CAACAgIAAxkBAAEIfZZkL-ns9NwAAd2kHBQkHySZrgJWUnIAAtcVAAISsoFIF-MQVAiJUPcvBA",
    r"CAACAgIAAxkBAAEIfZhkL-nuYB0JyYp-7lTnhRIXcNWAlAACJxEAAt4reEiDr-qYCekYKy8E",
    r"CAACAgIAAxkBAAEIfZpkL-nxR1tR5tqdRDsobPPvEbfcYAACkxEAAi7GgUjJo6jLrKEe9i8E",
    r"CAACAgIAAxkBAAEIfZxkL-n0FoM1tP8XiubHArVUkyN-zgACTg8AAjtZgEiGGyY2T1s96y8E",
    r"CAACAgIAAxkBAAEIfZ5kL-n4B9AAAcuLeS57LUl3b6STIcUAAtERAAKC8oFIfQ28on4X3tEvBA",
    r"CAACAgIAAxkBAAEIfaBkL-n7bNuUxJXFi_qsJNwsvc6O7AACqBEAAgqMgEjomgZtph1z3S8E",
    r"CAACAgIAAxkBAAEIfaJkL-n-6cAjoBiAdTYpM3tlCynK-gACaxQABIFIAc57sPSCC-EvBA",
    r"CAACAgIAAxkBAAEIfaRkL-oAAdbZ1mvju14TZo9BNq9PpgsAAgISAAK-aIFI4MNL8bnEsCEvBA",
    r"CAACAgIAAxkBAAEIfaZkL-oFTuAKB5hgS2UlmGLaHTTThgACzhIAAhphgEiiE2_W3aBlgS8E",
    r"CAACAgIAAxkBAAEIfahkL-oIGzuvVPXFyMTO6xoiqjWepwACfxUAAiOIgUi2qXTmARTYMS8E",
    r"CAACAgIAAxkBAAEIfapkL-oLIPvQ2bm8yUSa1Kdc1uWQagACahUAAh-ngUgWYUx1XJjK2C8E",
    r"CAACAgIAAxkBAAEIfaxkL-oOBSOSGNodRVn7rei7H_QhMgAC3hMAAsI9gEirY_tCgg80Ny8E",
    r"CAACAgIAAxkBAAEIfa5kL-oRjMwFLsic9AUClKy8Ans5lQACghEAAuGqgEhaQjhEUXHk-S8E",
    r"CAACAgIAAxkBAAEIfbBkL-oTJzsGofBaZBaWL3El4oWULQAChxIAAuYWgEjOLbzKOt36-y8E"
]

timespaces = [1, 0.8, 1, 0.8, 0.7, 1, 0.7, 2, 1, 0.8, 0.8, 0.7, 1, 3, 1.5, 0.3, 0.3, 0.1, 0.3, 0.3, 0.1,
              0.4, 0.4, 0.3, 1.5, 0.1, 0.3, 0.1, 0.3, 0.1, 0.1, 0.08, 0.5, 0.07,
              0.1, 0.1, 0.1, 0.07, 0.07, 0.1, 1.5]

API_TOKEN = '5610114981:AAGoNqTpOLOfkzPVye5uRc_CPQ82_j0u8LY'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

mykb = InlineKeyboardMarkup(row_width=1)
mybt = InlineKeyboardButton(text="Пошумим, блять!", callback_data="rap")
mykb.add(mybt)

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer_sticker(r'CAACAgIAAxkBAAEIfqxkMDe93f5oiPqMbh0vea4iDMs3xgACwxIAAjT4gEgX7geJP3zxZC8E')
    await message.answer("Вы готовы?", reply_markup=mykb)

@dp.callback_query_handler(text="rap")
async def rap(query: types.CallbackQuery):
#    print("quary reached\n")
    i = 0
    for i in range(0, len(stickerpack)):
#        print(i, end="\n")
        await asyncio.sleep(timespaces[i])
        await query.message.answer_sticker(stickerpack[i])

    await asyncio.sleep(2.5)
    await query.message.answer_sticker(r'CAACAgIAAxkBAAEIfqxkMDe93f5oiPqMbh0vea4iDMs3xgACwxIAAjT4gEgX7geJP3zxZC8E')
    await query.message.answer("Вы готовы?", reply_markup=mykb)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
