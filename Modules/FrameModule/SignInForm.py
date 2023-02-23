"""
    sign in 관련 모듈
"""
from Modules.States.SignInState import signInState
import pynecone as pc

class signInForm:
    def signIn():
        return pc.vstack(
            pc.input(placeholder="ID",
                on_blur=signInState.set_user_id,
                width="15em",
            ),
            pc.input(placeholder="Password",
                type_="password",
                on_blur=signInState.set_password,
                width="15em",
            ),
            pc.center(
                pc.hstack(
                    pc.button(
                        pc.text("Sign in"),
                        on_click=signInState.signIn,
                        width="7em"
                    ),
                    pc.spacer(),
                    pc.button(
                        pc.text("Sign up"),
                        on_click=signInState.goSignUp,
                        width="7em"
                    )
                )
            ),
        )
    
    def signUp():
        return pc.vstack(
            pc.input(
                placeholder="ID",
                on_blur=signInState.set_user_id,
                width="15em"
            ),
            pc.input(
                placeholder="Username",
                on_blur=signInState.set_username,
                width="15em"
            ),
            pc.input(
                placeholder="email",
                on_blur=signInState.set_email,
                width="15em"
            ),
            pc.input(
                placeholder="Password",
                on_blur=signInState.set_password,
                width="15em",
                type_="password"
            ),
            pc.input(
                placeholder="Confirm Password",
                on_blur=signInState.set_confirm_password,
                width="15em",
                type_="password"
            ),
            pc.center(
                pc.hstack(
                    pc.button(
                        pc.text("Confirm"),
                        on_click=signInState.signUp,
                        width="7em"
                    ),
                    pc.spacer(),
                    pc.button(
                        pc.text("Cancel"),
                        on_click=signInState.cancelSignUp,
                        width="7em"
                    )
                )
            )
        )