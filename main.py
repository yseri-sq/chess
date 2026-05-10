import flet as ft
from Board import create_Board, FIGURES

async def main(page : ft.Page):
    page.title = "Chess"
    page.window.width = 650
    page.window.height = 650
    page.window.minimizable = False
    page.window.maximizable = False
    page.window.always_on_top = True

    # await page.window.center()



    board_view = ft.GridView(
        width=550,
        runs_count=8,
        run_spacing=0,
        spacing=0,
    )
    
    board = create_Board() #matrix
    
    select_figure = None
    
    
    # def check_field(e):
    #     row = e.control.data["row"]
    #     col = e.control.data["col"]
    #     print({row}, {col})
    
    
    def move(e):
        nonlocal select_figure
        
        row = e.control.data["row"]
        col = e.control.data["col"]
        
        if select_figure is None:
            if board[row][col] != 0:
                select_figure = e.control.data
                e.control.border = ft.border.all(2, ft.Colors.GREEN)
                page.update()
                
        else:
            old_row = select_figure["row"]
            old_col = select_figure["col"]
            
            board[row][col] = board[old_row][old_col]
            board[old_row][old_col] = 0
            
            select_figure = None
            show_board()
            page.update()
            
        # print(board)

    def show_board():
        board_view.controls.clear()
        for row in range(8):
            for col in range(8):
                figure_val = board[row][col]
                
                bg_color = ft.Colors.WHITE_60 if (row + col) % 2 == 0 else ft.Colors.BROWN
                figure_color = ft.Colors.BLACK if figure_val < 0 else ft.Colors.WHITE
            
                board_view.controls.append(
                    ft.Container(
                        content=ft.Text(
                            FIGURES.get(figure_val, ""),
                            size=40,
                            color=figure_color,
                            weight=ft.FontWeight.BOLD
                        ),
                        width=60,
                        height=60,
                        bgcolor=bg_color,
                        alignment=ft.Alignment.CENTER,
                        data={"row": row, "col": col}, #интерактивный объект
                        on_click=move
                    )
                )
            
            
    show_board()

    page.add(
        ft.Row([
            board_view
        ], alignment=ft.MainAxisAlignment.CENTER)
    )

ft.run(main=main)