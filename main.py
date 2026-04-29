import flet as ft

async def main(page : ft.Page):
    page.title = "Chess"
    page.window.width = 650
    page.window.height = 650
    page.window.minimizable = False
    page.window.maximizable = False
    # page.window.always_on_top = True

    await page.window.center()



    board_view = ft.GridView(
        width=550,
        runs_count=8,
        run_spacing=5,
        controls=[]
    )
    

    def show_board():
        cell = ft.Container(width=35, height=35, bgcolor=ft.Colors.WHITE)
        for i in range(64):
            board_view.controls.append(cell)
            
    show_board()

    page.add(
        ft.Row([
            board_view
        ], alignment=ft.MainAxisAlignment.CENTER)
    )

ft.run(main=main)