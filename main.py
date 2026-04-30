import flet as ft

async def main(page : ft.Page):
    page.title = "Chess"
    page.window.width = 650
    page.window.height = 650
    page.window.minimizable = False
    page.window.maximizable = False
    page.window.always_on_top = True

    await page.window.center()



    board_view = ft.GridView(
        width=550,
        runs_count=8,
        run_spacing=5,
        controls=[]
    )
    

    def show_board():
        for row in range(8):
            for col in range(8):
                color = ft.Colors.WHITE_60 if (row + col) % 2 == 0 else ft.Colors.BROWN
            
                board_view.controls.append(
                    ft.Container(
                        content=ft.Text(f""),
                        width=60,
                        height=60,
                        bgcolor=color,
                        alignment=ft.Alignment.CENTER
                    )
                )
            
            
    show_board()

    page.add(
        ft.Row([
            board_view
        ], alignment=ft.MainAxisAlignment.CENTER)
    )

ft.run(main=main)