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
                value = signInState.user_id,
                placeholder="ID",
                on_change=signInState.set_user_id,
                width="15em"
            ),
            pc.input(
                value = signInState.username,
                placeholder="Username",
                on_change=signInState.set_username,
                width="15em"
            ),
            pc.input(
                value = signInState.email,
                placeholder="email",
                on_change=signInState.set_email,
                width="15em"
            ),
            pc.input(
                value = signInState.password,
                placeholder="Password",
                on_change=signInState.set_password,
                width="15em",
                type_="password"
            ),
            pc.input(
                value = signInState.confirm_password,
                placeholder="Confirm Password",
                on_change=signInState.set_confirm_password,
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