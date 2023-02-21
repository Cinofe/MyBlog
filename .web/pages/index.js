import {useEffect, useRef, useState} from "react"
import {useRouter} from "next/router"
import {E, connect, updateState} from "/utils/state"
import "focus-visible/dist/focus-visible"
import {Button, Center, Drawer, DrawerBody, DrawerContent, DrawerFooter, DrawerHeader, DrawerOverlay, Flex, HStack, Heading, Image, Input, Spacer, Square, Text, VStack} from "@chakra-ui/react"
import {CloseIcon, HamburgerIcon} from "@chakra-ui/icons"
import NextHead from "next/head"

const EVENT = "ws://localhost:8000/event"
export default function Component() {
const [state, setState] = useState({"Permission": false, "id": "", "pw": "", "show_signIn": false, "show_signUp": false, "show_user": false, "events": [{"name": "state.hydrate"}]})
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
<Square sx={{"padding": 10}}>
<Image src="/logo.png"
sx={{"width": "5em"}}/></Square>
<Spacer/>
<Square sx={{"padding": 10}}>
<Heading>
{`My Blog`}</Heading></Square>
<Spacer/>
<Square sx={{"padding": 10}}>
<Button onClick={() => Event([E("state.show_drawer", {})])}
sx={{"width": "5vw", "bg": "lightgray"}}>
<HamburgerIcon sx={{"width": "1.5em", "height": "1.5em"}}/></Button>
<Drawer isOpen={state.show_signIn}>
<DrawerOverlay>
<DrawerContent>
<DrawerHeader>
<HStack justifyContent="right">
<CloseIcon onClick={() => Event([E("state.close_signIn_drawer", {})])}/></HStack>
<Center>
{`Sign in`}</Center></DrawerHeader>
<DrawerBody>
<VStack>
<Input type="text"
placeholder="ID"
onChange={(_e) => Event([E("state.set_id", {id:_e.target.value})])}
sx={{"width": "15em"}}/>
<Input type="password"
placeholder="PW"
onChange={(_e) => Event([E("state.set_pw", {pw:_e.target.value})])}
sx={{"width": "15em"}}/>
<Center>
<HStack>
<Button onClick={() => Event([E("state.show_data", {})])}
sx={{"width": "7em"}}>
<Text>
{`Sign in`}</Text></Button>
<Spacer/>
<Button onClick={() => Event([E("state.show_signUp_drawer", {})])}
sx={{"width": "7em"}}>
<Text>
{`Sign up`}</Text></Button></HStack></Center></VStack></DrawerBody>
<DrawerFooter/></DrawerContent></DrawerOverlay></Drawer>
<Drawer isOpen={state.show_user}>
<DrawerOverlay>
<DrawerContent>
<DrawerHeader>
<HStack justifyContent="right">
<CloseIcon onClick={() => Event([E("state.close_user_drawer", {})])}/></HStack>
<Center>
{`Signed`}</Center></DrawerHeader></DrawerContent></DrawerOverlay></Drawer>
<Drawer isOpen={state.show_signUp}>
<DrawerOverlay>
<DrawerContent>
<DrawerHeader sx={{"justifyContent": "right"}}>
<HStack>
<CloseIcon onClick={() => Event([E("state.close_signUp_drawer", {})])}/></HStack></DrawerHeader>
<Center>
{`Sign up`}</Center></DrawerContent></DrawerOverlay></Drawer></Square></Flex>
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
<meta content="A Pynecone app."
name="description"/>
<meta property="og:image"
content="favicon.ico"/></NextHead></VStack>
)
}