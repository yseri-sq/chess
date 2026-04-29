import flet as ft

async def main(page : ft.Page):
    page.title = "Chess"
    page.window.width = 650
    page.window.height = 650
    page.window.minimizable = False
    page.window.maximizable = False
    page.window.always_on_top = True

    await page.window.center()

    

ft.run(main=main)