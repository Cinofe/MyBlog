import {useEffect, useRef, useState} from "react"
import {useRouter} from "next/router"
import {E, connect, updateState} from "/utils/state"
import "focus-visible/dist/focus-visible"
import {Badge, Box, Button, Center, Drawer, DrawerBody, DrawerContent, DrawerFooter, DrawerHeader, DrawerOverlay, Flex, HStack, Heading, Image, Input, Link, Modal, ModalBody, ModalContent, ModalFooter, ModalHeader, ModalOverlay, Spacer, Square, Text, Textarea, VStack, useColorMode} from "@chakra-ui/react"
import {CloseIcon} from "@chakra-ui/icons"
import NextLink from "next/link"
import NextHead from "next/head"

const EVENT = "ws://localhost:8000/event"
export default function Component() {
const [state, setState] = useState({"Auth": false, "drawer_state": {"UNAME": ""}, "post_state": {"post_text": "", "show_modal": false}, "show_admin_user": false, "show_signIn": false, "show_signUp": false, "show_user": false, "sign_in_state": {"confirm_password": "", "email": "", "password": "", "user_id": "", "username": ""}, "user_state": {"ADMIN": false, "UID": "", "UNAME": ""}, "events": [{"name": "state.hydrate"}]})
const [result, setResult] = useState({"state": null, "events": [], "processing": false})
const router = useRouter()
const socket = useRef(null)
const { isReady } = router;
const { colorMode, toggleColorMode } = useColorMode()
const Event = events => setState({
  ...state,
  events: [...state.events, ...events],
})
useEffect(() => {
  if(!isReady) {
    return;
  }
  if (!socket.current) {
    connect(socket, state, setState, result, setResult, router, EVENT, ['websocket', 'polling'])
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
    await updateState(state, setState, result, setResult, router, socket.current)
  }
  update()
})
return (
<VStack sx={{"width": "100%"}}><Flex sx={{"width": "100%", "height": "15vh"}}><Box sx={{"position": "Fixed", "width": "100%", "top": "0px"}}><HStack justify="space-between"
sx={{"borderBottom": "0.2em solid #F0F0F0", "paddingX": "2em", "bg": "rgba(255,255,255, 0.75)"}}><HStack><Image src="/logo.png"
sx={{"width": "75px"}}/>
<Heading size="lg">{`My Blog`}</Heading>
<Flex><Badge colorScheme="blue">{`2022-2023 Season`}</Badge></Flex></HStack>
<Square><Center sx={{"padding": 10}}><Button onClick={() => Event([E("state.drawer_state.show_drawer", {})])}
sx={{"width": "3.5em", "height": "3.5em", "padding": 0, "borderRadius": "4em", "_hover": {"bg": "lightgray"}}}><Image src="/person.png"
sx={{"width": "2em"}}/></Button>
<Drawer isOpen={state.show_signIn}><DrawerOverlay><DrawerContent><DrawerHeader><HStack justifyContent="right"><Square onClick={() => Event([E("state.drawer_state.close_signIn_drawer", {})])}
sx={{"_hover": {"bg": "lightgray"}, "width": "2em", "height": "2em", "borderRadius": "3em"}}><CloseIcon sx={{"width": "0.8em", "height": "0.8em"}}/></Square></HStack>
<Center>{`Sign in`}</Center></DrawerHeader>
<DrawerBody><VStack><Input value={state.sign_in_state.user_id}
placeholder="ID"
type="text"
onChange={(_e) => Event([E("state.sign_in_state.set_user_id", {value:_e.target.value})])}
onKeyDown={(_e) => Event([E("state.sign_in_state.idKeyDown", {key:_e.key})])}
sx={{"width": "15em"}}/>
<Input value={state.sign_in_state.password}
placeholder="Password"
type="password"
onChange={(_e) => Event([E("state.sign_in_state.set_password", {value:_e.target.value})])}
onKeyDown={(_e) => Event([E("state.sign_in_state.pwKeyDown", {key:_e.key})])}
sx={{"width": "15em"}}/>
<Center><HStack><Button onClick={() => Event([E("state.sign_in_state.signIn", {})])}
sx={{"width": "7em"}}><Text>{`Sign in`}</Text></Button>
<Spacer/>
<Button onClick={() => Event([E("state.sign_in_state.goSignUp", {})])}
sx={{"width": "7em"}}><Text>{`Sign up`}</Text></Button></HStack></Center></VStack></DrawerBody>
<DrawerFooter/></DrawerContent></DrawerOverlay></Drawer>
<Drawer isOpen={state.show_user}><DrawerOverlay><DrawerContent><DrawerHeader><HStack justifyContent="right"><Square onClick={() => Event([E("state.drawer_state.close_user_drawer", {})])}
sx={{"_hover": {"bg": "lightgray"}, "width": "2em", "height": "2em", "borderRadius": "3em"}}><CloseIcon sx={{"width": "0.8em", "height": "0.8em"}}/></Square></HStack>
<Center><Heading>{("Hi! " + state.drawer_state.UNAME)}</Heading></Center></DrawerHeader>
<DrawerBody/>
<DrawerFooter><HStack justifyContent="center"><NextLink href="#"
passHref={true}><Link onClick={() => Event([E("state.signOut", {})])}
sx={{"_hover": {"color": "rgb(107,99,246)", "fontSize": "1.2em"}}}>{`Sign out`}</Link></NextLink></HStack></DrawerFooter></DrawerContent></DrawerOverlay></Drawer>
<Drawer isOpen={state.show_signUp}><DrawerOverlay><DrawerContent><DrawerHeader><HStack justifyContent="right"><Square onClick={() => Event([E("state.drawer_state.close_signUp_drawer", {})])}
sx={{"_hover": {"bg": "lightgray"}, "width": "2em", "height": "2em", "borderRadius": "3em"}}><CloseIcon sx={{"width": "0.8em", "height": "0.8em"}}/></Square></HStack>
<Center>{`Sign up`}</Center></DrawerHeader>
<VStack><Input value={state.sign_in_state.user_id}
placeholder="ID"
type="text"
onChange={(_e) => Event([E("state.sign_in_state.set_user_id", {value:_e.target.value})])}
sx={{"width": "15em"}}/>
<Input value={state.sign_in_state.username}
placeholder="Username"
type="text"
onChange={(_e) => Event([E("state.sign_in_state.set_username", {value:_e.target.value})])}
sx={{"width": "15em"}}/>
<Input value={state.sign_in_state.email}
placeholder="email"
type="text"
onChange={(_e) => Event([E("state.sign_in_state.set_email", {value:_e.target.value})])}
sx={{"width": "15em"}}/>
<Input value={state.sign_in_state.password}
placeholder="Password"
type="password"
onChange={(_e) => Event([E("state.sign_in_state.set_password", {value:_e.target.value})])}
sx={{"width": "15em"}}/>
<Input value={state.sign_in_state.confirm_password}
placeholder="Confirm Password"
type="password"
onChange={(_e) => Event([E("state.sign_in_state.set_confirm_password", {value:_e.target.value})])}
sx={{"width": "15em"}}/>
<Center><HStack><Button onClick={() => Event([E("state.sign_in_state.signUp", {})])}
sx={{"width": "7em"}}><Text>{`Confirm`}</Text></Button>
<Spacer/>
<Button onClick={() => Event([E("state.sign_in_state.cancelSignUp", {})])}
sx={{"width": "7em"}}><Text>{`Cancel`}</Text></Button></HStack></Center></VStack>
<DrawerFooter/></DrawerContent></DrawerOverlay></Drawer>
<Drawer isOpen={state.show_admin_user}><DrawerOverlay><DrawerContent><DrawerHeader><HStack justifyContent="right"><Square onClick={() => Event([E("state.drawer_state.close_admin_drawer", {})])}
sx={{"_hover": {"bg": "lightgray"}, "width": "2em", "height": "2em", "borderRadius": "3em"}}><CloseIcon sx={{"width": "0.8em", "height": "0.8em"}}/></Square></HStack>
<Center>{`Admin Signed`}</Center></DrawerHeader>
<DrawerBody><VStack><Center><Button onClick={() => Event([E("state.post_state.posting", {})])}
sx={{"width": "15vw"}}>{`Post`}</Button></Center></VStack></DrawerBody>
<DrawerFooter><HStack justifyContent="center"><NextLink href="#"
passHref={true}><Link onClick={() => Event([E("state.signOut", {})])}
sx={{"_hover": {"color": "rgb(107,99,246)", "fontSize": "1.2em"}}}>{`Sign out`}</Link></NextLink></HStack></DrawerFooter></DrawerContent></DrawerOverlay></Drawer></Center></Square></HStack></Box>
<Spacer/></Flex>
<Square><Center sx={{"width": "65vw", "height": "135vh", "bg": "yellow", "padding": 10}}><Text>{`Body Area`}</Text></Center>
<Box><Modal size="5xl"
isOpen={state.post_state.show_modal}><ModalOverlay><ModalContent><ModalHeader>{`Posting`}</ModalHeader>
<ModalBody><VStack><HStack/>
<Textarea value={state.post_state.post_text}
onChange={(_e) => Event([E("state.post_state.setText", {text:_e.target.value})])}
sx={{"height": "30vw"}}/></VStack></ModalBody>
<ModalFooter><Button onClick={() => Event([E("state.post_state.closeModal", {})])}>{`Close`}</Button></ModalFooter></ModalContent></ModalOverlay></Modal></Box></Square>
<Square sx={{"width": "100%", "height": "20vh", "bg": "blue"}}><Center><Text sx={{"fontSize": "2em", "color": "yellow"}}>{`Footer Area`}</Text></Center></Square>
<NextHead><title>{`Pynecone App`}</title>
<meta name="description"
content="A Pynecone app."/>
<meta content="favicon.ico"
property="og:image"/></NextHead></VStack>
)
}