import re
import traceback

from . import logger


class SupportString(object):
    @classmethod
    def get_cate_char_by_first(cls, title):  # get_first
        value = ord(title[0].upper())
        if ord('가') <= value < ord('나'): return '가'
        if ord('나') <= value < ord('다'): return '나'
        if ord('다') <= value < ord('라'): return '다'
        if ord('라') <= value < ord('마'): return '라'
        if ord('마') <= value < ord('바'): return '마'
        if ord('바') <= value < ord('사'): return '바'
        if ord('사') <= value < ord('아'): return '사'
        if ord('아') <= value < ord('자'): return '아'
        if ord('자') <= value < ord('차'): return '자'
        if ord('차') <= value < ord('카'): return '차'
        if ord('카') <= value < ord('타'): return '카'
        if ord('타') <= value < ord('파'): return '타'
        if ord('파') <= value < ord('하'): return '파'
        if ord('하') <= value < ord('힣'): return '하'
        return '0Z'
    

    @classmethod
    def is_include_hangul(cls, text):
        try:
            hanCount = len(re.findall(u'[\u3130-\u318F\uAC00-\uD7A3]+', text))
            return hanCount > 0
        except:
            return False

    @classmethod
    def language_info(cls, text):
        try:
            text = text.strip().replace(' ', '')
            all_count = len(text)
            han_count = len(re.findall('[\u3130-\u318F\uAC00-\uD7A3]', text))
            eng_count = len(re.findall('[a-zA-Z]', text))
            etc_count = len(re.findall('[0-9]', text))
            etc_count += len(re.findall('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》：]', text))
            
            han_percent = int(han_count * 100 / (all_count-etc_count))
            eng_percent = int(eng_count * 100 / (all_count-etc_count))
            return (han_percent, eng_percent)
        except Exception as e: 
            logger.error(f"Exception:{str(e)}")
            logger.error(traceback.format_exc())
            return False

    @classmethod
    def remove_special_char(cls, text):
        return re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》：]', '', text)

