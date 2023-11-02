from handlers.add_address import add_address
from handlers.add_birthday import add_birthday
from handlers.add_contact import add_contact
from handlers.add_email import add_email
from handlers.add_note import add_note
from handlers.add_tag_to_note import add_tag_to_note
from handlers.birthdays import birthdays
from handlers.delete_address import delete_address
from handlers.delete_note_by_title import delete_note_by_title
from handlers.delete_tag_from_note import delete_tag_from_note
from handlers.edit_address import edit_address
from handlers.edit_birthday import edit_birthday
from handlers.edit_contact import edit_contact
from handlers.edit_email import edit_email
from handlers.edit_name import edit_name
from handlers.edit_note_text import edit_note_text
from handlers.edit_note_title import edit_note_title
from handlers.find_notes_by_tags import find_notes_by_tags
from handlers.find_notes_by_title import find_notes_by_title
from handlers.help_info import help_info
from handlers.search_email import search_email
from handlers.search import search
from handlers.show_all import show_all
from handlers.show_birthday import show_birthday
from handlers.show_phone import show_phone
from handlers.sort_by_tag import sort_by_tag

handlers = {
    "add_address": add_address,
    "add_birthday": add_birthday,
    "add_contact": add_contact,
    "add_email": add_email,
    "add_note": add_note,
    "add_tag_to_note": add_tag_to_note,
    "birthdays": birthdays,
    "delete_address": delete_address,
    "delete_note_by_title": delete_note_by_title,
    "delete_tag_from_note": delete_tag_from_note,
    "edit_address": edit_address,
    "edit_birthday": edit_birthday,
    "edit_contact": edit_contact,
    "edit_email": edit_email,
    "edit_name": edit_name,
    "edit_note_text": edit_note_text,
    "edit_note_title": edit_note_title,
    "find_notes_by_tags": find_notes_by_tags,
    "find_notes_by_title": find_notes_by_title,
    "help_info": help_info,
    "search_email": search_email,
    "search": search,
    "show_all": show_all,
    "show_birthday": show_birthday,
    "show_phone": show_phone,
    "sort_by_tag": sort_by_tag,
}
