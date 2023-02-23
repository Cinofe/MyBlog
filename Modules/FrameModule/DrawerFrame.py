"""
    Drawer 구성 요소 간략화
"""
import pynecone as pc

class drawerFrame:
    
    def drawer(head= pc.drawer_header(), body=pc.drawer_body(), footer=pc.drawer_footer(), isOpen = False):
        return pc.drawer(
            pc.drawer_overlay(
                pc.drawer_content(
                    head,body,footer,
                )
            ),
            is_open = isOpen
        )