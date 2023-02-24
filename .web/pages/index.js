import {useEffect, useRef, useState} from "react"
import {useRouter} from "next/router"
import {E, connect, updateState} from "/utils/state"
import "focus-visible/dist/focus-visible"
import {Button, Center, Drawer, DrawerBody, DrawerContent, DrawerFooter, DrawerHeader, DrawerOverlay, Flex, HStack, Heading, Image, Input, Spacer, Square, Text, VStack} from "@chakra-ui/react"
import {CloseIcon} from "@chakra-ui/icons"
import NextHead from "next/head"

const EVENT = "ws://localhost:8000/event"
export default function Component() {
const [state, setState] = useState({"Auth": false, "drawer_state": {}, "show_signIn": false, "show_signUp": false, "show_user": false, "sign_in_state": {"confirm_password": "", "email": "", "password": "", "user_id": "", "username": ""}, "events": [{"name": "state.hydrate"}]})
const [result, setResult] = useState({"state": null, "events": [], "processing": false})
const router = useRouter()
const socket = useRef(null)
const { isReady } = router;
const Event = events => setState({
  ...state,
  events: [...state.events, ...events],
})
useEffect(() => {
  if(!isReady)
    return;
  if (!socket.current) {
    connect(socket, state, result, setResult, router, EVENT)
  }
  const update = async () => {
    if (result.state != null) {
      setState({
        ...result.state,
        events: [...state.events, ...result.events],
      })
      setResult({
        state: null,
        events: [],
        processing: false,
      })
    }
    await updateState(state, result, setResult, router, socket.current)
  }
  update()
})
return (
<VStack sx={{"width": "100%"}}>
<Flex sx={{"width": "100%", "height": "15vh"}}>
<Square>
<Center sx={{"padding": 10}}>
<Image src="/logo.png"
sx={{"width": "5em"}}/></Center></Square>
<Spacer/>
<Square>
<Center sx={{"padding": 10}}>
<Heading>
{`My Blog`}</Heading></Center></Square>
<Spacer/>
<Square>
<Center sx={{"padding": 10}}>
<Button onClick={() => Event([E("state.drawer_state.show_drawer", {})])}
sx={{"width": "3em", "height": "3em", "padding": 0, "borderRadius": "3em", "_hover": {"bg": "lightgray"}}}>
<Image src="/person.png"
sx={{"width": "2em"}}/></Button>
<Drawer isOpen={state.show_signIn}>
<DrawerOverlay>
<DrawerContent>
<DrawerHeader>
<HStack justifyContent="right">
<Square sx={{"_hover": {"bg": "lightgray"}, "width": "2em", "height": "2em", "borderRadius": "3em"}}>
<CloseIcon onClick={() => Event([E("state.drawer_state.close_signIn_drawer", {})])}
sx={{"width": "0.8em", "height": "0.8em"}}/></Square></HStack>
<Center>
{`Sign in`}</Center></DrawerHeader>
<DrawerBody>
<VStack>
<Input placeholder="ID"
type="text"
onBlur={(_e) => Event([E("state.sign_in_state.set_user_id", {value:_e.target.value})])}
sx={{"width": "15em"}}/>
<Input placeholder="Password"
type="password"
onBlur={(_e) => Event([E("state.sign_in_state.set_password", {value:_e.target.value})])}
sx={{"width": "15em"}}/>
<Center>
<HStack>
<Button onClick={() => Event([E("state.sign_in_state.signIn", {})])}
sx={{"width": "7em"}}>
<Text>
{`Sign in`}</Text></Button>
<Spacer/>
<Button onClick={() => Event([E("state.sign_in_state.goSignUp", {})])}
sx={{"width": "7em"}}>
<Text>
{`Sign up`}</Text></Button></HStack></Center></VStack></DrawerBody>
<DrawerFooter/></DrawerContent></DrawerOverlay></Drawer>
<Drawer isOpen={state.show_user}>
<DrawerOverlay>
<DrawerContent>
<DrawerHeader>
<HStack justifyContent="right">
<Square sx={{"_hover": {"bg": "lightgray"}, "width": "2em", "height": "2em", "borderRadius": "3em"}}>
<CloseIcon onClick={() => Event([E("state.drawer_state.close_user_drawer", {})])}
sx={{"width": "0.8em", "height": "0.8em"}}/></Square></HStack>
<Center>
{`Signed`}</Center></DrawerHeader>
<DrawerBody>
<Center>
<Button onClick={() => Event([E("state.signOut", {})])}>
{`Sign out`}</Button></Center></DrawerBody>
<DrawerFooter/></DrawerContent></DrawerOverlay></Drawer>
<Drawer isOpen={state.show_signUp}>
<DrawerOverlay>
<DrawerContent>
<DrawerHeader>
<HStack justifyContent="right">
<Square sx={{"_hover": {"bg": "lightgray"}, "width": "2em", "height": "2em", "borderRadius": "3em"}}>
<CloseIcon onClick={() => Event([E("state.drawer_state.close_signUp_drawer", {})])}
sx={{"width": "0.8em", "height": "0.8em"}}/></Square></HStack>
<Center>
{`Sign up`}</Center></DrawerHeader>
<VStack>
<Input placeholder="ID"
type="text"
onBlur={(_e) => Event([E("state.sign_in_state.set_user_id", {value:_e.target.value})])}
sx={{"width": "15em"}}/>
<Input placeholder="Username"
type="text"
onBlur={(_e) => Event([E("state.sign_in_state.set_username", {value:_e.target.value})])}
sx={{"width": "15em"}}/>
<Input placeholder="email"
type="text"
onBlur={(_e) => Event([E("state.sign_in_state.set_email", {value:_e.target.value})])}
sx={{"width": "15em"}}/>
<Input placeholder="Password"
type="password"
onBlur={(_e) => Event([E("state.sign_in_state.set_password", {value:_e.target.value})])}
sx={{"width": "15em"}}/>
<Input placeholder="Confirm Password"
type="password"
onBlur={(_e) => Event([E("state.sign_in_state.set_confirm_password", {value:_e.target.value})])}
sx={{"width": "15em"}}/>
<Center>
<HStack>
<Button onClick={() => Event([E("state.sign_in_state.signUp", {})])}
sx={{"width": "7em"}}>
<Text>
{`Confirm`}</Text></Button>
<Spacer/>
<Button onClick={() => Event([E("state.sign_in_state.cancelSignUp", {})])}
sx={{"width": "7em"}}>
<Text>
{`Cancel`}</Text></Button></HStack></Center></VStack>
<DrawerFooter/></DrawerContent></DrawerOverlay></Drawer></Center></Square></Flex>
<Square>
<Center sx={{"width": "75vw", "height": "135vh", "bg": "yellow", "padding": 10}}>
<Text>
{`Body Area`}</Text></Center></Square>
<Square sx={{"width": "100%", "height": "20vh", "bg": "blue"}}>
<Center>
<Text sx={{"fontSize": "2em", "color": "yellow"}}>
{`Footer Area`}</Text></Center></Square>
<NextHead>
<title>{`Pynecone App`}</title>
<meta name="description"
content="A Pynecone app."/>
<meta content="favicon.ico"
property="og:image"/></NextHead></VStack>
)
}