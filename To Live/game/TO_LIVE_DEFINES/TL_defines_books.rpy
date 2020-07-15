
init -1 python:

    #image dissolves that could possibly do a page flip effect... not currently used
    book_pageflip1 = ImageDissolve(im.Tile("images/00_books/book_pageflip1.jpg"), 1.5, 16)
    book_pageflip1b = ImageDissolve(im.Tile("images/00_books/book_pageflip1.jpg"), 1.5, 16, reverse=True)

    book_pageflip2 = ImageDissolve(im.Tile("images/00_books/book_pageflip2.jpg"), 1.5, 16)
    book_pageflip2b = ImageDissolve(im.Tile("images/00_books/book_pageflip2.jpg"), 1.5, 16, reverse=True)

    offscreentop = Position(ypos=0.0, yanchor=1.0)

init python:
    import renpy.store as store
    class Note(store.object):
        #defines a note, with a text to display, text alignment, text size,
        #an image to display at the bottom of the note (if any), and a font.
        def __init__(self, note_text, alignment, sz=gui.text_size, img=None, fnt=gui.text_font):
            self.note_text = note_text
            self.alignment = alignment
            self.sz = sz
            self.img = img
            self.fnt = fnt

    class Book(store.object):
        #defines a book, with a text to display, text alignment, text size, and a font.
        #probably should also define a book graphic (so different books can use different covers)
        def __init__(self, book_title, book_text, alignment, sz=gui.text_size, fnt=gui.text_font):
            self.book_title = book_title
            self.book_text = book_text #a LIST of texts, one for each page
            self.alignment = alignment
            self.sz = sz
            self.fnt = fnt

        def flip_prev(self):
            renpy.show("page flip_prev", at_list=[page_turning_alpha], layer='screens', zorder=100)
            global page_showing_left
            global page_showing_right
            page_showing_left -= 2
            page_showing_right -= 2
            renpy.restart_interaction

        #can the function also display the page turning animation, and change the text xzoom, then hide the text, show the new text with xzoom 0, then stretch it out to 1?
        def flip_next(self):
            renpy.show("page flip_next", at_list=[page_turning_alpha], layer='screens', zorder=100)
            global page_showing_left
            global page_showing_right
            page_showing_left += 2
            page_showing_right += 2
            renpy.restart_interaction

default page_showing_left = 0
default page_showing_right = 1
default closing = False
default book = "images/00_books/book_06.png"

image page flip_next:
    "images/00_books/page_0.png"
    pause 0.05
    "images/00_books/page_1.png"
    pause 0.05
    "images/00_books/page_2.png"
    pause 0.05
    "images/00_books/page_3.png"
    pause 0.05
    "images/00_books/page_4.png"
    pause 0.05
    "images/00_books/page_5.png"
    pause 0.05
    Null()

image page flip_prev:
    "images/00_books/page_5.png"
    pause 0.05
    "images/00_books/page_4.png"
    pause 0.05
    "images/00_books/page_3.png"
    pause 0.05
    "images/00_books/page_2.png"
    pause 0.05
    "images/00_books/page_1.png"
    pause 0.05
    "images/00_books/page_0.png"
    pause 0.05
    Null()

image page_left_opening: #cover opening over "book_pg_right.png"
    "images/00_books/book_00.png"
    pause 0.2
    "images/00_books/book_01.png"
    pause 0.15
    "images/00_books/book_02_cover.png"
    pause 0.1
    "images/00_books/book_03_cover.png"
    pause 0.08
    "images/00_books/book_04_cover.png"
    pause 0.06
    "images/00_books/book_05_cover.png"
    pause 0.04
    "images/00_books/book_pg_left.png"
image page_left_closing:
    on show:
        "images/00_books/book_05_cover.png"
        pause 0.07
        "images/00_books/book_04_cover.png"
        pause 0.07
        "images/00_books/book_03_cover.png"
        pause 0.07
        "images/00_books/book_02_cover.png"
        pause 0.07
        "images/00_books/book_01.png"
        pause 0.07
        "images/00_books/book_00.png"
image page_right_flat = "images/00_books/book_pg_right.png"

image book opening:
    contains:
        "images/00_books/book_pg_right.png"

    contains:
        "page_left_opening"

    xalign 0.5 yanchor 1.0 ypos 0
    ease 1.0 yanchor 0.0

image book closing:
    contains:
        "page_left_closing"

    xalign 0.5 yanchor 0.0 ypos 0
    ease 1.0 yanchor 1.0

transform book_appear:
    on show:
        xalign 0.5
        ypos 0 yanchor 1.0
        ease 1.0 yanchor 0.0
    on hide:
        xalign 0.5
        ypos 0 yanchor 0.0
        ease 1.0 yanchor 1.0

transform page_turning_alpha:
    alpha 0.0
    ease 0.15 alpha 1.0
    ease 0.15 alpha 0.0

#timings probably need to be adjusted...
transform page_right_squish_to_center: #turn the page, right side
    xanchor 0.0 xzoom 1.0
    linear 0.3 xzoom 0.0

transform page_right_unsquish: #turn to previous page, right side
    xanchor 0.0 xzoom 0.0
    linear 0.3 xzoom 1.0

transform page_left_squish_to_center: #turn the page, left side
    xanchor 1.0 xzoom 1.0
    linear 0.3 xzoom 0.0

transform page_left_unsquish: #turn to previous page, left side
    xanchor 1.0 xzoom 0.0
    linear 0.3 xzoom 1.0

screen book_open(book): #take parameters from a Book object

    on "show" action [SetVariable("closing", False), SetVariable("turning_prev", False), SetVariable("turning_next", False)]

    fixed at book_appear:
        add "page_right_flat" #the right side of the book has to be lower in the order
        #so that the left side of the book can cover it when it opens and closes

        vbox: #right side text
            area 995,190,490,700
            box_wrap True
            box_wrap_spacing 30
            spacing 20
            text str(book.book_text[page_showing_right]):
                color "#000"
                text_align book.alignment
                size book.sz
                font book.fnt
                line_spacing 20

        showif closing == True:
            add "page_left_closing"
        else:
            add "page_left_opening"

        vbox: #left side text
            area 365,190,490,700
            box_wrap True
            box_wrap_spacing 30
            spacing 20
            if closing != True:
                text str(book.book_text[page_showing_left]):
                    yalign 0.0
                    color "#000"
                    text_align book.alignment
                    size book.sz
                    font book.fnt
                    line_spacing 20

    hbox: #buttons to navigate the book
        xalign 0.49
        yalign 0.93
        spacing 50

        textbutton "<":
            text_color "#fff"
            text_hover_color gui.hover_color
            text_selected_color gui.selected_color
            selected False
            text_insensitive_color gui.insensitive_color
            sensitive page_showing_left != 0
            action [Function(book.flip_prev)]
            #can the function also display the page turning animation, and change the text xzoom, then hide the text, show the new text with xzoom 0, then stretch it out to 1?

        textbutton "X":
            text_color "#fff"
            text_hover_color gui.hover_color
            text_selected_color gui.selected_color
            selected False
            text_insensitive_color gui.insensitive_color
            action [SetVariable("closing", True), Return()]

        textbutton ">":
            text_color "#fff"
            text_hover_color gui.hover_color
            text_selected_color gui.selected_color
            selected False
            text_insensitive_color gui.insensitive_color
            sensitive len(book.book_text) > int(page_showing_right)+2
            action [Function(book.flip_next)]
            #can the function also display the page turning animation, and change the text xzoom, then hide the text, show the new text with xzoom 0, then stretch it out to 1?

transform note_appear: #rotate a bit as it comes in
    on show:
        xalign 0.5
        ypos -1520 rotate -80 xzoom 0.0
        ease .5 ypos -570 rotate renpy.random.randint(-5,5) xzoom 1.0
    on hide:
        xalign 0.5
        ease .5 ypos -1520 rotate 80 xzoom 0.0

screen note(note_object): #take parameters from a Note object
    fixed at note_appear:
        add "images/00_books/paper.png"
        vbox:
            area 690,150,545,765
            box_wrap True
            box_wrap_spacing 30
            spacing 20
            text str(note_object.note_text):
                color "#000"
                text_align note_object.alignment
                size note_object.sz
                font note_object.fnt
                line_spacing 20
                yalign 0.4
            add note_object.img xalign 0.5

        textbutton "X":
            text_color "#333"
            text_hover_color gui.hover_color
            text_selected_color gui.selected_color
            text_insensitive_color gui.insensitive_color
            action Return()
            xalign 0.65
            yalign 0.88
