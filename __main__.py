import os
import sys
import logging
from time import sleep
from markdown_test import md1

os.system(f"{sys.executable} -m pip install flet six plotly")

import flet
from flet import icons, theme, colors

LIGHT_SEED_COLOR = colors.CYAN_ACCENT
DARK_SEED_COLOR = colors.LIGHT_GREEN_ACCENT

logging.basicConfig(level=logging.INFO)


def main(page: flet.Page):

    # dialog function
    dlg = flet.AlertDialog(title=flet.Text("Hello, you!"), on_dismiss=lambda e: print("Dialog dismissed!"))

    def close_dlg(e):
        dlg_modal.open = False
        page.update()

    def open_dlg_modal(e):
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()

    dlg_modal = flet.AlertDialog(
        modal=True,
        title=flet.Text("Warning"),
        content=flet.Text("Do you really want to exit program?"),
        actions=[flet.TextButton("Yes", on_click=close_dlg), flet.TextButton("No", on_click=close_dlg)],
        actions_alignment=flet.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )

    # server info
    server_info = flet.ResponsiveRow(
        [
            flet.TextField(label="server_ip", value="127.0.0.1", border="underline", col={"xs": 8}),
            flet.TextField(label="server_port", value="9090", border="underline", col={"xs": 4}),
        ],
    )

    # state tab
    states = [
        flet.ResponsiveRow([flet.ElevatedButton("full width button", col={"xs": 12})]),
        flet.ResponsiveRow(
            [
                flet.TextField(label="adress", value="", border="underline", col={"xs": 4}),
                flet.TextField(label="database", value="", border="underline", col={"xs": 4}),
                flet.TextField(label="collection", value="", border="underline", col={"xs": 4}),
            ],
        ),
        flet.Container(
            content=flet.Row(
                [
                    flet.TextField(label="ip", value="127.0.0.1", width=150),
                    flet.TextField(label="border", value="9090", width=150, border="underline"),
                    flet.TextField(label="filled", value="9090", width=150, border="underline", filled=True),
                    flet.TextField(label="multiline", value="9090\n9090\n9090", width=150, multiline=True),
                    flet.TextField(label="password", value="9090", width=150, password=True, can_reveal_password=True),
                    flet.TextField(label="number keyboard", value="9090", width=150, keyboard_type="number"),
                    flet.TextField(label="phone keyboard", value="01022223333", width=150, keyboard_type="phone"),
                    flet.TextField(label="URL keyboard", value="https://w", width=150, keyboard_type="url"),
                ],
                wrap=True,
            ),
        ),
        flet.Text("Show state"),
        flet.Text("robot"),
    ]
    states.extend(list(flet.Text(f"fryer{i}") for i in range(50)))
    states.extend(list(flet.Text(f"add fryer{i}") for i in range(30)))
    state = flet.Container(content=flet.Column(states, scroll="auto"))

    # time tab
    settime_form = flet.ResponsiveRow(
        [
            flet.TextField(label="openwait_sec", value="", border="underline", col={"xs": 4, "sm": 2}),
            flet.TextField(label="closewait_sec", value="", border="underline", col={"xs": 4, "sm": 2}),
            flet.TextField(label="frying_sec", value="", border="underline", col={"xs": 4, "sm": 2}),
            flet.TextField(label="draining_sec", value="", border="underline", col={"xs": 4, "sm": 2}),
            flet.TextField(label="soaking_sec", value="", border="underline", col={"xs": 4, "sm": 2}),
        ]
    )
    time_tab = [
        server_info,
        flet.ElevatedButton("SET TIME", width=page.width),
        settime_form,
        flet.ElevatedButton("GET TIME"),
        settime_form,
    ]
    time = flet.Container(flet.Column(time_tab))

    # action tab
    action_tab = [server_info]
    action = flet.Container(flet.Column(action_tab))

    # exit tab
    exit_tab = [server_info, flet.ElevatedButton("Robot exit", on_click=open_dlg_modal, col={"xs": 12})]
    exit_ = flet.Container(flet.Column(exit_tab))

    # tab pages
    tab = flet.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            flet.Tab(text="State", icon=icons.MONITOR, content=state),
            flet.Tab(text="Time", icon=icons.TIMER, content=time),
            flet.Tab(text="Action", icon=icons.RUN_CIRCLE, content=action),
            flet.Tab(text="Exit", icon=icons.EXIT_TO_APP, content=exit_),
        ],
        expand=1,
    )

    # order
    def option_on_change(e):
        print(batter_option.value)
        if batter_option.value == "original":
            time_option.controls[2].value = "5"
        elif batter_option.value == "thin":
            time_option.controls[2].value = "9"
        elif batter_option.value == "custom":
            time_option.controls[2].value = "-1"
        page.update()

    bidxs = list(flet.Radio(value=f"{i}", label=f"{i}", col={"xs": 4}) for i in range(3))
    batter_index = flet.RadioGroup(content=flet.ResponsiveRow(bidxs), value="original", on_change=option_on_change)
    fidxs = list(flet.Radio(value=f"{i}", label=f"{i}", col={"xs": 4, "sm": 2}) for i in range(6))
    fryer_index = flet.RadioGroup(content=flet.ResponsiveRow(fidxs), value="original", on_change=option_on_change)

    batter_option = flet.RadioGroup(
        content=flet.ResponsiveRow(
            [
                flet.Radio(value="original", label="오리지널", col={"xs": 4}),
                flet.Radio(value="thin", label="얇게", col={"xs": 4}),
                flet.Radio(value="custom", label="커스텀", col={"xs": 4}),
            ]
        ),
        value="original",
        on_change=option_on_change,
    )
    time_option = flet.ResponsiveRow(
        [
            flet.TextField(label="frying_sec", value="-1", border="underline", col={"xs": 4}),
            flet.TextField(label="soaking_sec", value="-1", border="underline", col={"xs": 4}),
            flet.TextField(label="drain_sec", value="-1", border="underline", col={"xs": 4}),
        ]
    )
    option_on_change(None)

    order_form = flet.Container(
        flet.Column(
            [
                flet.Text("Batter index", style="headlineMedium"),
                batter_index,
                flet.Text("Fryer index", style="headlineMedium"),
                fryer_index,
                flet.Text("Batter option", style="headlineMedium"),
                batter_option,
                flet.Text("time option", style="headlineMedium"),
                time_option,
                flet.OutlinedButton("Send to robot"),
            ],
            scroll="auto",
        ),
        expand=True,
    )

    flet.ControlEvent
    # animate page
    def click_animate(e):
        a1.animate_scale = flet.Animation(400, e.control.text)
        a2.animate_rotation = flet.Animation(800, e.control.text)
        a3.animate_size = flet.Animation(800, e.control.text)
        a4.animate_offset = flet.Animation(800, e.control.text)
        a4.animate_opacity = flet.Animation(800, e.control.text)
        page.update()
        a1.scale = 0.8
        a2.rotate = 0
        a3.width = 50
        a4.offset = flet.transform.Offset(2, 0)
        a4.opacity = 0.2
        page.update()
        sleep(1)
        a1.scale = 1
        a2.rotate = 6.28
        a3.width = 100
        a4.offset = flet.transform.Offset(0, 0)
        a4.opacity = 1
        page.update()

    flet.Text(""),
    a1 = flet.Container(flet.Text("Scale"), bgcolor=colors.AMBER_800, width=100, height=100)
    a2 = flet.Container(flet.Text("Rotation"), bgcolor=colors.GREEN_800, width=100, height=100)
    a3 = flet.Container(flet.Text("Size"), bgcolor=colors.DEEP_ORANGE, width=100, height=100)
    a4 = flet.Container(flet.Text("Offset & Opacity"), bgcolor=colors.DEEP_PURPLE, width=100, height=50)
    r = []
    for ani in flet.AnimationCurve:
        r.append(flet.ElevatedButton(ani.value, on_click=click_animate, data=ani.value))

    animates = [
        flet.Row([a1, a2, a3]),
        a4,
        flet.Container(flet.Row(r, wrap=True, scroll="auto"), expand=True),
    ]
    animate_form = flet.Container(flet.Column(animates), expand=True)

    # audio page
    audio1 = flet.Audio(src="https://luan.xyz/files/audio/ambient_c_motion.mp3", autoplay=False)
    page.overlay.append(audio1)
    audio_container = flet.Container(
        content=flet.Column(
            [
                flet.Text("This is an app with background audio."),
                flet.ElevatedButton("Stop playing", on_click=lambda _: audio1.pause()),
                flet.ElevatedButton("Start playing", on_click=lambda _: audio1.play()),
            ]
        )
    )

    # image grid page
    images_grid = flet.GridView(
        expand=1,
        runs_count=5,
        max_extent=150,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
    )

    for i in range(0, 100):
        images_grid.controls.append(
            flet.Image(
                src=f"https://picsum.photos/150/150?{i}",
                fit=flet.ImageFit.NONE,
                repeat=flet.ImageRepeat.NO_REPEAT,
                border_radius=flet.border_radius.all(10),
            )
        )

    # setting page
    def always_on_top_changed(e):
        page.window_always_on_top = always_on_top.value
        page.update()

    def full_screen_changed(e):
        page.window_full_screen = full_screen.value
        page.update()

    always_on_top = flet.Switch(label="Always on top", value=False, on_change=always_on_top_changed)
    full_screen = flet.Switch(label="Full screen", value=False, on_change=full_screen_changed)

    def button_clicked(e):
        t.value = f"Checkboxes values are:  {b2.value}, {c2.value}, {c3.value}, {c4.value}, {c5.value}."
        page.update()

    def disable_update(e):
        c4.disabled = c3.value
        page.update()

    t = flet.Text()
    b2 = flet.Checkbox(label="Unchecked by default checkbox", value=False)
    c2 = flet.Checkbox(label="Undefined by default tristate checkbox", tristate=True, value=None)
    c3 = flet.Switch(label="Disable below checkbox", value=True, on_change=disable_update)
    c4 = flet.Checkbox(label="Disabled checkbox", disabled=True)
    c5 = flet.Checkbox(
        label="Checkbox with rendered label_position='left'",
        label_position=flet.LabelPosition.LEFT,
    )
    b = flet.ElevatedButton(text="Submit", on_click=button_clicked)

    results = flet.Column(scroll="auto", height=100)

    def rg1_on_change(e):
        results.controls.append(flet.Text(f"Selected value: {rg1.value}"))
        page.update()

    rg1_t = flet.Text("Radio with on_change", style="headlineMedium")
    rg1 = flet.RadioGroup(
        content=flet.Row(
            [
                flet.Radio(value="one", label="1"),
                flet.Radio(value="two", label="2"),
                flet.Radio(value="three", label="3"),
            ]
        ),
        value="two",
        on_change=rg1_on_change,
    )
    rg1_c = flet.Container(
        content=results,
        padding=10,
        border=flet.border.all(1, "black12"),
        border_radius=flet.border_radius.all(10),
        bgcolor="black12",
    )

    dd2_t = flet.Text("Dropdown with all decoration", style="headlineMedium")
    dd2 = flet.Dropdown(
        options=[
            flet.dropdown.Option("1", "One"),
            flet.dropdown.Option("2", "Two"),
            flet.dropdown.Option("3", "Three"),
        ],
        label="My favorite number",
        icon="format_size",
        hint_text="Choose your favorite color",
        helper_text="You can choose only one color",
        counter_text="0 colors selected",
        prefix_icon="color_lens",
        suffix_text="...is your color",
    )
    settings = [always_on_top, full_screen, b2, c2, c3, c4, c5, b, t, rg1_t, rg1, rg1_c, dd2_t, dd2]
    setting_form = flet.Container(content=flet.Column(settings, scroll="auto"), expand=True)

    # markdown page
    md = flet.ListView(
        [flet.Markdown(md1, selectable=True, extension_set="gitHubWeb", on_tap_link=lambda e: page.launch_url(e.data))],
        expand=True,
    )

    # responsive rowlayout
    row_texts = [
        flet.Container(flet.Text(f"row {i}"), padding=5, bgcolor=colors.ON_SECONDARY, col={"sm": 6, "md": 4, "xl": 2})
        for i in range(10)
    ]
    row_tfs = [flet.TextField(label=f"TF {i}", col={"xs": 6, "sm": 3, "md": 2, "xl": 1}) for i in range(10)]
    responsive_row = flet.Container(
        flet.Column(
            [
                flet.Text("가로 길이에 따른 반응형 배치"),
                flet.ResponsiveRow(row_texts),
                flet.ResponsiveRow(row_tfs, run_spacing={"xs": 10}),
            ],
            scroll="auto",
        ),
        expand=True,
    )

    # navigation rail
    hf = flet.HapticFeedback()
    page.overlay.append(hf)

    def rail_extend_convert(e):
        if rail.extended:
            rail.extended = False
        else:
            rail.extended = True
        page.update()

    def rail_select_page():
        print(f"Selected index: {rail.selected_index}")
        for index, p in enumerate(mains):
            p.visible = True if index == rail.selected_index else False
        rail.extended = False
        page.update()

    def rail_dest_change(e):
        rail_select_page()
        hf.heavy_impact()

    mains = [
        tab,
        order_form,
        animate_form,
        audio_container,
        images_grid,
        md,
        responsive_row,
        setting_form,
    ]
    main_form = flet.Column(mains, alignment="start", expand=True)

    rail = flet.NavigationRail(
        selected_index=0,
        label_type="none",
        extended=False,
        height=page.height,
        min_width=30,
        min_extended_width=200,
        group_alignment=-0.98,
        destinations=[
            flet.NavigationRailDestination(icon=icons.HANDSHAKE, label="Robot"),
            flet.NavigationRailDestination(icon_content=flet.Icon(icons.MENU_BOOK), label="Order"),
            flet.NavigationRailDestination(icon_content=flet.Icon(icons.ROCKET_LAUNCH), label="Animate"),
            flet.NavigationRailDestination(icon=icons.SPEAKER, label_content=flet.Text("flet.Audio")),
            flet.NavigationRailDestination(icon=icons.IMAGE, label_content=flet.Text("Image")),
            flet.NavigationRailDestination(icon=icons.DOCUMENT_SCANNER, label_content=flet.Text("Markdown")),
            flet.NavigationRailDestination(icon=icons.STAR, label_content=flet.Text("Responsive row")),
            flet.NavigationRailDestination(icon=icons.SETTINGS, label_content=flet.Text("Settings")),
        ],
        on_change=rail_dest_change,
    )
    rail_select_page()

    # app bar
    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()

    page.title = "Flet setting app"
    page.theme_mode = "dark"
    page.theme = theme.Theme(color_scheme_seed=LIGHT_SEED_COLOR, use_material3=True)
    page.dark_theme = theme.Theme(color_scheme_seed=DARK_SEED_COLOR, use_material3=True)
    page.update()

    def toggle_theme_mode(e):
        page.theme_mode = "dark" if page.theme_mode == "light" else "light"
        lightMode.icon = icons.WB_SUNNY_OUTLINED if page.theme_mode == "light" else icons.WB_SUNNY
        page.update()

    lightMode = flet.IconButton(
        icons.WB_SUNNY_OUTLINED if page.theme_mode == "light" else icons.WB_SUNNY,
        on_click=toggle_theme_mode,
    )

    def toggle_material(e):
        use_material3 = not page.theme.use_material3
        page.theme = theme.Theme(color_scheme_seed=LIGHT_SEED_COLOR, use_material3=use_material3)
        page.dark_theme = theme.Theme(color_scheme_seed=DARK_SEED_COLOR, use_material3=use_material3)
        materialMode.icon = icons.FILTER_3 if page.theme.use_material3 else icons.FILTER_2
        page.update()

    materialMode = flet.IconButton(
        icons.FILTER_3 if page.theme.use_material3 else icons.FILTER_2,
        on_click=toggle_material,
    )

    page.appbar = flet.AppBar(
        # toolbar_height=100,
        bgcolor=colors.SECONDARY_CONTAINER,
        leading=flet.IconButton(
            icon=icons.MENU,
            on_click=rail_extend_convert,
        ),
        leading_width=40,
        title=flet.Text("Setting web app"),
        center_title=False,
        actions=[
            lightMode,
            materialMode,
            flet.PopupMenuButton(
                items=[
                    flet.PopupMenuItem(text="Item 1"),
                    flet.PopupMenuItem(icon=icons.POWER_INPUT, text="Check power"),
                    flet.PopupMenuItem(),  # divider
                    flet.PopupMenuItem(text="Checked item", checked=False, on_click=check_item_clicked),
                ]
            ),
        ],
    )

    # add page
    logs = flet.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
    log_form = flet.Container(logs, height=page.height * 0.1)
    page.add(
        flet.Row(
            [
                rail,
                flet.VerticalDivider(width=1),
                flet.Column(
                    [main_form, flet.Divider(), log_form],
                    expand=True,
                ),
            ],
            expand=True,
        )
    )

    for i in range(0, 60):
        sleep(1)
        logs.controls.append(flet.Text(f"One line add per sec, log updating {i}"))
        log_form.height = page.height * 0.1
        page.update()


flet.app(target=main)  # run pc application
# flet.app(target=main, port=8080, view=flet.WEB_BROWSER)  # run web app
